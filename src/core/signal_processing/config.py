# src/core/signal_processing/config.py
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional
from config.settings import load_config, resolve_path, BASE_DIR, DEFAULT_CONFIG_PATH
from .sqi_scorer import CompositeConfig

# Fallback when no sqi section exists in YAML
_DEFAULT_SQI_ENTRY = {"enabled": True, "threshold": -2, "threshold_type": "below"}

_ALL_SQI_METHODS = [
    "signal_entropy_sqi",
    "snr_sqi",
    "kurtosis_sqi",
    "skewness_sqi",
    "zero_crossing_sqi",
    "energy_sqi",
    "amplitude_variability_sqi",
    "baseline_wander_sqi",
    "peak_to_peak_amplitude_sqi",
    "ppg_signal_quality_sqi",
    "respiratory_signal_quality_sqi",
]


@dataclass
class SignalConfig:
    """Configuration for signal processing pipeline.

    Values are resolved in this order:
      1. Explicit keyword arguments (e.g. from CLI)
      2. Values in the YAML config file
      3. Hardcoded defaults below
    """
    mode: str = "directory"

    data_dir: Path = field(default_factory=lambda: BASE_DIR / "data")
    output_base: Path = field(default_factory=lambda: BASE_DIR / "output")
    file_list_path: Optional[Path] = None

    # Signal processing
    fs: int = 100
    duration: int = 300
    step_size: int = 300
    lowcut: float = 0.5
    highcut: float = 20.0
    nperseg: int = 1024

    # OUCRU data loading
    signal_type: str = "auto"       # "auto" | "PPG" | "ECG"
    signal_column: str = "pleth"    # PPG column: pleth | ir | red
    ecg_signal_column: str = "ecg"  # ECG column
    data_format: str = "OUCRU_CSV"

    # SQI — thresholding
    threshold_method: str = "composite"   # "value" | "composite"
    primary_sqi: str = "signal_entropy_sqi"
    sqi_config: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    composite_config: CompositeConfig = field(default_factory=CompositeConfig)

    # Peak detection
    peak_height_percentile: float = 95
    peak_distance: int = 5

    # Feature extraction (slow — disable to only get SQI + RR)
    extract_features: bool = False

    # Processing
    max_workers: int = 4
    batch_size: int = 100

    _VALID_SIGNAL_TYPES = ("auto", "PPG", "ECG")
    _VALID_THRESHOLD_METHODS = ("value", "composite")

    def __post_init__(self):
        if self.mode not in ("directory", "file_list"):
            raise ValueError("mode must be 'directory' or 'file_list'")
        if self.mode == "file_list" and not self.file_list_path:
            raise ValueError("file_list_path required when mode is 'file_list'")

        self.signal_type = self.signal_type.upper() if self.signal_type != "auto" else "auto"
        if self.signal_type not in self._VALID_SIGNAL_TYPES:
            raise ValueError(f"signal_type must be one of {self._VALID_SIGNAL_TYPES}")

        if self.threshold_method not in self._VALID_THRESHOLD_METHODS:
            raise ValueError(f"threshold_method must be one of {self._VALID_THRESHOLD_METHODS}")

        self.data_dir = Path(self.data_dir)
        self.output_base = Path(self.output_base)
        if self.file_list_path is not None:
            self.file_list_path = Path(self.file_list_path)

        if not self.sqi_config:
            self.sqi_config = {m: dict(_DEFAULT_SQI_ENTRY) for m in _ALL_SQI_METHODS}

        # Only ensure output_base exists; per-file dirs are created in the processor
        self.output_base.mkdir(parents=True, exist_ok=True)

    def resolve_signal(self, file_path: Path) -> tuple:
        """Determine (signal_type, column_name) for a given file.

        When signal_type is "auto", infer from the filename:
          - filename contains "ecg" (case-insensitive) → ECG
          - otherwise → PPG
        Returns ("PPG", self.signal_column) or ("ECG", self.ecg_signal_column).
        """
        if self.signal_type == "auto":
            detected = "ECG" if "ECG" in file_path.name.upper() else "PPG"
        else:
            detected = self.signal_type

        column = self.ecg_signal_column if detected == "ECG" else self.signal_column
        return detected, column

    # ── derived directories ──────────────────────────────────────────────
    @property
    def segment_dir(self) -> Path:
        return self.output_base / "segments"

    @property
    def feature_dir(self) -> Path:
        return self.output_base / "features"

    @property
    def sqi_dir(self) -> Path:
        return self.output_base / "sqi"

    @property
    def rr_dir(self) -> Path:
        return self.output_base / "rr_intervals"

    @property
    def enabled_sqi_methods(self) -> List[str]:
        return [m for m, c in self.sqi_config.items() if c.get("enabled", True)]

    def sqi_params(self, method: str) -> Dict[str, Any]:
        """Return {threshold, threshold_type} for a given SQI method."""
        entry = self.sqi_config.get(method, _DEFAULT_SQI_ENTRY)
        return {
            "threshold": entry.get("threshold", -2),
            "threshold_type": entry.get("threshold_type", "below"),
        }

    # ── factory from YAML ────────────────────────────────────────────────
    @classmethod
    def from_yaml(cls, yaml_path: Path = DEFAULT_CONFIG_PATH, **overrides) -> "SignalConfig":
        """Build config from a YAML file, with optional keyword overrides."""
        cfg = load_config(yaml_path)

        _YAML_TO_FIELD = {
            "mode": "mode",
            "data_dir": "data_dir",
            "output_dir": "output_base",
            "file_list_path": "file_list_path",
            "data_format": "data_format",
            "signal_type": "signal_type",
            "signal_column": "signal_column",
            "ecg_signal_column": "ecg_signal_column",
            "sampling_rate": "fs",
            "segment_duration": "duration",
            "step_size": "step_size",
            "lowcut": "lowcut",
            "highcut": "highcut",
            "nperseg": "nperseg",
            "threshold_method": "threshold_method",
            "primary_sqi": "primary_sqi",
            "peak_height_percentile": "peak_height_percentile",
            "peak_distance": "peak_distance",
            "extract_features": "extract_features",
            "max_workers": "max_workers",
            "batch_size": "batch_size",
        }

        kwargs: Dict[str, Any] = {}
        for yaml_key, field_name in _YAML_TO_FIELD.items():
            if yaml_key in cfg and cfg[yaml_key] is not None:
                val = cfg[yaml_key]
                if field_name in ("data_dir", "output_base", "file_list_path"):
                    val = resolve_path(val)
                kwargs[field_name] = val

        # Composite threshold config
        raw_composite = cfg.get("composite", {})
        if raw_composite:
            kwargs["composite_config"] = CompositeConfig(
                min_quantile=raw_composite.get("min_quantile", 10.0),
                max_tail_area=raw_composite.get("max_tail_area", 0.05),
                max_modified_z=raw_composite.get("max_modified_z", 3.0),
                min_trapz_ratio=raw_composite.get("min_trapz_ratio", 0.3),
                max_rolling_var=raw_composite.get("max_rolling_var", 2.0),
                weights=raw_composite.get("weights", [0.25, 0.20, 0.20, 0.20, 0.15]),
                score_threshold=raw_composite.get("score_threshold", 0.5),
            )

        # Per-SQI config
        raw_sqi = cfg.get("sqi", {})
        if raw_sqi:
            sqi_cfg: Dict[str, Dict[str, Any]] = {}
            for method_name in _ALL_SQI_METHODS:
                entry = raw_sqi.get(method_name, {})
                sqi_cfg[method_name] = {
                    "enabled": entry.get("enabled", True),
                    "threshold": entry.get("threshold", -2),
                    "threshold_type": entry.get("threshold_type", "below"),
                }
            kwargs["sqi_config"] = sqi_cfg

        kwargs.update({k: v for k, v in overrides.items() if v is not None})
        return cls(**kwargs)

    @staticmethod
    def get_harmonic_frequencies() -> Dict[str, List[float]]:
        cfg = load_config()
        return cfg.get("harmonic_frequencies", {
            "Mg": [4.0], "Ca": [6.0], "Fe": [12.0], "Zn": [18.0],
        })
