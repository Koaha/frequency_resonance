# src/core/signal_processing/feature_extractor.py
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, Any
import logging
from vitalDSP.transforms.beats_transformation import RRTransformation
from vitalDSP.physiological_features.hrv_analysis import HRVFeatures
from vitalDSP.feature_engineering.morphology_features import (
    PhysiologicalFeatureExtractor,
    PreprocessConfig
)

class FeatureExtractor:
    """Handles feature extraction from signal segments."""
    
    def __init__(self, fs: int = 100, signal_type: str = 'PPG'):
        self.fs = fs
        self.logger = logging.getLogger(__name__)
        self.signal_type = signal_type

    def extract_features(self, signal: np.ndarray) -> Dict[str, Any]:
        """Extract HRV and morphological features from signal segment."""
        try:
            if self.signal_type == "ECG":
                peak_config = {
                    "distance": 50,
                    "window_size": 7,
                    "threshold_factor": 1.6,
                    "search_window": 6,
                    "slope_unit": "radians",
                }
            else:  # PPG
                peak_config = {
                    "distance": 50,
                    "window_size": 7,
                    "threshold_factor": 0.8,
                    "search_window": 6,
                    "fs": self.fs,
                }

            # Extract RR intervals
            config = PreprocessConfig()
            # Create RR transformer with both configs
            rr_transformer = RRTransformation(signal, fs=self.fs, 
                                            signal_type=self.signal_type,
                                            options=None)  # options is for other transformations
            # Pass both configs when computing intervals
            rr_intervals = rr_transformer.compute_rr_intervals(
                preprocess_config=config,
                peak_config=peak_config
            )  # already in ms
            # Compute HRV features
            hrv_features = HRVFeatures(
                signal, 
                nn_intervals=rr_intervals, 
                fs=self.fs, 
                signal_type=self.signal_type
            )
            hrv_feats = hrv_features.compute_all_features()
            
            # Compute morphological features
            
            extractor = PhysiologicalFeatureExtractor(signal, fs=self.fs)
            morphology_feats = extractor.extract_features(
                signal_type=self.signal_type,
                preprocess_config=config,
                peak_config=peak_config 
            )
            
            return {**hrv_feats, **morphology_feats}, rr_intervals
            
        except Exception as e:
            self.logger.error(f"Feature extraction failed: {e}")
            raise