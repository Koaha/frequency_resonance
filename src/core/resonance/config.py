# src/core/resonance/config.py
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

@dataclass
class ResonanceConfig:
    """Configuration settings for resonance analysis."""
    
    # File system paths
    SEGMENT_PATH: Path = Path('D:/Workspace/Data/24EIa/output/Segmented_Data_24EI')
    FEATURE_PATH: Path = Path('D:/Workspace/Data/24EIa/output/Feature_Data_24EI')
    OUTPUT_PATH: Path = Path('D:/Workspace/Data/24EIa/output/resonance_analysis')
    MASTER_CSV: Path = OUTPUT_PATH / 'master.csv.gz'
    PLOT_DIR: Path = OUTPUT_PATH / 'plots'
    
    # Signal processing parameters
    fs: int = 100  # Sampling frequency in Hz
    segment_duration: int = 300  # Segment duration in seconds (5 minutes)
    lowcut: float = 0.5  # Low frequency cutoff for bandpass filter
    highcut: float = 20.0  # High frequency cutoff for bandpass filter
    nperseg: int = 1024  # Number of samples per STFT segment
    peak_height_percentile: float = 95  # Percentile for peak detection threshold
    peak_distance: int = 5  # Minimum distance between peaks

    @staticmethod
    def get_harmonic_frequencies() -> Dict[str, List[float]]:
        """Return harmonic frequencies for elements of interest."""
        return {
            'Mg': [4.0],  # Magnesium resonance frequency
            'Ca': [6.0],  # Calcium resonance frequency
            'Fe': [12.0],  # Iron resonance frequency
            'Zn': [18.0]  # Zinc resonance frequency
        }