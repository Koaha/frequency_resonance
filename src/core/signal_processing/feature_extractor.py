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
    
    def __init__(self, fs: int = 100):
        self.fs = fs
        self.logger = logging.getLogger(__name__)

    def extract_features(self, signal: np.ndarray) -> Dict[str, Any]:
        """Extract HRV and morphological features from signal segment."""
        try:
            # Extract RR intervals
            rr_transformer = RRTransformation(signal, fs=self.fs, signal_type='ppg')
            rr_intervals = rr_transformer.process_rr_intervals() * 1000  # convert to ms
            
            # Compute HRV features
            hrv_features = HRVFeatures(
                signal, 
                nn_intervals=rr_intervals, 
                fs=self.fs, 
                signal_type='ppg'
            )
            hrv_feats = hrv_features.compute_all_features()
            
            # Compute morphological features
            config = PreprocessConfig()
            extractor = PhysiologicalFeatureExtractor(signal, fs=self.fs)
            morphology_feats = extractor.extract_features(
                signal_type="PPG",
                preprocess_config=config
            )
            
            return {**hrv_feats, **morphology_feats}, rr_intervals
            
        except Exception as e:
            self.logger.error(f"Feature extraction failed: {e}")
            raise