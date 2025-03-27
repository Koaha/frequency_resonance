# src/config/settings.py
from pathlib import Path
from dataclasses import dataclass

@dataclass
class SignalConfig:
    fs: int = 100  # Sampling frequency
    duration: int = 60 * 5  # Duration of each window (5 minutes)
    step_size: int = fs * 60 * 5  # Step size (30 seconds)

@dataclass
class PathConfig:
    BASE_DIR = Path(__file__).parent.parent.parent
    DATA_DIR = BASE_DIR / "data"
    OUTPUT_DIR = BASE_DIR / "output"
    SEGMENT_DIR = OUTPUT_DIR / "segments"
    FEATURE_DIR = OUTPUT_DIR / "features"
    REPORT_DIR = OUTPUT_DIR / "reports"

    def __post_init__(self):
        for path in [self.OUTPUT_DIR, self.SEGMENT_DIR, self.FEATURE_DIR, self.REPORT_DIR]:
            path.mkdir(parents=True, exist_ok=True)

config = SignalConfig()
paths = PathConfig()