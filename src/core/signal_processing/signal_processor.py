# src/core/signal_processing/signal_processor.py
from pathlib import Path
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Tuple, Optional
import logging
from vitalDSP.signal_quality_assessment.signal_quality_index import SignalQualityIndex

@dataclass
class SignalData:
    """Container for signal data and metadata."""
    signal: np.ndarray
    timestamps: np.ndarray
    file_path: Path
    start_time: dt.datetime

class SignalProcessor:
    """Handles signal processing operations."""
    
    def __init__(self, config: SignalConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def load_signal(self, file_path: Path) -> SignalData:
        """Load and prepare signal data from file."""
        try:
            df = pd.read_csv(file_path)
            start_datetime = dt.datetime.strptime(
                file_path.stem, 
                '%Y%m%dT%H%M%S.%f%z'
            )
            
            signal = np.array(df['PLETH'].values)
            timestamp_ms = np.array(df['TIMESTAMP_MS'].values)
            timestamps = start_datetime + pd.to_timedelta(timestamp_ms, unit='ms')
            
            return SignalData(signal, timestamps, file_path, start_datetime)
            
        except Exception as e:
            self.logger.error(f"Error loading signal from {file_path}: {e}")
            raise

    def get_quality_segments(self, signal: np.ndarray) -> Tuple[np.ndarray, list]:
        """Identify high-quality segments in the signal."""
        sqi = SignalQualityIndex(signal)
        sqi_values, normal_segments, _ = sqi.signal_entropy_sqi(
            window_size=self.config.fs * self.config.duration,
            step_size=self.config.step_size,
            threshold=-2,
            threshold_type='below'
        )
        return sqi_values, normal_segments