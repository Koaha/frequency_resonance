# Robust Scale-Agnostic SQI Scorer — Design Document

## 1. Problem statement

The original composite SQI scorer (`score_windows()`) worked well for files with
mostly good signal quality, but failed in two important scenarios:

### 1.1 Unit / scale vulnerability

Each SQI metric produced by vitalDSP lives on a different numerical scale:
- `snr_sqi` returns values in decibels (can be −10 to +60 dB)
- `kurtosis_sqi` returns raw statistical kurtosis (can be 1 to hundreds)
- `signal_entropy_sqi` returns Shannon entropy (typically 0–8 bits)
- `energy_sqi` returns signal energy (arbitrary units)

The legacy scorer applied a hard absolute bound (`abs_max_sqi: 10.0`) and
normalised values using intra-file statistics, but the fixed bound was wrong
for metrics like SNR that legitimately exceed 10.

Any change to vitalDSP's internal normalisation, or switching from PPG to ECG,
could silently break the classification without any error.

### 1.2 Majority-noise failure

The legacy scorer used relative statistics (quantile rank, modified z-score,
tail probability) computed within each file.  When the majority of segments in
a file are noisy:

- The "good" reference distribution no longer exists
- The noisy segments become the reference
- Previously bad segments are now classified as normal

The legacy `abs_max_sqi` safeguard only helped with obviously degenerate files
where every single window had an extreme value.

---

## 2. Core insight — dual normalisation

Instead of working with raw SQI values (unit-dependent), the robust scorer uses
**two complementary normalisation schemes** for different parts of the algorithm:

### 2.1 Rank normalisation (unit-free, [0, 1])

For each metric independently:
```
rank_m[i] = (rank_of(sqi_m[i]) - 1) / (N - 1)
```
Result: `rank_m ∈ [0, 1]^N`.  Transforms any distribution to a near-uniform
distribution over [0, 1].

**Used for:** HEAVY_NOISE detection (variance of rank consensus ≈ 0 when all
windows are equally "bad" or "good") and output `composite_scores` (always [0, 1]).

**Why rank, not z-score:** Rank normalisation is fully non-parametric and makes
no assumptions about the underlying distribution.  Z-score normalisation assumes
approximate normality and is sensitive to outliers.

### 2.2 IQR normalisation (structure-preserving)

```
iqr_m[i] = (sqi_m[i] - median(sqi_m)) / IQR(sqi_m)
```
Result: median → 0, IQR → 1.  Values can be negative (below-median windows).
Preserves the relative distances between windows.

**Used for:** BIMODAL detection and MAD / GMM classification, because bimodal
structure is destroyed by rank normalisation for equal-weight clusters.

> **Key insight:** Rank normalisation of two equal-sized clusters (e.g. 10 good
> + 10 bad windows) produces a uniform distribution over [0, 1] — exactly what
> a unimodal distribution looks like to a BIC test.  IQR normalisation preserves
> the two-cluster gap while still eliminating unit/scale differences.

---

## 3. Algorithm — eight steps

### Step 1: Rank normalisation

For each SQI metric `m` independently:
```
rank_m[i] = (rank_of(sqi_m[i]) - 1) / (N - 1)
```
NaN/Inf values are replaced by the finite median before ranking (via `_sanitize()`).

### Step 2: IQR normalisation

For each SQI metric `m` independently:
```
iqr_m[i] = (sqi_m[i] - median(sqi_m)) / (IQR(sqi_m) + ε)
```
where ε = 1e-12 prevents division by zero for constant metrics.

### Step 3: Consensus scores

```
rank_consensus[i] = mean(rank_m[i]  for all metrics m)   # output score, [0,1]
iqr_consensus[i]  = median(iqr_m[i] for all metrics m)   # classification score
```

Rank consensus is the primary output quality score (bounded, easy to compare).
IQR consensus drives classification (structure-preserving).

### Step 4: Cross-metric Spearman correlation

```
cross_corr = mean(Spearman(rank_m_i, rank_m_j)  for all metric pairs i < j)
```

This is the key statistic for detecting whether rank normalisation is meaningful.
Values near 0 indicate the metrics are ranking segments inconsistently (noise
dominates).  Values near +1 indicate strong agreement (real signal structure).

### Step 5: Regime detection

Using statistics from rank consensus and IQR consensus:

**Decision tree:**

```
if N < min_segments_for_gmm:
    → MOSTLY_GOOD       (too few windows for reliable GMM)

elif Var(rank_consensus) < heavy_noise_var_threshold
  OR cross_corr < cross_corr_threshold:
    → HEAVY_NOISE       (no real quality structure)

elif BIC_delta ≥ bic_delta_threshold
  AND cluster_ratio ≥ min_cluster_ratio
  (both tested on IQR-normalised consensus):
    → BIMODAL           (two distinct populations)

else:
    → MOSTLY_GOOD       (structure confirmed, unimodal → MAD handles outliers)
```

**Why HEAVY_NOISE uses rank variance (not IQR variance):**
In a pure-noise file, each metric assigns random ranks, so the mean rank
across metrics concentrates near 0.5 (low rank variance ≈ 0.008–0.02).
In a good-quality file, windows rank consistently high or low, spreading the
rank consensus across [0, 1] (variance ≈ 0.08–0.12).

**Why BIMODAL uses IQR-normalised consensus:**
Rank normalisation maps two equal-weight bimodal clusters to a near-uniform
distribution.  IQR normalisation preserves the gap between the two clusters,
making BIC model comparison reliable.

**Why Sarle's BC was abandoned:**
Sarle's Bimodality Coefficient on rank-normalised data reliably returns values
below the 0.555 threshold even for strongly bimodal distributions, because rank
normalisation of equal-weight bimodal clusters produces a uniform-like distribution.
Testing confirmed BIC comparison on IQR-normalised data correctly identifies
bimodal structure (BIC_delta ≈ 15 for n=20, ≈ 22 for n=30).

**Why the final else is MOSTLY_GOOD:**
By the time we reach the else branch, we have confirmed:
- `Var(rank_consensus) ≥ heavy_noise_var_threshold`  (sufficient structure)
- `cross_corr ≥ cross_corr_threshold`                (metrics agree)
- BIC does not strongly prefer k=2                   (unimodal)

This is consistent with a mostly-good file with a few bad outlier windows.

#### BIC bimodal check (Step 5.1)

Two GMMs are fitted to the IQR-normalised consensus:
- `GMM(k=1)`: single-component model
- `GMM(k=2)`: two-component model

BIC difference:
```
BIC_delta = BIC(k=1) - BIC(k=2)
```
Higher BIC_delta → stronger evidence for two components.

Cluster balance check:
```
cluster_ratio = min(GMM_weights) / max(GMM_weights)
```
If cluster_ratio < min_cluster_ratio, the smaller cluster contains only a few
outlier windows and the file is not truly bimodal → falls back to MOSTLY_GOOD.

### Step 6: Classify by regime

#### MOSTLY_GOOD → MAD threshold (on IQR consensus)

```
threshold = median(iqr_consensus) − k × MAD(iqr_consensus)
abnormal  ↔  iqr_consensus[i] < threshold
```
where `k = mad_multiplier` (default 2.0).

#### BIMODAL → GMM-2 (on IQR consensus)

A two-component Gaussian Mixture Model is fitted to IQR-normalised consensus scores.
The component with the higher mean is labelled as the normal cluster.

Before accepting the GMM split, the **Bhattacharyya coefficient** between the
two components is checked:
```
BC = exp(−(μ₁−μ₂)²/(4σ²_avg) − ½ ln(σ²_avg / √(σ₁²·σ₂²)))
```
If `BC ≥ gmm_max_overlap`, components overlap too much → fall back to MAD.

#### HEAVY_NOISE → top-fraction (on rank consensus)

```
threshold = percentile(rank_consensus, 100 × (1 − heavy_noise_keep_fraction))
abnormal  ↔  rank_consensus[i] < threshold
```
Rank consensus is used here (not IQR) because rank values are bounded [0, 1],
making the percentile threshold directly interpretable.

### Step 7: Graceful degradation

```
normal_fraction = count("normal") / N
file_flagged    = (normal_fraction < flag_file_min_normal_fraction)
```

If `file_flagged` is True, the downstream pipeline should treat the result as
low-confidence.

### Step 8: Output

```python
{
    "composite_scores":  [...],   # rank_consensus, [0,1] per window
    "quality":           [...],   # "normal" | "abnormal" per window
    "normal_segments":   [...],   # (start, end) sample indices
    "abnormal_segments": [...],
    "score_threshold":   float,   # threshold applied in classification
    "regime":            str,     # "mostly_good" | "bimodal" | "heavy_noise"
    "file_flagged":      bool,
    "normal_fraction":   float,
    "regime_info":       dict,    # diagnostics: variance, cross_corr, BIC, etc.
    "details":           dict,    # per-metric rank[] and iqr[] arrays
}
```

---

## 4. Regime characterisation — expected distributions

| Scenario | cross_corr | Var(rank_consensus) | BIC_delta (IQR) | Regime |
|---|---|---|---|---|
| Mostly clean, few noisy windows | High (> 0.5) | Medium (0.06–0.12) | Low (< 5) | MOSTLY_GOOD |
| Clean and noisy in ~equal proportions | High (> 0.3) | High (> 0.08) | High (> 10) + ratio ≥ 0.25 | BIMODAL |
| Mostly noisy, few clean windows | Medium | High | High (> 10) + low ratio → | MOSTLY_GOOD or BIMODAL |
| Entirely noisy (no structure) | Low (< 0.2) | Low (< 0.02) | Not checked | HEAVY_NOISE |
| Very short file (N < 6) | N/A | N/A | N/A | MOSTLY_GOOD (fallback) |

---

## 5. Worked example

**File A — 20 windows, 18 good + 2 noisy:**

- Rank consensus: 18 windows cluster near 0.75–0.95, 2 windows near 0.10–0.25.
- cross_corr ≈ 0.92 (metrics agree)
- Var(rank_consensus) ≈ 0.086 (> 0.02 threshold)
- BIC_delta < 10 (only 2 bad windows = small outlier cluster, not truly bimodal)
- **Regime: MOSTLY_GOOD**
- threshold = median(IQR_consensus) − 2 × MAD(IQR_consensus)
- Result: 18 normal + 2 abnormal ✓

**File B — 20 windows, 10 good + 10 noisy:**

- Two clear clusters in IQR consensus.
- cross_corr ≈ 0.75
- Var(rank_consensus) ≈ 0.09
- BIC_delta ≈ 15 (> 10), cluster_ratio ≈ 1.0 (equal-weight clusters)
- **Regime: BIMODAL**
- GMM finds means ≈ −0.5 and +0.7 (IQR space), Bhattacharyya ≈ 0.05 (well-separated)
- Result: 10 normal + 10 abnormal ✓

**File C — 20 windows, all noise:**

- Each metric independently assigns ranks 0–1 to the random noise patterns.
- cross_corr ≈ 0.13 (< 0.25 threshold) — metrics disagree
- Var(rank_consensus) ≈ 0.028
- **Regime: HEAVY_NOISE** (triggered by low cross_corr)
- threshold = 70th percentile of rank_consensus, keep top 30 % (6 windows)
- file_flagged = False (30% > 10% min threshold — best-of-bad windows returned)
- Result: 6 "best-of-bad" normal + 14 abnormal ✓

---

## 6. Edge cases and mitigations

| Edge case | Detection | Mitigation |
|---|---|---|
| N = 0 (empty file) | n_windows == 0 check | Return empty result |
| N = 1–5 (very short) | n < min_segments_for_gmm | Fall back to MOSTLY_GOOD/MAD |
| All SQI values identical | cross_corr=1, rank_var≈0 | HEAVY_NOISE (low rank_var) |
| 2 bad windows in 20 | cluster_ratio < min_cluster_ratio | Stays MOSTLY_GOOD (not BIMODAL) |
| Single metric available | n_metrics == 1 | cross_corr forced to 1.0; proceed normally |
| sklearn not installed (no GMM) | ImportError catch | Fall back to MAD in BIMODAL regime |
| GMM fails to converge | Exception catch | Fall back to MAD in BIMODAL regime |
| GMM components too close | Bhattacharyya ≥ gmm_max_overlap | Fall back to MAD |
| NaN/Inf in raw SQI | `_sanitize()` before ranking | Replaced with finite median |

---

## 7. Known limitations

1. **Cannot distinguish "all good" from "all bad" using ranks alone.**
   The cross-metric correlation provides partial discrimination (all-bad → low
   correlation), but a pathological case where all metrics are perfectly
   correlated AND all windows are bad would fool the detector.  In practice this
   is rare because different SQI metrics measure truly independent properties.

2. **IQR normalisation is sensitive to very short files.**
   With N = 6–10 windows, the IQR estimate is noisy.  BIC model comparison on
   noisy data may produce unstable results near the bic_delta_threshold.

3. **GMM assumes Gaussian components.**
   Real good/bad quality distributions may not be Gaussian.  The Bhattacharyya
   fallback to MAD provides a safety net.

4. **heavy_noise_keep_fraction is a heuristic.**
   In HEAVY_NOISE mode, the top 30 % of windows are kept regardless of whether
   they are actually usable.  There is no absolute quality guarantee.  The
   `file_flagged` output exists to propagate this uncertainty, but `file_flagged`
   will be False if ≥ 10 % of windows pass — downstream consumers should check
   the `regime` field, not only `file_flagged`.

5. **cross_corr_threshold is sensitive to the number of metrics.**
   With many metrics, the expected mean pairwise correlation under the null
   (independent noise) converges to 0 by the law of large numbers.  With few
   metrics (2–3), sampling variance is high.  Tune `cross_corr_threshold`
   downward to ~0.15 if you use fewer than 5 metrics.

---

## 8. Design decisions and trade-offs

### Why rank normalisation instead of z-score normalisation?

Z-score normalisation (`(x − mean) / std`) still assumes the data is roughly
normally distributed.  It is sensitive to outliers.  Rank normalisation makes
no distributional assumption and is fully non-parametric.

### Why IQR normalisation for bimodal detection?

Rank normalisation of two equal-weight clusters (50% good, 50% bad) maps both
clusters to a uniform distribution over [0, 1].  The BIC test then sees a single
flat distribution and (correctly, given the transformed data) prefers k=1.

IQR normalisation (`(x − median) / IQR`) preserves the distance between the
two cluster centres while removing the original scale.  The good cluster maps
to positive IQR-scores, the bad cluster to negative IQR-scores, and the BIC
test correctly identifies k=2.

### Why BIC model comparison instead of Sarle's Bimodality Coefficient?

Sarle's BC was tested on rank-normalised data and consistently returned values
below the 0.555 threshold even for strongly bimodal signals.  Root cause: rank
normalisation of equal-weight bimodal clusters produces a near-uniform
distribution that Sarle's BC rates as unimodal.

BIC comparison on IQR-normalised data correctly identifies bimodality:
BIC_delta ≈ 15 for n=20, ≈ 22 for n=30 in synthetic tests.

### Why consensus score (mean rank) instead of PCA?

PCA requires N > m (more windows than metrics); not guaranteed for short files.
PCA components are not interpretable as "quality".  Mean rank is simple,
interpretable, and requires only N ≥ 2.

### Why MAD instead of standard deviation for the MOSTLY_GOOD threshold?

The standard deviation is strongly influenced by the few bad segments.  MAD
(median absolute deviation) is robust to up to 50 % outliers and gives a
threshold that reflects the spread of the good-quality cluster.

### Why min_cluster_ratio in bimodal detection?

Without this check, a file with 2 bad windows out of 20 could satisfy the
BIC_delta threshold (since even a small outlier cluster improves GMM fit).
The cluster_ratio check (≥ 0.25 by default) ensures both clusters contain at
least ~20 % of windows — consistent with a genuinely mixed-quality file.
