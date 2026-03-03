# src/core/signal_processing/signal_processor.py
from pathlib import Path
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Tuple, Any
import logging
import datetime as dt
from vitalDSP.utils.data_processing.data_loader import DataLoader
from vitalDSP.signal_quality_assessment.signal_quality_index import SignalQualityIndex
from .config import SignalConfig


@dataclass
class SignalData:
    """Container for signal data and metadata."""
    signal: np.ndarray
    timestamps: np.ndarray
    file_path: Path
    start_time: dt.datetime
    signal_type: str


class SignalProcessor:
    """Handles signal loading and quality assessment."""

    def __init__(self, config: SignalConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def load_signal(self, file_path: Path) -> SignalData:
        """Load signal data using vitalDSP DataLoader (supports OUCRU_CSV)."""
        try:
            loader = DataLoader(
                file_path=str(file_path),
                format=self.config.data_format,
                sampling_rate=self.config.fs,
            )
            df = loader.load(signal_column=self.config.signal_column)

            signal = df["signal"].values.astype(float)
            timestamps = pd.to_datetime(df["timestamp"]).values
            start_time = pd.Timestamp(timestamps[0]).to_pydatetime()
            signal_type = "ECG" if "ECG" in file_path.name.upper() else "PPG"

            self.logger.info(
                f"Loaded {len(signal)} samples from {file_path.name} "
                f"(column={self.config.signal_column}, type={signal_type})"
            )
            return SignalData(
                signal=signal,
                timestamps=timestamps,
                file_path=file_path,
                start_time=start_time,
                signal_type=signal_type,
            )
        except Exception as e:
            self.logger.error(f"Error loading signal from {file_path}: {e}")
            raise

    # ── quality assessment ───────────────────────────────────────────────

    def compute_all_sqi(self, signal: np.ndarray) -> Dict[str, Any]:
        """Compute every enabled SQI metric with its own threshold.

        Returns a dict keyed by SQI name, each containing:
          - values:  per-window SQI floats
          - quality: per-window "normal" / "abnormal" label
          - threshold / threshold_type used
          - normal_segments / abnormal_segments (sample ranges)
        """
        window = self.config.fs * self.config.duration
        step = self.config.fs * self.config.step_size
        sqi_obj = SignalQualityIndex(signal)
        results: Dict[str, Any] = {}

        for method_name in self.config.enabled_sqi_methods:
            method = getattr(sqi_obj, method_name, None)
            if method is None:
                continue

            params = self.config.sqi_params(method_name)
            try:
                vals, normal, abnormal = method(
                    window_size=window,
                    step_size=step,
                    threshold=params["threshold"],
                    threshold_type=params["threshold_type"],
                    aggregate=False,
                )

                normal_set = set()
                for s, e in normal:
                    normal_set.add((int(s), int(e)))

                n_windows = len(vals)
                per_window_quality = []
                for i in range(n_windows):
                    ws = i * step
                    we = ws + window
                    per_window_quality.append(
                        "normal" if (ws, we) in normal_set else "abnormal"
                    )

                results[method_name] = {
                    "threshold": params["threshold"],
                    "threshold_type": params["threshold_type"],
                    "values": [round(float(v), 6) for v in vals],
                    "quality": per_window_quality,
                    "normal_segments": [(int(s), int(e)) for s, e in normal],
                    "abnormal_segments": [(int(s), int(e)) for s, e in abnormal],
                }
            except Exception as exc:
                self.logger.warning(f"SQI method {method_name} failed: {exc}")
                results[method_name] = {"error": str(exc)}

        return results

    def get_primary_segments(
        self, signal: np.ndarray
    ) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        """Segmentation based on the configured primary SQI metric.

        Used to decide which windows get downstream processing (RR, features).
        """
        method_name = self.config.primary_sqi
        params = self.config.sqi_params(method_name)

        sqi = SignalQualityIndex(signal)
        method = getattr(sqi, method_name)
        _, normal_segments, abnormal_segments = method(
            window_size=self.config.fs * self.config.duration,
            step_size=self.config.fs * self.config.step_size,
            threshold=params["threshold"],
            threshold_type=params["threshold_type"],
            aggregate=False,
        )
        return normal_segments, abnormal_segments
