# API Reference — Robust SQI Scorer

All symbols live in `src/core/signal_processing/sqi_scorer.py` and are
re-exported from `src/core/signal_processing/__init__.py`.

---

## `FileQualityRegime`

```python
class FileQualityRegime(str, Enum):
    MOSTLY_GOOD = "mostly_good"
    BIMODAL     = "bimodal"
    HEAVY_NOISE = "heavy_noise"
```

Enum that identifies the noise regime detected for a file.  Used internally
by `robust_score_windows()` to select the classification strategy.  Also
emitted as the `"regime"` string in the result dict so callers can inspect
or log it without importing the enum.

| Value | Meaning | Strategy used |
|---|---|---|
| `"mostly_good"` | Few bad segments in an otherwise clean file | MAD lower-tail removal |
| `"bimodal"` | Two distinct quality populations | GMM-2 component separation |
| `"heavy_noise"` | Majority noisy or no structure | Consensus vote, keep top fraction |

---

## `RobustConfig`

```python
@dataclass
class RobustConfig:
    min_segments_for_gmm: int = 6
    bimodality_coeff_threshold: float = 0.555
    heavy_noise_var_threshold: float = 0.02
    cross_corr_threshold: float = 0.25
    mad_multiplier: float = 2.0
    gmm_max_overlap: float = 0.30
    gmm_n_init: int = 10
    heavy_noise_keep_fraction: float = 0.30
    flag_file_min_normal_fraction: float = 0.10
```

Configuration dataclass for the robust scorer.  All thresholds operate on
rank-normalised consensus scores (unit-free).  See [config_reference.md](config_reference.md)
for per-field documentation.

Constructed automatically from the `robust_composite:` block in `config.yaml`
by `SignalConfig.from_yaml()`.  Can also be instantiated directly:

```python
from src.core.signal_processing import RobustConfig

cfg = RobustConfig(mad_multiplier=2.5, gmm_max_overlap=0.25)
```

---

## `robust_score_windows()`

```python
def robust_score_windows(
    sqi_values: Dict[str, np.ndarray],
    signal: np.ndarray,
    window: int,
    step: int,
    config: RobustConfig,
) -> Dict[str, Any]:
```

Main entry point for the robust scorer.  Processes one file's worth of
per-window SQI values and returns a classification result.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `sqi_values` | `dict[str, ndarray]` | `{metric_name: 1-D array of raw per-window SQI values}`.  Values can be in any unit or scale. |
| `signal` | `ndarray` | Raw signal array.  Used only to derive `n_windows = (len(signal) − window) // step + 1`. |
| `window` | `int` | Window length in samples. |
| `step` | `int` | Step size in samples. |
| `config` | `RobustConfig` | Tuning parameters. |

### Return value

A `dict` with the following keys:

| Key | Type | Description |
|---|---|---|
| `"composite_scores"` | `list[float]` | Per-window consensus score in `[0, 1]`.  Mean rank across all enabled SQI metrics after rank normalisation. |
| `"quality"` | `list[str]` | `"normal"` or `"abnormal"` for each window, in window order. |
| `"normal_segments"` | `list[tuple[int,int]]` | `(start_sample, end_sample)` for each normal window. |
| `"abnormal_segments"` | `list[tuple[int,int]]` | `(start_sample, end_sample)` for each abnormal window. |
| `"score_threshold"` | `float` | The consensus-score value used as the decision boundary.  Interpretation depends on regime (MAD threshold, min GMM normal score, or percentile). |
| `"regime"` | `str` | Detected noise regime: `"mostly_good"`, `"bimodal"`, or `"heavy_noise"`. |
| `"file_flagged"` | `bool` | `True` if `normal_fraction < flag_file_min_normal_fraction`.  Signals low confidence. |
| `"normal_fraction"` | `float` | Fraction of windows classified as normal (`0.0–1.0`). |
| `"regime_info"` | `dict` | Diagnostic statistics used for regime detection (see below). |
| `"details"` | `dict` | Per-metric rank arrays plus GMM diagnostics if applicable (see below). |

#### `regime_info` structure

```json
{
  "n_windows": 20,
  "cross_metric_correlation": 0.4821,
  "consensus_variance": 0.0712,
  "bimodality_coefficient": 0.4830,
  "skewness": -1.0841,
  "reason": "mostly_good: skew=-1.084 < -0.3, cross_corr=0.482 >= 0.25"
}
```

| Key | Description |
|---|---|
| `n_windows` | Number of windows in the file |
| `cross_metric_correlation` | Mean pairwise Spearman correlation across all metric rank arrays |
| `consensus_variance` | Variance of the consensus score array |
| `bimodality_coefficient` | Sarle's BC value |
| `skewness` | Skewness of the consensus score array |
| `reason` | Human-readable explanation of the regime decision |

#### `details` structure

```json
{
  "signal_entropy_sqi": {"rank": [0.0, 0.111, 0.222, ...]},
  "snr_sqi":            {"rank": [0.0, 0.222, 0.111, ...]},
  "gmm": {
    "means": [0.2341, 0.7812],
    "variances": [0.0041, 0.0038],
    "bhattacharyya_overlap": 0.0012,
    "converged": true,
    "normal_component": 1
  }
}
```

The `"gmm"` key is present only when the BIMODAL regime was detected.  If GMM
fell back to MAD, the `"fallback"` key explains why:

```json
{
  "gmm": {
    "means": [0.41, 0.62],
    "variances": [0.08, 0.07],
    "bhattacharyya_overlap": 0.41,
    "converged": true,
    "fallback": "high_overlap (0.410) → MAD"
  }
}
```

### Empty result

When `n_windows == 0` or no valid metrics are provided, returns:

```json
{
  "composite_scores": [],
  "quality": [],
  "normal_segments": [],
  "abnormal_segments": [],
  "score_threshold": 0.0,
  "regime": "mostly_good",
  "file_flagged": false,
  "normal_fraction": 0.0,
  "regime_info": {},
  "details": {}
}
```

### Example

```python
import numpy as np
from src.core.signal_processing import robust_score_windows, RobustConfig

# Simulate 20 windows of 11 SQI metrics
rng = np.random.default_rng(42)
sqi_values = {f"metric_{i}": rng.normal(0, 1, 20) for i in range(11)}

signal = np.zeros(20 * 30000)   # placeholder; only length matters
config = RobustConfig()

result = robust_score_windows(
    sqi_values=sqi_values,
    signal=signal,
    window=30000,
    step=30000,
    config=config,
)

print(result["regime"])           # "mostly_good" / "bimodal" / "heavy_noise"
print(result["file_flagged"])     # True / False
print(result["normal_segments"])  # [(0, 30000), (60000, 90000), ...]
```

---

## `SignalProcessor.compute_robust_sqi()`

```python
def compute_robust_sqi(self, signal: np.ndarray) -> Dict[str, Any]:
```

Convenience method on `SignalProcessor` that:
1. Calls `compute_raw_sqi_values(signal)` to get per-metric arrays from vitalDSP
2. Calls `robust_score_windows(...)` with the config's `robust_config`
3. Returns the full result dict

Window and step sizes are derived from `config.fs × config.duration` and
`config.fs × config.step_size`.

### When it is called

`compute_robust_sqi()` is called automatically when `threshold_method == "robust_composite"` in:
- `SignalProcessor.get_primary_segments()` — for downstream RR/feature extraction
- `SignalProcessingPipeline.process_file()` — for JSON output generation

The result is embedded in the output JSON under the `"composite"` key along with
the regime, file_flagged, normal_fraction, and regime_info fields.

### Direct usage

```python
from src.core.signal_processing import SignalConfig, SignalProcessor

config = SignalConfig.from_yaml()
config.threshold_method = "robust_composite"

processor = SignalProcessor(config)
signal_data = processor.load_signal(path_to_file)
result = processor.compute_robust_sqi(signal_data.signal)

if result["file_flagged"]:
    print(f"WARNING: only {result['normal_fraction']:.1%} of windows are normal")
    print(f"Regime: {result['regime']}")
```

---

## Legacy API (still available)

The original `score_windows()` function and `CompositeConfig` dataclass are
unchanged and fully backward compatible.  They are used when
`threshold_method == "composite"`.

```python
from src.core.signal_processing import score_windows, CompositeConfig
```

See inline docstrings in `sqi_scorer.py` for their signatures.
