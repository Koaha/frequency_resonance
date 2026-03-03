# src/core/resonance/config.py
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from config.settings import load_config, resolve_path, DEFAULT_CONFIG_PATH


@dataclass
class ResonanceConfig:
    """Configuration settings for resonance analysis.

    All values are loaded from config.yaml (with sensible fallbacks).
    """

    # File system paths (derived from the shared output_dir)
    SEGMENT_PATH: Path = field(default=None)
    FEATURE_PATH: Path = field(default=None)
    OUTPUT_PATH: Path = field(default=None)
    MASTER_CSV: Path = field(default=None)
    PLOT_DIR: Path = field(default=None)

    # Signal processing parameters
    fs: int = 100
    segment_duration: int = 300
    lowcut: float = 0.5
    highcut: float = 20.0
    nperseg: int = 1024
    peak_height_percentile: float = 95
    peak_distance: int = 5

    def __post_init__(self):
        cfg = load_config()
        out = resolve_path(cfg.get("output_dir", "output"))

        if self.SEGMENT_PATH is None:
            self.SEGMENT_PATH = out / "segments"
        if self.FEATURE_PATH is None:
            self.FEATURE_PATH = out / "features"
        if self.OUTPUT_PATH is None:
            self.OUTPUT_PATH = out / "resonance_analysis"
        if self.MASTER_CSV is None:
            self.MASTER_CSV = self.OUTPUT_PATH / "master.csv.gz"
        if self.PLOT_DIR is None:
            self.PLOT_DIR = self.OUTPUT_PATH / "plots"

        self.fs = cfg.get("sampling_rate", self.fs)
        self.segment_duration = cfg.get("segment_duration", self.segment_duration)
        self.lowcut = cfg.get("lowcut", self.lowcut)
        self.highcut = cfg.get("highcut", self.highcut)
        self.nperseg = cfg.get("nperseg", self.nperseg)
        self.peak_height_percentile = cfg.get("peak_height_percentile", self.peak_height_percentile)
        self.peak_distance = cfg.get("peak_distance", self.peak_distance)

    @staticmethod
    def get_harmonic_frequencies() -> Dict[str, List[float]]:
        cfg = load_config()
        return cfg.get("harmonic_frequencies", {
            "Mg": [4.0], "Ca": [6.0], "Fe": [12.0], "Zn": [18.0],
        })
