# src/core/preprocessing.py
from typing import Tuple, List, Optional
import numpy as np
from ..config.settings import config
from ..utils.helpers import SignalProcessingError

class SignalPreprocessor:
    def __init__(self, fs: int = config.fs):
        self.fs = fs
        
    def segment_signal(
        self, 
        signal: np.ndarray, 
        window_size: int = config.duration * config.fs,
        step_size: int = config.step_size
    ) -> List[np.ndarray]:
        """
        Segment signal into overlapping windows.
        
        Args:
            signal: Input signal array
            window_size: Size of each window in samples
            step_size: Number of samples between windows
            
        Returns:
            List of signal segments
        """
        try:
            segments = []
            for start in range(0, len(signal) - window_size + 1, step_size):
                end = start + window_size
                segments.append(signal[start:end])
            return segments
        except Exception as e:
            raise SignalProcessingError(f"Error segmenting signal: {str(e)}")