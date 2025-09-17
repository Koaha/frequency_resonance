# src/core/signal_processing/signal_processor.py
from pathlib import Path
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Tuple, Optional, Dict
import logging
import datetime as dt
from vitalDSP.signal_quality_assessment.signal_quality_index import SignalQualityIndex
from .config import SignalConfig
import datetime

@dataclass
class SignalData:
    """Container for signal data and metadata."""
    signal: np.ndarray
    timestamps: np.ndarray
    file_path: Path
    start_time: dt.datetime
    signal_type: str  # 'PPG' or 'ECG'

class SignalProcessor:
    """Handles signal processing operations."""
    
    def __init__(self, config: SignalConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def _is_ecg_file(self, file_path: Path) -> bool:
        """Check if the file is an ECG file based on filename."""
        return 'ECG' in str(file_path).upper() #file_path.name.upper()

    def _combine_ecg_headers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Combine the first three rows of ECG data to create proper headers."""
        # Get the three header rows
        device_row = df.iloc[0]
        feature_row = df.iloc[1]
        calibration_row = df.iloc[2]
        unit_row = df.iloc[3]
        
        # Combine headers
        new_headers = []
        for device, feature, calib, unit in zip(device_row, feature_row, calibration_row, unit_row):
            new_header = f"{device}_{feature}_{calib}_{unit}"
            new_headers.append(new_header)
        
        # Create new dataframe without the header rows
        new_df = df.iloc[4:].copy()
        new_df.columns = new_headers
        
        # Convert all cells to float type
        new_df = new_df.astype(float)
        return new_df

    def _select_ecg_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        required_columns = ['LL-RA_24BIT_CAL', 'Timestamp_CAL']
        
        # Find matching columns that contain our required column names
        matching_columns = {}
        for required in required_columns:
            matches = [col for col in df.columns if required in col]
            if not matches:
                raise ValueError(f"Missing required ECG column: {required}")
            matching_columns[required] = matches[0]  # Take the first match
            
        # Select the matched columns
        return df[matching_columns.values()], matching_columns

    def wearable_timestamp_to_datetime(self, ts):
        try:
            ts_float = float(ts)  # Convert to float first
            return datetime.datetime.fromtimestamp((ts_float))
        except Exception as e:
            self.logger.error(f"Error converting timestamp to datetime: {e}")
            return None
        # return datetime.datetime.utcfromtimestamp(int(ts_float)) \
        #     + datetime.timedelta(days=ts_float % 1) \
        #     - datetime.timedelta(days=366)
    
    def load_signal(self, file_path: Path) -> SignalData:
        """Load and prepare signal data from file."""
        try:
            if self._is_ecg_file(file_path):
                # Read ECG file with all rows first
                df = pd.read_csv(file_path, header=None, delimiter='\t')
                
                # Combine headers from first three rows
                df = self._combine_ecg_headers(df)
                
                # Select only the required columns
                # df = self._select_ecg_columns(df)
                df, matching_columns = self._select_ecg_columns(df)
                
                # Extract signal and timestamp
                # signal = np.array(df['LL-RA_24BIT_CAL'].values)
                # timestamp_ms = np.array(df['Timestamp_CAL'].values)
                signal = np.array(df[matching_columns['LL-RA_24BIT_CAL']].values)
                timestamp_ms = np.array(df[matching_columns['Timestamp_CAL']].values)
                
                # Get start time from filename
                start_datetime = dt.datetime.strptime(
                    file_path.stem.split("_")[2], 
                    # '%d.%m.%Y.%H.%M.%S'
                    '%Y%m%dT%H%M%S.%f%z'
                )
                
                # timestamps = start_datetime + pd.to_timedelta(timestamp_ms, unit='ms')
                timestamps = np.array([self.wearable_timestamp_to_datetime(ts) for ts in timestamp_ms])
                
                return SignalData(
                    signal=signal,
                    timestamps=timestamps,
                    file_path=file_path,
                    start_time=start_datetime,
                    signal_type='ECG'
                )
                
            else:
                # Handle PPG files as before
                # with open(file_path, encoding="utf-8", errors="ignore") as f:
                #     df = pd.read_csv(f)

                df = pd.read_csv(file_path, encoding="latin1", on_bad_lines="skip")
                
                try:
                    # Extract date from file path (e.g., 21122018 from the path)
                    date_str = str(file_path).split('/')[-3]  # Get the date folder name
                    # Parse the date (ddmmyyyy format) and set time to noon
                    start_datetime = dt.datetime.strptime(date_str, '%d%m%Y').replace(
                        hour=12, minute=0, second=0, microsecond=0
                    )
                except (ValueError, IndexError) as e:
                    # Set default to 4 years before today
                    start_datetime = dt.datetime.now() - dt.timedelta(days=4*365)
                    self.logger.warning(f"Could not parse datetime from file path {file_path}, using default date: {start_datetime}")
                
                signal = np.array(df['PLETH'].values)
                timestamp_ms = np.array(df['TIMESTAMP_MS'].values)
                timestamps = start_datetime + pd.to_timedelta(timestamp_ms, unit='ms')
                
                return SignalData(
                    signal=signal,
                    timestamps=timestamps,
                    file_path=file_path,
                    start_time=start_datetime,
                    signal_type='PPG'
                )
            
        except Exception as e:
            self.logger.error(f"Error loading signal from {file_path}: {e}")
            raise

    def get_quality_segments(self, signal: np.ndarray) -> Tuple[np.ndarray, list]:
        """Identify high-quality segments in the signal."""
        sqi = SignalQualityIndex(signal)
        sqi_values, normal_segments, _ = sqi.signal_entropy_sqi(
            window_size=self.config.fs * self.config.duration,
            step_size=self.config.fs * self.config.step_size,
            threshold=-2,
            threshold_type='below'
        )
        return sqi_values, normal_segments