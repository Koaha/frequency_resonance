from dataclasses import dataclass
from pathlib import Path
from ...config.settings import paths

@dataclass
class DataPaths:
    """Data path configuration"""
    ADULT_PATH: Path = paths.DATA_DIR / "Adults"
    CHILD_PATH: Path = paths.DATA_DIR / "Children"
    SC_INSTRUCTION_PATH: Path = paths.DATA_DIR / "SC_data.csv"
    OUTPUT_PATH: Path = paths.OUTPUT_DIR / "processed_data.csv"
