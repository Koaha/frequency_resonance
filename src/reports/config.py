# src/reports/config.py
from dataclasses import dataclass
from pathlib import Path
from config.settings import paths

@dataclass
class ReportConfig:
    """Configuration for report generation.
    
    Attributes:
        fs (int): Sampling frequency in Hz
        duration (int): Duration of each window in seconds
        step_size (int): Step size between windows in samples
        base_work_dir (Path): Base working directory for report generation
        segment_dir (Path): Directory for segmented data
        feature_dir (Path): Directory for feature data
        event_dir (Path): Directory for event data
    """
    fs: int = 100
    duration: int = 300  # 5 minutes
    step_size: int = 3000  # 30 seconds * fs
    base_work_dir: Path = paths.BASE_DIR / "analysis"
    # segment_dir: Path = base_work_dir / "Segmented_Data/Data"
    segment_dir: Path = Path("D:\Workspace\Data\\24EIa\output\Segmented_Data_24EI")
    # feature_dir: Path = base_work_dir / "Feature_Data/Data"
    feature_dir: Path = Path("D:\Workspace\Data\\24EIa\output\Feature_Data_24EI")
    # event_dir: Path = base_work_dir / "Event_Data"
    event_dir: Path = Path("D:\Workspace\Data\\24EIa\output\Feature_Data_24EI")