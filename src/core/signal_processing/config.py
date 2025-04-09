# src/core/signal_processing/config.py
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
import json
import os

def load_config():
    """Load configuration from JSON file."""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found at {config_path}, using default values")
        return {}
    except json.JSONDecodeError:
        print(f"Error parsing config file {config_path}, using default values")
        return {}

# Load config once at module level
CONFIG = load_config()

@dataclass
class SignalConfig:
    """Configuration for signal processing pipeline."""
    # Processing mode
    mode: str = CONFIG.get("mode", "directory")  # Options: "directory" or "file_list"
    
    # Base paths
    output_base: Path = Path(CONFIG.get("output_base", 'W:/Workspace/Data/24EIa/output'))
    data_dir: Path = Path(CONFIG.get("data_dir", 'W:/Workspace/Data/24EIa/input'))
    file_list_path: Optional[Path] = Path(CONFIG.get("file_list_path")) if CONFIG.get("file_list_path") else None
    
    # Derived paths
    SEGMENT_PATH: Path = output_base / 'Segmented_Data_24EI'
    FEATURE_PATH: Path = output_base / 'Feature_Data_24EI'
    OUTPUT_PATH: Path = output_base / 'signal_processing'
    
    # Additional output directories
    segment_dir: Path = SEGMENT_PATH
    feature_dir: Path = FEATURE_PATH
    
    # Signal processing parameters
    fs: int = CONFIG.get("fs", 100)
    duration: int = CONFIG.get("duration", 180)
    step_size: int = CONFIG.get("step_size", 180)
    lowcut: float = CONFIG.get("lowcut", 0.5)
    highcut: float = CONFIG.get("highcut", 20.0)
    nperseg: int = CONFIG.get("nperseg", 1024)

    
    # Peak detection parameters
    peak_height_percentile: float = CONFIG.get("peak_height_percentile", 95)
    peak_distance: int = CONFIG.get("peak_distance", 5)
    
    # Processing parameters
    max_workers: int = CONFIG.get("max_workers", 4)
    batch_size: int = CONFIG.get("batch_size", 100)
    
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
        return CONFIG.get("harmonic_frequencies", {
            'Mg': [4.0],
            'Ca': [6.0],
            'Fe': [12.0],
            'Zn': [18.0]
        })