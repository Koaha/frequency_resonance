# src/core/signal_processing/sqi_scorer.py
"""SQI scoring: composite statistical scorer (legacy) and robust scale-agnostic scorer.

Two public entry-points
-----------------------
score_windows()          — original weighted composite scorer  (config: CompositeConfig)
robust_score_windows()   — new rank-based consensus scorer     (config: RobustConfig)

The robust scorer is completely independent of SQI units and scale.  It operates
entirely in rank space and automatically detects the file's noise regime before
choosing the appropriate classification strategy.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple

import logging
import numpy as np
from scipy import stats

logger = logging.getLogger(__name__)


# =============================================================================
# SECTION 1 — Legacy composite scorer
# =============================================================================

@dataclass
class CompositeConfig:
    """Parameters for the legacy composite statistical thresholding."""
    min_quantile: float = 10.0
    max_tail_area: float = 0.05
    max_modified_z: float = 3.0
    min_trapz_ratio: float = 0.3
    max_rolling_var: float = 2.0
    weights: List[float] = field(default_factory=lambda: [0.25, 0.20, 0.20, 0.20, 0.15])
    score_threshold: float = 0.7
    # Absolute sanity bound: if any metric's raw value has |value| > this,
    # the window is forced abnormal.  Catches degenerate cases where all
    # windows in a file share the same extreme value (zero intra-file variance)
    # so the relative statistics cannot detect the outlier.
    abs_max_sqi: float = 10.0

    def __post_init__(self):
        if len(self.weights) != 5:
            raise ValueError("weights must have exactly 5 elements")
        total = sum(self.weights)
        if total > 0:
            self.weights = [w / total for w in self.weights]


# ── shared helpers ────────────────────────────────────────────────────────────

def _sanitize(values: np.ndarray) -> np.ndarray:
    """Replace NaN/inf with the finite median (or 0 if all non-finite)."""
    v = values.copy()
    finite_mask = np.isfinite(v)
    if finite_mask.all():
        return v
    if not finite_mask.any():
        return np.zeros_like(v)
    fill = np.median(v[finite_mask])
    v[~finite_mask] = fill
    return v


# ── per-window feature functions ──────────────────────────────────────────────

def _quantile_ranks(values: np.ndarray) -> np.ndarray:
    """Percentile rank of each value within the array (0–1)."""
    v = _sanitize(values)
    n = len(v)
    if n < 2:
        return np.ones(n)
    ranks = stats.rankdata(v, method="average")
    return (ranks - 1) / (n - 1)


def _modified_z_scores(values: np.ndarray) -> np.ndarray:
    """Robust z-scores using median and MAD."""
    v = _sanitize(values)
    median = np.median(v)
    mad = np.median(np.abs(v - median))
    if mad < 1e-12:
        return np.zeros_like(v)
    return 0.6745 * (v - median) / mad


def _tail_probabilities(values: np.ndarray) -> np.ndarray:
    """Two-sided tail probability assuming approximate normality.

    Returns the probability mass *beyond* each value in the corresponding
    tail (low values → left tail, high values → right tail).  Clamped to
    [0, 1] and oriented so that *lower* probability = more extreme.
    """
    v = _sanitize(values)
    n = len(v)
    if n < 3:
        return np.full(n, 0.5)
    mu, sigma = np.mean(v), np.std(v, ddof=1)
    if sigma < 1e-12:
        return np.full(n, 0.5)
    z = (v - mu) / sigma
    return 2.0 * stats.norm.sf(np.abs(z))


def _trapz_ratios(signal: np.ndarray, window: int, step: int) -> np.ndarray:
    """Trapezoidal-integration ratio per window vs the global median window area.

    Captures sustained signal loss / flatline vs. normal signal energy.
    """
    n_windows = max(0, (len(signal) - window) // step + 1)
    if n_windows == 0:
        return np.array([])

    areas = np.empty(n_windows)
    for i in range(n_windows):
        seg = signal[i * step: i * step + window]
        areas[i] = np.trapz(np.abs(seg))

    ref = np.median(areas)
    if ref < 1e-12:
        return np.ones(n_windows)
    return np.clip(areas / ref, 0.0, None)


def _rolling_variances(values: np.ndarray, half_window: int = 2) -> np.ndarray:
    """Local variance of SQI values in a rolling window around each index."""
    v = _sanitize(values)
    n = len(v)
    if n < 3:
        return np.zeros(n)
    out = np.empty(n)
    for i in range(n):
        lo = max(0, i - half_window)
        hi = min(n, i + half_window + 1)
        out[i] = np.var(v[lo:hi], ddof=0)
    return out


# ── composite scorer ──────────────────────────────────────────────────────────

def score_windows(
    sqi_values: Dict[str, np.ndarray],
    signal: np.ndarray,
    window: int,
    step: int,
    config: CompositeConfig,
) -> Dict[str, Any]:
    """Compute composite quality scores for each window.

    Parameters
    ----------
    sqi_values : dict mapping metric_name → 1-D array of per-window SQI values
    signal     : raw signal array (used for trapz ratio)
    window     : window size in samples
    step       : step size in samples
    config     : CompositeConfig

    Returns
    -------
    dict with keys:
        composite_scores : list[float]  — per-window composite score (0–1)
        quality          : list[str]    — "normal" / "abnormal"
        normal_segments  : list[tuple]  — (start_sample, end_sample)
        abnormal_segments: list[tuple]
        details          : dict         — per-metric intermediate arrays
    """
    n_windows = max(0, (len(signal) - window) // step + 1)
    if n_windows == 0:
        return _empty_result()

    metrics = [
        m for m in sqi_values
        if len(sqi_values[m]) == n_windows and np.any(np.isfinite(sqi_values[m]))
    ]
    if not metrics:
        return _empty_result()

    w = config.weights

    trapz = _trapz_ratios(signal, window, step)
    if len(trapz) != n_windows:
        trapz = np.ones(n_windows)

    per_metric_scores: Dict[str, np.ndarray] = {}
    for metric in metrics:
        vals = np.asarray(sqi_values[metric], dtype=float)

        qr = _quantile_ranks(vals)
        tp = _tail_probabilities(vals)
        mz = _modified_z_scores(vals)
        rv = _rolling_variances(vals)

        s_quantile = qr
        s_tail = np.where(tp >= config.max_tail_area, 1.0, tp / config.max_tail_area)
        s_mz = 1.0 / (1.0 + np.abs(mz) / config.max_modified_z)
        s_trapz = np.clip(trapz / max(config.min_trapz_ratio, 1e-12), 0, 1)
        s_rv = 1.0 / (1.0 + rv / max(config.max_rolling_var, 1e-12))

        composite = (
            w[0] * s_quantile
            + w[1] * s_tail
            + w[2] * s_mz
            + w[3] * s_trapz
            + w[4] * s_rv
        )
        per_metric_scores[metric] = composite

    if not per_metric_scores:
        return _empty_result()

    all_scores = np.stack(list(per_metric_scores.values()), axis=0)
    final_scores = np.nanmean(all_scores, axis=0)
    final_scores = np.where(np.isfinite(final_scores), final_scores, 0.0)

    # Absolute sanity check: force windows to 0 if ANY metric's raw value
    # exceeds abs_max_sqi.  This catches degenerate files where all windows
    # share the same extreme value and the relative statistics can't detect it.
    if config.abs_max_sqi > 0:
        for metric in metrics:
            vals = np.asarray(sqi_values[metric], dtype=float)
            abs_outlier = np.abs(vals) > config.abs_max_sqi
            if np.any(abs_outlier):
                n_flagged = int(np.sum(abs_outlier))
                logger.info(
                    "abs_max_sqi: %d/%d windows in '%s' exceed ±%.1f — forced abnormal",
                    n_flagged, n_windows, metric, config.abs_max_sqi,
                )
                final_scores[abs_outlier] = 0.0

    quality = ["normal" if s >= config.score_threshold else "abnormal" for s in final_scores]

    normal_segs = []
    abnormal_segs = []
    for i in range(n_windows):
        start = i * step
        end = start + window
        if quality[i] == "normal":
            normal_segs.append((int(start), int(end)))
        else:
            abnormal_segs.append((int(start), int(end)))

    details: Dict[str, Any] = {}
    for metric in metrics:
        vals = np.asarray(sqi_values[metric], dtype=float)
        details[metric] = {
            "quantile_rank": _round_list(_quantile_ranks(vals)),
            "tail_probability": _round_list(_tail_probabilities(vals)),
            "modified_z_score": _round_list(_modified_z_scores(vals)),
            "rolling_variance": _round_list(_rolling_variances(vals)),
            "metric_composite": _round_list(per_metric_scores[metric]),
        }
    details["trapz_ratio"] = _round_list(trapz)

    return {
        "composite_scores": _round_list(final_scores),
        "quality": quality,
        "normal_segments": normal_segs,
        "abnormal_segments": abnormal_segs,
        "score_threshold": config.score_threshold,
        "details": details,
    }


def _round_list(arr: np.ndarray, decimals: int = 6) -> list:
    return [round(float(v), decimals) for v in arr]


def _empty_result() -> Dict[str, Any]:
    return {
        "composite_scores": [],
        "quality": [],
        "normal_segments": [],
        "abnormal_segments": [],
        "score_threshold": 0.0,
        "details": {},
    }


# =============================================================================
# SECTION 2 — Robust scale-agnostic scorer
# =============================================================================

class FileQualityRegime(str, Enum):
    """Noise regime detected for a file, determines the classification strategy.

    MOSTLY_GOOD  — few bad segments in an otherwise good file.
                   Strategy: MAD lower-tail removal on IQR-normalised consensus.

    BIMODAL      — clear two populations (good cluster + bad cluster).
                   Strategy: GMM-2 on IQR-normalised consensus.

    HEAVY_NOISE  — majority of segments are noisy or no real structure exists.
                   Strategy: top-fraction on rank consensus, flag the file.
    """
    MOSTLY_GOOD = "mostly_good"
    BIMODAL     = "bimodal"
    HEAVY_NOISE = "heavy_noise"


@dataclass
class RobustConfig:
    """Parameters for the robust scale-agnostic SQI scorer.

    The scorer uses TWO normalisation schemes for different purposes:

      Rank normalisation   — converts each metric to [0, 1] percentile ranks.
                             Used for: HEAVY_NOISE detection (low rank-variance =
                             no structure) and output composite_scores.

      IQR normalisation    — subtracts median, divides by IQR.  Preserves relative
                             distances between windows.
                             Used for: BIMODAL detection (BIC + cluster ratio) and
                             MAD / GMM classification.

    Regime detection
    ----------------
    min_segments_for_gmm : int
        Minimum number of windows before GMM-based bimodal detection is attempted.
        Files with fewer windows fall back to MOSTLY_GOOD (MAD) classification.

    heavy_noise_var_threshold : float
        Applied to RANK-normalised consensus.  If Var(rank_consensus) < this,
        the metrics are not ranking segments consistently → HEAVY_NOISE.
        Rank-normalised consensus of all-noise files concentrates near 0.5
        (low variance), while good or mixed files have higher variance (~0.08).

    cross_corr_threshold : float
        Minimum mean pairwise Spearman correlation between metric rank arrays.
        Values below this indicate the metrics rank segments inconsistently
        → noise dominates → HEAVY_NOISE.

    bic_delta_threshold : float
        BIC(k=1) − BIC(k=2) must exceed this value on the IQR-normalised
        consensus for BIMODAL to be declared.  IQR normalisation preserves
        cluster distances that rank normalisation destroys, making BIC reliable.

    min_cluster_ratio : float
        min(GMM_weights) / max(GMM_weights) must be ≥ this for BIMODAL.
        Prevents treating a file with 2 bad windows out of 20 (small outlier
        cluster) as bimodal.  With the default 0.25, both clusters must contain
        at least 20 % of windows.

    MOSTLY_GOOD mode (MAD)
    ----------------------
    mad_multiplier : float
        k in  threshold = median(IQR_consensus) − k × MAD(IQR_consensus).
        Segments below threshold → abnormal.  k = 2.0 ≈ 97.7th-percentile cut.

    BIMODAL mode (GMM)
    ------------------
    gmm_max_overlap : float
        Bhattacharyya coefficient upper bound.  If the two fitted GMM components
        overlap more than this, the split is unreliable → fall back to MAD.

    gmm_n_init : int
        Number of GMM random initialisations to reduce local-optima risk.

    HEAVY_NOISE mode
    ----------------
    heavy_noise_keep_fraction : float
        In HEAVY_NOISE mode, keep the top this fraction of windows (by rank
        consensus) as normal (best-of-bad).

    Graceful degradation
    --------------------
    flag_file_min_normal_fraction : float
        Set file_flagged=True if fewer than this fraction of windows are normal.
    """

    # ── regime detection ──────────────────────────────────────────────────────
    min_segments_for_gmm: int      = 6
    heavy_noise_var_threshold: float = 0.02   # applied to RANK consensus
    cross_corr_threshold: float    = 0.25

    # ── bimodal detection (IQR space) ─────────────────────────────────────────
    bic_delta_threshold: float     = 10.0
    min_cluster_ratio: float       = 0.25

    # ── MOSTLY_GOOD mode ──────────────────────────────────────────────────────
    mad_multiplier: float          = 2.0

    # ── BIMODAL mode ──────────────────────────────────────────────────────────
    gmm_max_overlap: float         = 0.30
    gmm_n_init: int                = 10

    # ── HEAVY_NOISE mode ──────────────────────────────────────────────────────
    heavy_noise_keep_fraction: float = 0.30

    # ── graceful degradation ──────────────────────────────────────────────────
    flag_file_min_normal_fraction: float = 0.10


# ── robust helper functions ───────────────────────────────────────────────────

def _iqr_normalize(values: np.ndarray) -> np.ndarray:
    """IQR normalisation: subtract median, divide by IQR.

    Unlike rank normalisation, this preserves relative distances between
    windows — making it suitable for bimodality detection where rank
    normalisation would flatten two equal-sized clusters into a uniform
    distribution.

    Result: median → 0, IQR → 1.  May contain negative values for windows
    below the file median.  Not bounded to [0, 1].
    """
    v = _sanitize(values)
    med = float(np.median(v))
    q75, q25 = float(np.percentile(v, 75)), float(np.percentile(v, 25))
    iqr = q75 - q25
    return (v - med) / (iqr + 1e-12)


def _mean_pairwise_spearman(rank_matrix: np.ndarray) -> float:
    """Mean pairwise Spearman rank correlation across columns of *rank_matrix*.

    Parameters
    ----------
    rank_matrix : ndarray of shape (n_windows, n_metrics)

    Returns
    -------
    float in [−1, 1].  Near 0 → metrics disagree (noise).  Near +1 → agree (structure).

    Returns 1.0 for < 2 metrics, 0.0 for < 3 windows.
    """
    n_windows, n_metrics = rank_matrix.shape
    if n_windows < 3 or n_metrics < 2:
        return 1.0
    total, count = 0.0, 0
    for i in range(n_metrics):
        for j in range(i + 1, n_metrics):
            r, _ = stats.spearmanr(rank_matrix[:, i], rank_matrix[:, j])
            if np.isfinite(r):
                total += r
                count += 1
    return float(total / count) if count > 0 else 0.0


def _bic_bimodal_check(
    iqr_consensus: np.ndarray,
    config: RobustConfig,
) -> Tuple[bool, float, Dict[str, Any]]:
    """Test bimodality using BIC model comparison on IQR-normalised consensus.

    Fits GMM(k=1) and GMM(k=2) to the IQR-normalised consensus scores.
    IQR normalisation is used here (not rank) because it preserves cluster
    distances — rank normalisation of equal-weight bimodal clusters produces
    a uniform distribution that looks like k=1 to BIC.

    Returns
    -------
    (is_bimodal, cluster_ratio, info_dict)
        is_bimodal    : True if BIC strongly prefers k=2 AND clusters are balanced
        cluster_ratio : min(GMM_weights) / max(GMM_weights)  ∈ [0, 1]
        info_dict     : BIC values, means, weights for logging
    """
    info: Dict[str, Any] = {}
    try:
        from sklearn.mixture import GaussianMixture

        x    = iqr_consensus.reshape(-1, 1)
        gmm1 = GaussianMixture(n_components=1, random_state=42).fit(x)
        gmm2 = GaussianMixture(
            n_components=2, random_state=42, n_init=config.gmm_n_init
        ).fit(x)

        bic1 = float(gmm1.bic(x))
        bic2 = float(gmm2.bic(x))
        delta = bic1 - bic2

        weights        = gmm2.weights_.flatten()
        cluster_ratio  = float(min(weights) / max(weights)) if max(weights) > 0 else 0.0

        info["bic_k1"]        = round(bic1, 2)
        info["bic_k2"]        = round(bic2, 2)
        info["bic_delta"]     = round(delta, 2)
        info["cluster_ratio"] = round(cluster_ratio, 4)
        info["gmm2_means"]    = [round(float(m), 4) for m in gmm2.means_.flatten()]
        info["gmm2_weights"]  = [round(float(w), 4) for w in weights]

        is_bimodal = (
            delta >= config.bic_delta_threshold
            and cluster_ratio >= config.min_cluster_ratio
        )
        return is_bimodal, cluster_ratio, info

    except ImportError:
        info["error"] = "sklearn_unavailable"
        return False, 0.0, info
    except Exception as exc:
        info["error"] = str(exc)
        return False, 0.0, info


def _gmm_bhattacharyya(means: np.ndarray, variances: np.ndarray) -> float:
    """Bhattacharyya coefficient between two 1-D Gaussian components.

    Returns a value in [0, 1]:  0 = no overlap,  1 = identical distributions.
    """
    mu1, mu2  = float(means[0]), float(means[1])
    s1sq      = max(float(variances[0]), 1e-12)
    s2sq      = max(float(variances[1]), 1e-12)
    sigma_avg = (s1sq + s2sq) / 2.0
    term_dist  = (mu1 - mu2) ** 2 / (4.0 * sigma_avg)
    term_shape = 0.5 * np.log(sigma_avg / np.sqrt(s1sq * s2sq))
    return float(np.exp(-term_dist - term_shape))


# ── regime detection ──────────────────────────────────────────────────────────

def _detect_quality_regime(
    rank_consensus: np.ndarray,
    iqr_consensus: np.ndarray,
    rank_values: Dict[str, np.ndarray],
    config: RobustConfig,
) -> Tuple[FileQualityRegime, Dict[str, Any]]:
    """Determine the noise regime for this file.

    Two normalisation spaces are used:
      rank_consensus — for HEAVY_NOISE detection (low variance = no structure)
      iqr_consensus  — for BIMODAL detection (preserves inter-cluster distances)

    Decision tree
    -------------
    1. n < min_segments_for_gmm                     → MOSTLY_GOOD  (too few for GMM)
    2. Var(rank_consensus) < heavy_noise_var_threshold
       OR mean_pairwise_spearman < cross_corr_threshold  → HEAVY_NOISE
    3. BIC(k=2) beats BIC(k=1) on iqr_consensus by ≥ bic_delta_threshold
       AND cluster_ratio ≥ min_cluster_ratio             → BIMODAL
    4. else                                              → MOSTLY_GOOD

    Returns
    -------
    (regime, info_dict)
    """
    n    = len(rank_consensus)
    info : Dict[str, Any] = {"n_windows": n}

    # ── cross-metric Spearman correlation (rank-space, invariant to normalisation)
    if len(rank_values) > 1:
        rank_matrix = np.stack(list(rank_values.values()), axis=1)
        cross_corr  = _mean_pairwise_spearman(rank_matrix)
    else:
        cross_corr = 1.0
    info["cross_metric_correlation"] = round(float(cross_corr), 4)

    # ── rank-consensus variance (HEAVY_NOISE signal) ──────────────────────────
    rank_var = float(np.var(rank_consensus))
    info["rank_consensus_variance"] = round(rank_var, 6)

    # ── IQR-consensus stats (for information) ────────────────────────────────
    info["iqr_consensus_median"] = round(float(np.median(iqr_consensus)), 4)
    info["skewness"]             = round(float(stats.skew(iqr_consensus)) if n >= 3 else 0.0, 4)

    # ── decision tree ─────────────────────────────────────────────────────────
    if n < config.min_segments_for_gmm:
        regime = FileQualityRegime.MOSTLY_GOOD
        info["reason"] = (
            f"too_few_segments: n={n} < min_segments_for_gmm={config.min_segments_for_gmm}"
        )

    elif (rank_var < config.heavy_noise_var_threshold
          or cross_corr < config.cross_corr_threshold):
        regime = FileQualityRegime.HEAVY_NOISE
        info["reason"] = (
            f"low_structure: rank_var={rank_var:.4f}"
            f" (thresh={config.heavy_noise_var_threshold}),"
            f" cross_corr={cross_corr:.3f}"
            f" (thresh={config.cross_corr_threshold})"
        )

    else:
        # Confirm structure exists; now test bimodality on IQR-normalised consensus
        is_bimodal, cluster_ratio, bic_info = _bic_bimodal_check(iqr_consensus, config)
        info["bic_check"] = bic_info

        if is_bimodal:
            regime = FileQualityRegime.BIMODAL
            info["reason"] = (
                f"bimodal_detected: BIC_delta={bic_info.get('bic_delta', '?')},"
                f" cluster_ratio={cluster_ratio:.3f}"
            )
        else:
            regime = FileQualityRegime.MOSTLY_GOOD
            info["reason"] = (
                f"mostly_good: unimodal structure,"
                f" cross_corr={cross_corr:.3f},"
                f" rank_var={rank_var:.4f}"
            )

    logger.debug("Regime detected: %s — %s", regime.value, info["reason"])
    return regime, info


# ── regime-specific classifiers ───────────────────────────────────────────────

def _classify_mostly_good(
    iqr_consensus: np.ndarray,
    config: RobustConfig,
) -> Tuple[List[str], float]:
    """MAD-based lower-tail removal for MOSTLY_GOOD files.

    Operates on IQR-normalised consensus.

    Threshold = median(iqr_consensus) − mad_multiplier × MAD(iqr_consensus).
    Segments below the threshold are classified as abnormal.

    Returns (quality_list, threshold_used).
    """
    med       = float(np.median(iqr_consensus))
    mad       = float(np.median(np.abs(iqr_consensus - med)))
    threshold = med - config.mad_multiplier * mad
    quality   = ["normal" if float(s) >= threshold else "abnormal" for s in iqr_consensus]
    return quality, threshold


def _classify_bimodal(
    iqr_consensus: np.ndarray,
    config: RobustConfig,
) -> Tuple[List[str], float, Dict[str, Any]]:
    """GMM-2 classification for BIMODAL files.

    Operates on IQR-normalised consensus scores.  The component with the
    higher mean is labelled as the normal cluster.

    Falls back to _classify_mostly_good() when:
      - sklearn is unavailable
      - GMM fails to converge
      - Bhattacharyya overlap between components ≥ gmm_max_overlap

    Returns (quality_list, threshold_used, gmm_info_dict).
    """
    gmm_info: Dict[str, Any] = {}
    try:
        from sklearn.mixture import GaussianMixture

        gmm = GaussianMixture(
            n_components=2,
            covariance_type="full",
            random_state=42,
            n_init=config.gmm_n_init,
        )
        gmm.fit(iqr_consensus.reshape(-1, 1))

        means     = gmm.means_.flatten()
        variances = gmm.covariances_.reshape(2)   # (2,1,1) → (2,)
        overlap   = _gmm_bhattacharyya(means, variances)

        gmm_info["means"]                 = [round(float(m), 6) for m in means]
        gmm_info["variances"]             = [round(float(v), 6) for v in variances]
        gmm_info["bhattacharyya_overlap"] = round(overlap, 4)
        gmm_info["converged"]             = bool(gmm.converged_)

        if overlap >= config.gmm_max_overlap:
            logger.debug(
                "GMM overlap %.3f >= %.3f — falling back to MAD",
                overlap, config.gmm_max_overlap,
            )
            gmm_info["fallback"] = f"high_overlap ({overlap:.3f}) → MAD"
            quality, threshold = _classify_mostly_good(iqr_consensus, config)
            return quality, threshold, gmm_info

        labels       = gmm.predict(iqr_consensus.reshape(-1, 1))
        normal_label = int(np.argmax(means))
        quality      = ["normal" if int(l) == normal_label else "abnormal" for l in labels]
        normal_scores = [float(iqr_consensus[i]) for i, q in enumerate(quality) if q == "normal"]
        threshold     = float(min(normal_scores)) if normal_scores else 0.0

        gmm_info["normal_component"] = normal_label
        return quality, threshold, gmm_info

    except ImportError:
        logger.warning("sklearn not available — falling back to MAD for BIMODAL regime")
        gmm_info["fallback"] = "no_sklearn → MAD"
        quality, threshold = _classify_mostly_good(iqr_consensus, config)
        return quality, threshold, gmm_info

    except Exception as exc:
        logger.warning("GMM failed (%s) — falling back to MAD", exc)
        gmm_info["fallback"] = f"gmm_error → MAD: {exc}"
        quality, threshold = _classify_mostly_good(iqr_consensus, config)
        return quality, threshold, gmm_info


def _classify_heavy_noise(
    rank_consensus: np.ndarray,
    config: RobustConfig,
) -> Tuple[List[str], float]:
    """Top-fraction classification for HEAVY_NOISE files.

    Operates on RANK-normalised consensus (already in [0, 1]).
    Keeps the top heavy_noise_keep_fraction of windows as normal (best-of-bad).
    Returns (quality_list, threshold_used).
    """
    threshold = float(
        np.percentile(rank_consensus, 100.0 * (1.0 - config.heavy_noise_keep_fraction))
    )
    quality = ["normal" if float(s) >= threshold else "abnormal" for s in rank_consensus]
    return quality, threshold


# ── main public function ──────────────────────────────────────────────────────

def robust_score_windows(
    sqi_values: Dict[str, np.ndarray],
    signal: np.ndarray,
    window: int,
    step: int,
    config: RobustConfig,
) -> Dict[str, Any]:
    """Robust scale-agnostic SQI scorer.

    Uses two normalisation schemes:
      - Rank normalisation  → HEAVY_NOISE detection + output composite_scores [0,1]
      - IQR normalisation   → BIMODAL detection (BIC) + MAD / GMM classification

    Algorithm
    ---------
    1. Rank-normalise each metric → rank_values  (kills unit differences)
    2. IQR-normalise each metric  → iqr_values   (preserves cluster distances)
    3. Rank consensus  = mean of rank_values     (output score, [0,1])
    4. IQR  consensus  = median of iqr_values    (classification score)
    5. Cross-metric Spearman on rank_values      (structure test)
    6. Regime detection  (HEAVY_NOISE / BIMODAL / MOSTLY_GOOD)
    7. Classify by regime (top-fraction / GMM / MAD)
    8. Graceful degradation: set file_flagged if < min_normal_fraction are normal

    Parameters
    ----------
    sqi_values : dict  metric_name → 1-D array of raw per-window SQI values
    signal     : ndarray  raw signal — used only to derive n_windows
    window     : int  window length in samples
    step       : int  step size in samples
    config     : RobustConfig

    Returns
    -------
    dict — see key descriptions in the Returns section of the API reference.
    """
    n_windows = max(0, (len(signal) - window) // step + 1)
    if n_windows == 0:
        return _empty_robust_result()

    # ── 1. filter to valid metrics ────────────────────────────────────────────
    metrics = [
        m for m in sqi_values
        if len(sqi_values[m]) == n_windows and np.any(np.isfinite(sqi_values[m]))
    ]
    if not metrics:
        return _empty_robust_result()

    # ── 2. rank normalisation (unit-free, [0,1]) ──────────────────────────────
    rank_values: Dict[str, np.ndarray] = {
        m: _quantile_ranks(np.asarray(sqi_values[m], dtype=float))
        for m in metrics
    }

    # ── 3. IQR normalisation (structure-preserving) ───────────────────────────
    iqr_values: Dict[str, np.ndarray] = {
        m: _iqr_normalize(np.asarray(sqi_values[m], dtype=float))
        for m in metrics
    }

    # ── 4. consensus scores ───────────────────────────────────────────────────
    rank_stacked   = np.stack(list(rank_values.values()), axis=0)   # (m, n)
    rank_consensus = np.nanmean(rank_stacked, axis=0)               # [0,1]
    rank_consensus = np.where(np.isfinite(rank_consensus), rank_consensus, 0.5)

    iqr_stacked    = np.stack(list(iqr_values.values()), axis=0)    # (m, n)
    iqr_consensus  = np.nanmedian(iqr_stacked, axis=0)              # robust median
    iqr_consensus  = np.where(np.isfinite(iqr_consensus), iqr_consensus, 0.0)

    # ── 5. regime detection ───────────────────────────────────────────────────
    regime, regime_info = _detect_quality_regime(
        rank_consensus, iqr_consensus, rank_values, config
    )

    # ── 6. classification by regime ───────────────────────────────────────────
    gmm_details: Dict[str, Any] = {}

    if regime == FileQualityRegime.MOSTLY_GOOD:
        quality, score_threshold = _classify_mostly_good(iqr_consensus, config)

    elif regime == FileQualityRegime.BIMODAL:
        quality, score_threshold, gmm_details = _classify_bimodal(iqr_consensus, config)

    else:  # HEAVY_NOISE — use rank_consensus (already in [0,1])
        quality, score_threshold = _classify_heavy_noise(rank_consensus, config)

    # ── 7. graceful degradation ───────────────────────────────────────────────
    normal_count    = sum(1 for q in quality if q == "normal")
    normal_fraction = normal_count / len(quality) if quality else 0.0
    file_flagged    = normal_fraction < config.flag_file_min_normal_fraction

    if file_flagged:
        logger.warning(
            "File flagged: only %.1f%% of windows are normal "
            "(threshold: %.1f%%, regime: %s)",
            normal_fraction * 100,
            config.flag_file_min_normal_fraction * 100,
            regime.value,
        )

    # ── 8. build segment lists ────────────────────────────────────────────────
    normal_segs: List[Tuple[int, int]]   = []
    abnormal_segs: List[Tuple[int, int]] = []
    for i, q in enumerate(quality):
        start = i * step
        end   = start + window
        (normal_segs if q == "normal" else abnormal_segs).append(
            (int(start), int(end))
        )

    # ── 9. assemble result ────────────────────────────────────────────────────
    # composite_scores is always rank_consensus (bounded [0,1], easy to compare)
    details: Dict[str, Any] = {
        m: {
            "rank": _round_list(rank_values[m]),
            "iqr":  _round_list(iqr_values[m]),
        }
        for m in metrics
    }
    if gmm_details:
        details["gmm"] = gmm_details

    return {
        "composite_scores":  _round_list(rank_consensus),
        "quality":           quality,
        "normal_segments":   normal_segs,
        "abnormal_segments": abnormal_segs,
        "score_threshold":   round(float(score_threshold), 6),
        "regime":            regime.value,
        "file_flagged":      file_flagged,
        "normal_fraction":   round(normal_fraction, 4),
        "regime_info":       regime_info,
        "details":           details,
    }


def _empty_robust_result() -> Dict[str, Any]:
    return {
        "composite_scores":  [],
        "quality":           [],
        "normal_segments":   [],
        "abnormal_segments": [],
        "score_threshold":   0.0,
        "regime":            FileQualityRegime.MOSTLY_GOOD.value,
        "file_flagged":      False,
        "normal_fraction":   0.0,
        "regime_info":       {},
        "details":           {},
    }
