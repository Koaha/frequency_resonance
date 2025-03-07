import numpy as np
import pandas as pd
import os
import concurrent.futures
from vitalDSP.signal_quality_assessment.signal_quality_index import SignalQualityIndex
from vitalDSP.transforms.beats_transformation import RRTransformation
from vitalDSP.physiological_features.hrv_analysis import HRVFeatures
from vitalDSP.feature_engineering.morphology_features import PhysiologicalFeatureExtractor,\
    PreprocessConfig
from tqdm import tqdm
import datetime as dt
from vitalDSP.health_analysis.health_report_generator import HealthReportGenerator

SC_FILES_PATH = "../Data/df_data_path.csv"
EVENT_FILES_PATH = "../Data/events_prereshock-postfluid_2h_windows.csv"
# Signal processing parameters
fs = 100  # Sampling frequency
duration = 60 * 5  # Duration of each window in seconds (5 minutes)
step_size = fs * 30  # Step size (30 seconds)

# Directory to save the segmented data
SEGMENT_OUTPUT_DIR = "../Segmented_Data/Data"
FEATURE_OUTPUT_DIR = "../Feature_Data/Data"
EVENT_DATA_DIR = "../Event_Data"

df = pd.read_csv(SC_FILES_PATH)
df_event = pd.read_csv(EVENT_FILES_PATH)

def list_files(directory):
    file_list = []
    for entry in os.scandir(directory):
        if entry.is_file():
            file_list.append(entry.path)
        elif entry.is_dir():
            file_list.extend(list_files(entry.path))
    return file_list

feature_files = list_files(FEATURE_OUTPUT_DIR)

# row = df_event.iloc[10]
def join_event(row):
    subject_id = str(row['SUBJID']).strip()  # Make sure there's no extra whitespace

    substring = f'01NVa-003-{subject_id}'

    # Filter the list based on the substring presence, stripping whitespace for safety
    filtered_files = [feature_file for feature_file in feature_files 
                        if substring in feature_file.strip()]
    # print(f"Filtered files: {filtered_files}")
    event_start = dt.datetime.strptime(row['time_winstart'], '%Y-%m-%d %H:%M:%S') 
    event_end = dt.datetime.strptime(row['time_winstop'], '%Y-%m-%d %H:%M:%S') 
    # Format the datetime object to a string without special characters
    event_start_str = event_start.strftime('%Y%m%dT%H%M%S')
    event_end_str = event_end.strftime('%Y%m%dT%H%M%S')

    fname = f'01NVa-003-{subject_id}_{event_start_str}_{event_end_str}_features.csv'

    df_event_features=None

    for feature_file in filtered_files:
        # Extract file date from the filename (assumed format: '%Y%m%dT%H%M%S')
        file_date = dt.datetime.strptime(feature_file.split('/')[-1].split('_')[0], '%Y%m%dT%H%M%S')

        # Extract the start and end offsets (assumed to be in milliseconds, so we divide by 1000 to convert to seconds)
        start_offset_ms = int(feature_file.split('/')[-1].split('_')[1])
        end_offset_ms = int(feature_file.split('/')[-1].split('_')[2])

        # Convert milliseconds to seconds and add to file_date
        file_start = file_date + dt.timedelta(seconds=start_offset_ms/fs)
        file_end = file_date + dt.timedelta(seconds=end_offset_ms/fs)

        if event_start <= file_start and event_end >= file_end:
            if df_event_features is None:
                df_event_features = pd.read_csv(feature_file)
            else:
                df_event_features = pd.concat([df_event_features, pd.read_csv(feature_file)])
    if df_event_features is not None:
        df_event_features.to_csv(os.path.join(EVENT_DATA_DIR, fname), index=False)
        return fname
    return ""

if __name__ == "__main__":
    df_event['Join_Event'] = df_event.apply(join_event, axis=1)
    df_event.to_csv(os.path.join(EVENT_DATA_DIR, 'event.csv'), index=False)