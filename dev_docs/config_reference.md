# Configuration Reference — `robust_composite` Block

This document describes every key in the `robust_composite:` section of
`config.yaml`.  These parameters control the `robust_score_windows()` function
via the `RobustConfig` dataclass.

The scorer uses **two normalisation schemes**:

- **Rank normalisation** — each metric mapped to [0, 1].  Used for HEAVY_NOISE
  detection and output `composite_scores`.
- **IQR normalisation** — subtract median, divide by IQR.  Preserves inter-cluster
  distances.  Used for BIMODAL detection (BIC) and MAD / GMM classification.

All parameters operate on these normalised scores, independent of raw SQI units,
scale, or vitalDSP version.

---

## How to activate

Set `threshold_method: robust_composite` in `config.yaml`.

```yaml
threshold_method: robust_composite
```

The `robust_composite:` block supplies the tuning parameters.  All keys are
optional — omitting a key uses the hardcoded default in `RobustConfig`.

---

## Regime detection parameters

These parameters determine which noise regime is assigned to the file.
The regime selects the classification strategy.

---

### `min_segments_for_gmm`

| | |
|---|---|
| **Type** | `int` |
| **Default** | `6` |
| **Valid range** | ≥ 2 |

Minimum number of windows (segments) before GMM-based bimodal detection is
attempted.  Files with fewer windows are automatically assigned the `MOSTLY_GOOD`
regime and classified using MAD.

**Why:** GMM with N < 6 data points is statistically unreliable.

**When to change:**

- Decrease to 4 if your files are routinely very short.
- Increase to 8–10 if you want more statistical power before trusting GMM.

---

### `heavy_noise_var_threshold`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `0.02` |
| **Valid range** | > 0.0 |

Applied to **rank-normalised** consensus.  If `Var(rank_consensus) < this`,
the file has no real quality structure → `HEAVY_NOISE`.

**Physical meaning:**
In a pure-noise file, rank consensus concentrates near 0.5 (variance ≈ 0.008).
In a good-quality or mixed file, rank consensus is spread across [0, 1]
(variance ≈ 0.06–0.12).  A value below 0.02 means the file lacks structure.

**When to change:**

- Decrease (e.g. 0.01) to tolerate lower variance — fewer files flagged as heavy noise.
- Increase (e.g. 0.04) to be stricter — more files assigned HEAVY_NOISE.

Note: this threshold is checked alongside `cross_corr_threshold`.
Either condition triggers HEAVY_NOISE.

---

### `cross_corr_threshold`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `0.25` |
| **Valid range** | [−1.0, 1.0] (practical range: 0.1–0.5) |

Minimum mean pairwise Spearman correlation across all SQI metric rank arrays.
Below this threshold, metrics rank segments inconsistently → noise dominates →
`HEAVY_NOISE`.

**Physical meaning:**
In a good-quality file, all metrics rank the same windows highly (coherent signal
→ high Spearman).  In a noise-dominated file, each metric ranks windows by
different random properties → Spearman near 0.

**When to change:**

- Decrease (e.g. 0.15) to tolerate more inter-metric disagreement.
- Increase (e.g. 0.35) to require stronger agreement before trusting rank scores.
- With only 2–3 metrics, sampling variance is high; consider decreasing to 0.15.

---

## BIMODAL detection parameters (IQR space)

Bimodal detection uses **IQR-normalised** consensus (not rank-normalised), because
rank normalisation of two equal-weight clusters produces a uniform-like distribution
that BIC cannot distinguish from a single component.

---

### `bic_delta_threshold`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `10.0` |
| **Valid range** | > 0.0 |

`BIC(k=1) − BIC(k=2)` on IQR-normalised consensus must exceed this for BIMODAL
to be declared.  Higher delta = stronger evidence that two Gaussian components fit
better than one.

**Empirical calibration:**

| Scenario | Typical BIC_delta |
|---|---|
| 18 good + 2 bad (MOSTLY_GOOD) | < 5 |
| 10 good + 10 bad (BIMODAL) | 12–18 (n=20), 20–25 (n=30) |
| All noise (HEAVY_NOISE) | Not checked (caught earlier) |

**When to change:**

- Decrease (e.g. 5.0) to detect bimodality more aggressively — more files as BIMODAL.
- Increase (e.g. 20.0) to require stronger evidence — fewer files as BIMODAL.

---

### `min_cluster_ratio`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `0.25` |
| **Valid range** | (0.0, 1.0] |

`min(GMM_weights) / max(GMM_weights)` for the GMM-2 fit on IQR consensus.
If this ratio is below the threshold, the smaller cluster contains only a few
outlier windows and the file is not genuinely bimodal → falls back to MOSTLY_GOOD.

**Example:**

- 10 good + 10 bad: weights ≈ [0.5, 0.5], ratio = 1.0 → passes
- 18 good + 2 bad: weights ≈ [0.9, 0.1], ratio = 0.11 → fails → MOSTLY_GOOD
- 16 good + 4 bad: weights ≈ [0.8, 0.2], ratio = 0.25 → boundary (passes with default)

**When to change:**

- Decrease (e.g. 0.15) to allow more imbalanced splits to be treated as BIMODAL.
- Increase (e.g. 0.35) to require more balanced clusters before declaring BIMODAL.

---

## MOSTLY_GOOD mode parameter

### `mad_multiplier`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `2.0` |
| **Valid range** | > 0.0 (practical range: 1.5–3.0) |

`k` in the MAD threshold formula on IQR-normalised consensus:

```
threshold = median(iqr_consensus) − k × MAD(iqr_consensus)
```

Windows with `iqr_consensus < threshold` are classified as abnormal.

**Sensitivity:**

| k | Approx. % windows kept (normal dist.) | Behaviour |
|---|---|---|
| 1.0 | ~86 % | Aggressive rejection |
| 1.5 | ~93 % | Moderate |
| 2.0 | ~97 % | Default — conservative |
| 2.5 | ~99 % | Very conservative |
| 3.0 | ~99.7 % | Almost nothing rejected |

**When to change:**

- Decrease to 1.5 if data frequently has 10–20 % bad windows.
- Increase to 2.5–3.0 to keep as many windows as possible.

---

## BIMODAL mode parameters

### `gmm_max_overlap`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `0.30` |
| **Valid range** | (0.0, 1.0) |

Bhattacharyya coefficient ceiling for the two GMM components.  If the overlap
between the two fitted Gaussians exceeds this, the bimodal split is unreliable →
fall back to MAD classification.

BC = 0 means no overlap (perfectly separated).  BC = 1 means identical distributions.

**When to change:**

- Decrease (e.g. 0.15) to require better cluster separation before trusting GMM.
- Increase (e.g. 0.45) to accept noisier GMM fits.

---

### `gmm_n_init`

| | |
|---|---|
| **Type** | `int` |
| **Default** | `10` |
| **Valid range** | ≥ 1 |

Number of random initialisations for `GaussianMixture`.  Higher values reduce
the risk of converging to a poor local optimum.

**When to change:**

- Decrease to 1–3 if speed is critical and files have many windows (> 100).
- Increase to 20–50 for very small N (6–10 windows).

---

## HEAVY_NOISE mode parameter

### `heavy_noise_keep_fraction`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `0.30` |
| **Valid range** | (0.0, 1.0] |

In HEAVY_NOISE mode, the top `heavy_noise_keep_fraction` of windows by **rank**
consensus score are classified as normal (best-of-bad).

```
threshold = percentile(rank_consensus, 100 × (1 − keep_fraction))
```

E.g. `0.30` → threshold = 70th percentile → top 30 % kept.

**Important:** these "normal" windows are not guaranteed to be good quality.
Check the `regime` field in the output (`"heavy_noise"`) to know when this mode
was applied.

**When to change:**

- Decrease (e.g. 0.10) to only keep the very best windows of a bad file.
- Increase (e.g. 0.50) if you need more windows and accept lower quality.

---

## Graceful degradation parameter

### `flag_file_min_normal_fraction`

| | |
|---|---|
| **Type** | `float` |
| **Default** | `0.10` |
| **Valid range** | (0.0, 1.0) |

If the fraction of windows classified as normal (after all classification) is
below this threshold, `file_flagged = True` is set in the result.

This does not change which windows are classified — it is a post-hoc signal to
downstream consumers: "very few normal windows were found, treat with caution."

**When to change:**

- Decrease to 0.05 if files with only 5 % good windows are acceptable.
- Increase to 0.20–0.30 to flag files more aggressively for review.

---

## Full example block

```yaml
threshold_method: robust_composite

robust_composite:
  # ── Regime detection ──────────────────────────────────────────────────────
  min_segments_for_gmm: 6
  heavy_noise_var_threshold: 0.02
  cross_corr_threshold: 0.25

  # ── BIMODAL detection (IQR space) ─────────────────────────────────────────
  bic_delta_threshold: 10.0
  min_cluster_ratio: 0.25

  # ── MOSTLY_GOOD mode (MAD threshold) ──────────────────────────────────────
  mad_multiplier: 2.0

  # ── BIMODAL mode (GMM-2) ──────────────────────────────────────────────────
  gmm_max_overlap: 0.30
  gmm_n_init: 10

  # ── HEAVY_NOISE mode (best-of-bad) ────────────────────────────────────────
  heavy_noise_keep_fraction: 0.30

  # ── Graceful degradation ──────────────────────────────────────────────────
  flag_file_min_normal_fraction: 0.10
```

---

## Interaction between parameters

| Scenario | Recommended change |
|---|---|
| Too many files in HEAVY_NOISE | Decrease `cross_corr_threshold` or `heavy_noise_var_threshold` |
| Too many files in BIMODAL when they should be MOSTLY_GOOD | Increase `bic_delta_threshold` or `min_cluster_ratio` |
| Losing too many good windows | Increase `mad_multiplier` (MOSTLY_GOOD) or `heavy_noise_keep_fraction` |
| GMM splitting wrong | Decrease `gmm_max_overlap` (force more fallback to MAD) |
| Too many files flagged | Decrease `flag_file_min_normal_fraction` |
| Too few files flagged | Increase `flag_file_min_normal_fraction` |

---

## Legacy parameters (still supported)

The `composite:` block still works when `threshold_method: composite`.  Setting
`threshold_method: robust_composite` makes the `composite:` block unused (but
harmless to keep).

The `sqi:` per-metric block controls which metrics are **computed** — both the
legacy and robust scorers use only the metrics listed as `enabled: true`.
The `threshold` and `threshold_type` fields in `sqi:` are only used in `"value"`
mode; both composite scorers ignore them.
