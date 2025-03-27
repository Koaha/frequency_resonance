# src/core/resonance/data_manager.py
import pandas as pd
import numpy as np
from pathlib import Path
import datetime as dt
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import logging
from .config import ResonanceConfig  # Add this import
from tqdm import tqdm

@dataclass
class PatientData:
    """Container for patient signal data."""
    day1_signal: np.ndarray
    day5_signal: np.ndarray
    day1_count: int
    day5_count: int
    time_points: List[Tuple[dt.datetime, dt.datetime]]
    day1_date: dt.date

class DataManager:
    """Handle data loading and organization."""
    
    def __init__(self, config: ResonanceConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def load_patient_files(self) -> pd.DataFrame:
        """Load and organize patient files."""
        data_list = []
        
        # Get total number of patient directories first
        patient_dirs = list(self.config.SEGMENT_PATH.glob("*"))
        patient_dirs = [d for d in patient_dirs if d.is_dir()]
        
        # Add progress bar for file loading
        with tqdm(total=len(patient_dirs), desc="Loading patient files") as pbar:
            for patient_dir in patient_dirs:
                data_path = patient_dir / "data"
                feature_path = (self.config.FEATURE_PATH / patient_dir.name 
                              / "data" / "features")
                
                if not data_path.is_dir():
                    pbar.update(1)
                    continue
                
                rr_folder = data_path / "rr"
                segments_folder = data_path / "segments"
                
                if rr_folder.is_dir() and segments_folder.is_dir():
                    rr_files = list(rr_folder.glob("*_rr.txt"))
                    for rr_file in rr_files:
                        segment_file = rr_file.stem.replace('_rr', '') + '.csv'
                        feature_file = rr_file.stem.replace('_rr', '_features.csv')
                        
                        data_list.append({
                            "patient_id": patient_dir.name,
                            "rr_path": str(rr_file),
                            "feature_path": str(feature_path / feature_file),
                            "segment_path": str(segments_folder / segment_file)
                        })
                
                pbar.update(1)
                pbar.set_postfix({"Patient": patient_dir.name})
        
        df = pd.DataFrame(data_list)
        return df.sort_values(by=["segment_path", "patient_id"])

    def process_patient_data(
        self, 
        df_patient: pd.DataFrame,
        patient_id: str
    ) -> PatientData:
        """Process patient data into day1 and day5 signals."""
        df_patient = df_patient.sort_values(by=['segment_path'])
        
        first_segment_time = dt.datetime.strptime(
            Path(df_patient['segment_path'].iloc[0]).stem.split("_")[0],
            # '%Y%m%dT%H%M%S'
            '%Y%m%dT%H%M%S.%f%z'
        )
        day1_date = first_segment_time.date()
        
        day1_signals = []
        day5_signals = []
        time_points = []
        day1_count = 0
        day5_count = 0
        
        # Add progress bar for segment processing
        with tqdm(total=len(df_patient), desc=f"Processing segments for {patient_id}") as pbar:
            for _, row in df_patient.iterrows():
                try:
                    segment = pd.read_csv(row['segment_path'])['PLETH'].values
                    segment_info = self._process_segment_time(row['segment_path'])
                    
                    if segment_info.is_day1:
                        day1_signals.append(segment)
                        day1_count += 1
                    else:
                        day5_signals.append(segment)
                        day5_count += 1
                        
                    time_points.append((segment_info.start_time, segment_info.end_time))
                    
                except Exception as e:
                    self.logger.warning(f"Error processing segment {row['segment_path']}: {e}")
                finally:
                    pbar.update(1)
                    pbar.set_postfix({
                        "Day1": day1_count,
                        "Day5": day5_count
                    })
        
        return PatientData(
            day1_signal=np.concatenate(day1_signals) if day1_signals else np.array([]),
            day5_signal=np.concatenate(day5_signals) if day5_signals else np.array([]),
            day1_count=day1_count,
            day5_count=day5_count,
            time_points=time_points,
            day1_date=day1_date
        )

    def _process_segment_time(
        self, 
        segment_path: str
    ) -> Tuple[dt.datetime, dt.datetime, bool]:
        """Process segment timing information."""
        @dataclass
        class SegmentInfo:
            start_time: dt.datetime
            end_time: dt.datetime
            is_day1: bool
            
        path = Path(segment_path)
        parts = path.stem.split("_")
        
        start_time = dt.datetime.strptime(parts[0], '%Y%m%dT%H%M%S.%f%z')
        offset = int(parts[1]) / self.config.fs
        
        segment_start = start_time + dt.timedelta(seconds=offset)
        segment_end = segment_start + dt.timedelta(
            seconds=self.config.segment_duration
        )
        
        return SegmentInfo(
            start_time=segment_start,
            end_time=segment_end,
            is_day1=segment_start.date() == start_time.date()
        )