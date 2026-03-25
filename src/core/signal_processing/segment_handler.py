# src/core/signal_processing/segment_handler.py
from pathlib import Path
import pandas as pd
import numpy as np
from typing import Optional, Tuple
import logging
from vitalDSP.transforms.beats_transformation import RRTransformation
from vitalDSP.feature_engineering.morphology_features import PreprocessConfig
from .signal_processor import SignalData
from .config import SignalConfig


class SegmentHandler:
    """Manages the processing and storage of signal segments."""

    def __init__(self, config: SignalConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def _get_peak_config(self, signal_type: str) -> dict:
        if signal_type == "ECG":
            return {
                "distance": 50,
                "window_size": 7,
                "threshold_factor": 1.6,
                "search_window": 6,
                "slope_unit": "radians",
            }
        return {
            "distance": 50,
            "window_size": 7,
            "threshold_factor": 0.8,
            "search_window": 6,
            "fs": self.config.fs,
        }

    def compute_rr_intervals(
        self, segment: np.ndarray, signal_type: str = "PPG"
    ) -> np.ndarray:
        """Extract RR intervals (ms) from a signal segment."""
        peak_config = self._get_peak_config(signal_type)
        preprocess_config = PreprocessConfig()

        rr = RRTransformation(
            segment, fs=self.config.fs, signal_type=signal_type, options=None
        )
        rr_intervals = rr.compute_rr_intervals(
            preprocess_config=preprocess_config, peak_config=peak_config
        )  # already in ms
        return rr_intervals

    def process_segment(
        self,
        signal_data: SignalData,
        start: int,
        end: int,
        output_dirs: dict[str, Path],
    ) -> Optional[np.ndarray]:
        """Process a single signal segment.

        Always computes RR intervals (fast).
        Optionally runs full HRV + morphology feature extraction when
        config.extract_features is True.

        Returns the RR intervals (ms) or None on failure.
        """
        try:
            segment = signal_data.signal[start:end]
            timestamps = signal_data.timestamps[start:end]
            base_name = f"{signal_data.file_path.stem}_{start}_{end}"

            # ── optionally save segment CSV ───────────────────────────────
            if self.config.save_segments:
                pd.DataFrame({
                    "timestamp": timestamps,
                    "signal": segment,
                }).to_csv(output_dirs["segments"] / f"{base_name}.csv", index=False)

            # ── always: compute & save RR intervals ──────────────────────
            rr_intervals = self.compute_rr_intervals(
                segment, signal_data.signal_type
            )
            if len(rr_intervals) > 0:
                np.savetxt(
                    output_dirs["rr"] / f"{base_name}_rr.txt",
                    rr_intervals, fmt="%.3f",
                )

            # ── optional: full feature extraction (slow) ─────────────────
            if self.config.extract_features:
                self._extract_and_save_features(
                    segment, rr_intervals, signal_data, start, end, output_dirs
                )

            return rr_intervals

        except Exception as e:
            self.logger.error(f"Error processing segment {start}-{end}: {e}")
            return None

    def _extract_and_save_features(
        self,
        segment: np.ndarray,
        rr_intervals: np.ndarray,
        signal_data: SignalData,
        start: int,
        end: int,
        output_dirs: dict[str, Path],
    ) -> None:
        from .feature_extractor import FeatureExtractor
        extractor = FeatureExtractor(fs=self.config.fs, signal_type=signal_data.signal_type)
        features, _ = extractor.extract_features(segment)

        base_name = f"{signal_data.file_path.stem}_{start}_{end}"
        features_df = pd.DataFrame([features])
        features_df["file_path"] = str(signal_data.file_path)
        features_df["start"] = start
        features_df["end"] = end
        features_df.to_csv(
            output_dirs["features"] / f"{base_name}_features.csv", index=False
        )
