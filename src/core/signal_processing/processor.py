# src/core/signal_processing/processor.py
import json
from pathlib import Path
import logging
import numpy as np
from tqdm import tqdm
from typing import Any, Dict, List
from .config import SignalConfig
from .signal_processor import SignalProcessor
from .segment_handler import SegmentHandler


class SignalProcessingPipeline:
    """Coordinates the entire signal processing pipeline."""

    def __init__(self, config: SignalConfig = None):
        if config is None:
            config = SignalConfig()
        self.config = config
        self.signal_processor = SignalProcessor(config)
        self.segment_handler = SegmentHandler(config)
        self.logger = logging.getLogger(__name__)

    # ── public API ───────────────────────────────────────────────────────

    def process_file(self, file_path: Path) -> Dict[str, Any]:
        """Process a single file end-to-end and write JSON outputs."""
        try:
            signal_data = self.signal_processor.load_signal(file_path)

            # All SQI metrics (each with its own threshold)
            all_sqi = self.signal_processor.compute_all_sqi(signal_data.signal)

            # Primary SQI decides which segments get RR / feature extraction
            normal_segments, abnormal_segments = (
                self.signal_processor.get_primary_segments(signal_data.signal)
            )

            output_dirs = self._prepare_output_dirs(file_path)

            # Build per-window index → per-SQI quality lookup
            window = self.config.fs * self.config.duration
            step = self.config.fs * self.config.step_size
            n_samples = len(signal_data.signal)
            n_windows = max(0, (n_samples - window) // step + 1)
            per_window_sqi = self._build_per_window_quality(all_sqi, n_windows)

            # ── process segments ─────────────────────────────────────────
            segment_details: List[Dict[str, Any]] = []
            all_rr: Dict[str, Any] = {}

            for idx, (start, end) in enumerate(normal_segments):
                seg_len = end - start
                win_idx = start // step if step else 0

                detail = {
                    "segment_index": idx,
                    "window_index": int(win_idx),
                    "start_sample": int(start),
                    "end_sample": int(end),
                    "length_samples": int(seg_len),
                    "length_seconds": round(seg_len / self.config.fs, 2),
                    "primary_sqi_quality": "normal",
                    "quality_by_sqi": per_window_sqi[win_idx] if win_idx < len(per_window_sqi) else {},
                }
                segment_details.append(detail)

                rr_intervals = self.segment_handler.process_segment(
                    signal_data, start, end, output_dirs
                )
                if rr_intervals is not None and len(rr_intervals) > 0:
                    all_rr[f"segment_{idx}_{start}_{end}"] = {
                        "start_sample": int(start),
                        "end_sample": int(end),
                        "rr_intervals_ms": [round(float(v), 3) for v in rr_intervals],
                        "count": len(rr_intervals),
                        "mean_ms": round(float(np.mean(rr_intervals)), 3),
                        "std_ms": round(float(np.std(rr_intervals)), 3),
                    }

            for idx, (start, end) in enumerate(abnormal_segments):
                seg_len = end - start
                win_idx = start // step if step else 0

                segment_details.append({
                    "segment_index": len(normal_segments) + idx,
                    "window_index": int(win_idx),
                    "start_sample": int(start),
                    "end_sample": int(end),
                    "length_samples": int(seg_len),
                    "length_seconds": round(seg_len / self.config.fs, 2),
                    "primary_sqi_quality": "abnormal",
                    "quality_by_sqi": per_window_sqi[win_idx] if win_idx < len(per_window_sqi) else {},
                })

            # ── build JSON result ────────────────────────────────────────
            sqi_result = {
                "file": file_path.name,
                "total_samples": len(signal_data.signal),
                "total_duration_seconds": round(n_samples / self.config.fs, 2),
                "sampling_rate": self.config.fs,
                "signal_column": self.config.signal_column,
                "window_size_seconds": self.config.duration,
                "step_size_seconds": self.config.step_size,
                "primary_sqi": self.config.primary_sqi,
                "normal_segment_count": len(normal_segments),
                "abnormal_segment_count": len(abnormal_segments),
                "segments": sorted(segment_details, key=lambda s: s["start_sample"]),
                "sqi_metrics": all_sqi,
            }

            # ── write files ──────────────────────────────────────────────
            stem = file_path.stem
            _write_json(self.config.sqi_dir / f"{stem}_sqi.json", sqi_result)
            self.logger.info(f"SQI JSON  -> {self.config.sqi_dir / stem}_sqi.json")

            _write_json(self.config.rr_dir / f"{stem}_rr.json", all_rr)
            self.logger.info(f"RR  JSON  -> {self.config.rr_dir / stem}_rr.json")

            return sqi_result

        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {e}")
            return {"file": file_path.name, "error": str(e)}

    def process_files(self) -> None:
        """Process all CSV files in the data directory."""
        files = sorted(self.config.data_dir.rglob("*.csv"))
        self.logger.info(f"Found {len(files)} file(s) in {self.config.data_dir}")

        all_results = []
        for file_path in tqdm(files, desc="Processing files"):
            all_results.append(self.process_file(file_path))

        summary = self.config.sqi_dir / "sqi_summary.json"
        _write_json(summary, all_results)
        self.logger.info(f"Summary   -> {summary}")

    # ── helpers ───────────────────────────────────────────────────────────

    @staticmethod
    def _build_per_window_quality(
        all_sqi: Dict[str, Any], n_windows: int
    ) -> List[Dict[str, str]]:
        """Create a list (one entry per window index) mapping SQI name → quality."""
        per_window: List[Dict[str, str]] = [{} for _ in range(n_windows)]
        for sqi_name, sqi_data in all_sqi.items():
            qualities = sqi_data.get("quality")
            if not qualities:
                continue
            for i, q in enumerate(qualities):
                if i < n_windows:
                    per_window[i][sqi_name] = q
        return per_window

    def _prepare_output_dirs(self, file_path: Path) -> Dict[str, Path]:
        stem = file_path.stem
        dirs = {
            "segments": self.config.segment_dir / stem,
            "features": self.config.feature_dir / stem,
            "rr": self.config.rr_dir / stem,
        }
        for d in dirs.values():
            d.mkdir(parents=True, exist_ok=True)
        return dirs


def _write_json(path: Path, obj: Any) -> None:
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
