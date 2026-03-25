# src/core/signal_processing/sqi_scorer.py
"""Composite statistical SQI scorer.

Combines multiple statistical features of per-window SQI values into a single
quality score per window, replacing the legacy single-value threshold approach.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

import logging
import numpy as np
from scipy import stats

logger = logging.getLogger(__name__)


@dataclass
class CompositeConfig:
    """Parameters for composite statistical thresholding."""
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


# ── helpers ──────────────────────────────────────────────────────────────────

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


# ── per-window feature functions ─────────────────────────────────────────────

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


# ── composite scorer ─────────────────────────────────────────────────────────

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
