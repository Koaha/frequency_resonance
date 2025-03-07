# src/core/resonance/config.py
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

@dataclass
class ResonanceConfig:
    """Configuration for resonance analysis."""
    SEGMENT_PATH: Path = Path('D:\Workspace\Data\\24EIa/output/Segmented_Data_24EI')
    FEATURE_PATH: Path = Path('D:\Workspace\Data\\24EIa/output/Feature_Data_24EI')
    OUTPUT_PATH: Path = Path('D:\Workspace\Data\\24EIa/output/resonance_analysis')
    MASTER_CSV: Path = OUTPUT_PATH / 'master.csv'
    PLOT_DIR: Path = OUTPUT_PATH / 'plots'
    
    # Signal processing parameters
    fs: int = 100
    segment_duration: int = 300  # 5 minutes in seconds
    lowcut: float = 0.5
    highcut: float = 20.0
    nperseg: int = 1024
    peak_height_percentile: float = 95
    peak_distance: int = 5

    @staticmethod
    def get_harmonic_frequencies() -> Dict[str, List[float]]:
        """Get element harmonic frequencies."""
        return {
            'Mg': [4.0],
            'Ca': [6.0],
            'Fe': [12.0],
            'Zn': [18.0]
        }