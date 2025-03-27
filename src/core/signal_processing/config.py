# src/core/signal_processing/config.py
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

@dataclass
class SignalConfig:
    """Configuration for signal processing pipeline."""
    # Processing mode
    mode: str = "directory"  # Options: "directory" or "file_list"
    
    # Base paths
    output_base: Path = Path('D:\Workspace\Data\\24EIa/output')
    data_dir: Path = Path('D:\Workspace\Data\\24EIa/input')
    file_list_path: Path = None  # Path to CSV file containing list of files to process
    
    # Derived paths
    SEGMENT_PATH: Path = output_base / 'Segmented_Data_24EI'
    FEATURE_PATH: Path = output_base / 'Feature_Data_24EI'
    OUTPUT_PATH: Path = output_base / 'signal_processing'
    
    # Additional output directories
    segment_dir: Path = SEGMENT_PATH
    feature_dir: Path = FEATURE_PATH
    
    # Signal processing parameters
    fs: int = 100
    duration: int = 300  # 5 minutes in seconds
    step_size: int = 300  # 5 minutes in seconds
    lowcut: float = 0.5
    highcut: float = 20.0
    nperseg: int = 1024

    
    # Peak detection parameters
    peak_height_percentile: float = 95
    peak_distance: int = 5
    
    # Processing parameters
    max_workers: int = 4
    batch_size: int = 100
    
    def __post_init__(self):
        """Create output directories after initialization."""
        if self.mode not in ["directory", "file_list"]:
            raise ValueError("mode must be either 'directory' or 'file_list'")
            
        if self.mode == "file_list" and not self.file_list_path:
            raise ValueError("file_list_path must be provided when mode is 'file_list'")
            
        self.output_base.mkdir(parents=True, exist_ok=True)
        self.SEGMENT_PATH.mkdir(parents=True, exist_ok=True)
        self.FEATURE_PATH.mkdir(parents=True, exist_ok=True)
        self.OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def get_harmonic_frequencies() -> Dict[str, List[float]]:
        """Get element harmonic frequencies."""
        return {
            'Mg': [4.0],
            'Ca': [6.0],
            'Fe': [12.0],
            'Zn': [18.0]
        } 