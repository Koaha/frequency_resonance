# src/analysis/Dengue_69DX/data_processor/config.py
from dataclasses import dataclass, field
from pathlib import Path
from config.settings import load_config, resolve_path


@dataclass
class DataPaths:
    """Data path configuration for Dengue analysis.

    All values are loaded from the 'analysis' section of config.yaml.
    """
    ADULT_PATH: Path = field(default=None)
    CHILD_PATH: Path = field(default=None)
    SC_INSTRUCTION_PATH: Path = field(default=None)
    OUTPUT_PATH: Path = field(default=None)

    def __post_init__(self):
        cfg = load_config()
        analysis = cfg.get("analysis", {}) or {}

        if self.ADULT_PATH is None:
            self.ADULT_PATH = resolve_path(analysis.get("adult_path", "data/Adults"))
        if self.CHILD_PATH is None:
            self.CHILD_PATH = resolve_path(analysis.get("child_path", "data/Children"))
        if self.SC_INSTRUCTION_PATH is None:
            self.SC_INSTRUCTION_PATH = resolve_path(analysis.get("sc_instruction_path", "data/SC_data.csv"))
        if self.OUTPUT_PATH is None:
            self.OUTPUT_PATH = resolve_path(analysis.get("processed_output", "output/processed_data.csv"))
