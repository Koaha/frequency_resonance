# src/reports/config.py
from dataclasses import dataclass, field
from pathlib import Path
from config.settings import load_config, resolve_path


@dataclass
class ReportConfig:
    """Configuration for report generation.

    All values are loaded from config.yaml.
    """
    fs: int = 100
    duration: int = 300
    step_size: int = 300

    base_work_dir: Path = field(default=None)
    segment_dir: Path = field(default=None)
    feature_dir: Path = field(default=None)
    event_dir: Path = field(default=None)
    report_dir: Path = field(default=None)

    def __post_init__(self):
        cfg = load_config()
        out = resolve_path(cfg.get("output_dir", "output"))
        reports_cfg = cfg.get("reports", {}) or {}

        self.fs = cfg.get("sampling_rate", self.fs)
        self.duration = cfg.get("segment_duration", self.duration)
        self.step_size = cfg.get("step_size", self.step_size)

        if self.base_work_dir is None:
            self.base_work_dir = out
        if self.segment_dir is None:
            self.segment_dir = out / "segments"
        if self.feature_dir is None:
            self.feature_dir = out / "features"
        if self.report_dir is None:
            raw = reports_cfg.get("report_dir", "output/reports")
            self.report_dir = resolve_path(raw)
        if self.event_dir is None:
            raw = reports_cfg.get("event_dir")
            self.event_dir = resolve_path(raw) if raw else None

        self.report_dir.mkdir(parents=True, exist_ok=True)
