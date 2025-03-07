# src/core/signal_processing/segment_handler.py
from pathlib import Path
import pandas as pd
import numpy as np
from typing import Optional
import logging
from .signal_processor import SignalData
from .feature_extractor import FeatureExtractor

class SegmentHandler:
    """Manages the processing and storage of signal segments."""
    
    def __init__(self, config: SignalConfig):
        self.config = config
        self.feature_extractor = FeatureExtractor(fs=config.fs)
        self.logger = logging.getLogger(__name__)

    def process_segment(
        self,
        signal_data: SignalData,
        start: int,
        end: int,
        output_dirs: Dict[str, Path]
    ) -> bool:
        """Process a single signal segment."""
        try:
            # Prepare segment data
            segment = signal_data.signal[start:end]
            timestamps = signal_data.timestamps[start:end]
            
            # Extract features
            features, rr_intervals = self.feature_extractor.extract_features(segment)
            
            # Save segment data
            self._save_segment_data(
                segment,
                timestamps,
                signal_data.file_path,
                start,
                end,
                features,
                rr_intervals,
                output_dirs
            )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing segment {start}-{end}: {e}")
            return False

    def _save_segment_data(
        self,
        segment: np.ndarray,
        timestamps: np.ndarray,
        file_path: Path,
        start: int,
        end: int,
        features: Dict,
        rr_intervals: np.ndarray,
        output_dirs: Dict[str, Path]
    ) -> None:
        """Save segment data, features, and RR intervals."""
        base_name = f"{file_path.stem}_{start}_{end}"
        
        # Save segment
        pd.DataFrame({
            "TIMESTAMP_MS": timestamps,
            "PLETH": segment
        }).to_csv(output_dirs['segments'] / f"{base_name}.csv", index=False)
        
        # Save features
        features_df = pd.DataFrame([features])
        features_df['file_path'] = str(file_path)
        features_df['start'] = start
        features_df['end'] = end
        features_df.to_csv(
            output_dirs['features'] / f"{base_name}_features.csv",
            index=False
        )
        
        # Save RR intervals
        np.savetxt(output_dirs['rr'] / f"{base_name}_rr.txt", rr_intervals)