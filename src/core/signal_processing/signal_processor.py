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
from .sqi_scorer import score_windows


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
        """Load signal data using vitalDSP DataLoader (supports OUCRU_CSV).

        Signal type and column are resolved per file via config.resolve_signal(),
        so mixed PPG / ECG directories work automatically.
        """
        try:
            signal_type, column = self.config.resolve_signal(file_path)

            loader = DataLoader(
                file_path=str(file_path),
                format=self.config.data_format,
                sampling_rate=self.config.fs,
            )
            df = loader.load(signal_column=column)

            signal = df["signal"].values.astype(float)
            timestamps = pd.to_datetime(df["timestamp"]).values
            start_time = pd.Timestamp(timestamps[0]).to_pydatetime()

            self.logger.info(
                f"Loaded {len(signal)} samples from {file_path.name} "
                f"(column={column}, type={signal_type})"
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

    def compute_raw_sqi_values(self, signal: np.ndarray) -> Dict[str, np.ndarray]:
        """Compute raw per-window SQI values for all enabled metrics.

        Unlike compute_all_sqi(), this returns only the numeric arrays
        without applying any threshold — used as input to the composite scorer.
        """
        window = self.config.fs * self.config.duration
        step = self.config.fs * self.config.step_size
        sqi_obj = SignalQualityIndex(signal)
        raw: Dict[str, np.ndarray] = {}

        for method_name in self.config.enabled_sqi_methods:
            method = getattr(sqi_obj, method_name, None)
            if method is None:
                continue
            params = self.config.sqi_params(method_name)
            try:
                vals, _, _ = method(
                    window_size=window,
                    step_size=step,
                    threshold=params["threshold"],
                    threshold_type=params["threshold_type"],
                    aggregate=False,
                )
                raw[method_name] = np.asarray(vals, dtype=float)
            except Exception as exc:
                self.logger.warning(f"SQI method {method_name} failed: {exc}")
        return raw

    def compute_composite_sqi(
        self, signal: np.ndarray
    ) -> Dict[str, Any]:
        """Compute composite statistical SQI scores.

        Returns the full result dict from sqi_scorer.score_windows(), which
        includes composite_scores, quality labels, segment lists, and
        per-metric detail breakdowns.
        """
        window = self.config.fs * self.config.duration
        step = self.config.fs * self.config.step_size
        raw_vals = self.compute_raw_sqi_values(signal)
        return score_windows(
            sqi_values=raw_vals,
            signal=signal,
            window=window,
            step=step,
            config=self.config.composite_config,
        )

    def get_primary_segments(
        self, signal: np.ndarray
    ) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
        """Segmentation for downstream processing (RR, features).

        Uses composite scoring when threshold_method == "composite",
        otherwise falls back to the legacy single-metric threshold.
        """
        if self.config.threshold_method == "composite":
            result = self.compute_composite_sqi(signal)
            return result["normal_segments"], result["abnormal_segments"]

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
