import numpy as np
import pandas as pd
import os
import datetime as dt
import concurrent.futures
from vitalDSP.signal_quality_assessment.signal_quality_index import SignalQualityIndex
from vitalDSP.transforms.beats_transformation import RRTransformation
from vitalDSP.physiological_features.hrv_analysis import HRVFeatures
from vitalDSP.feature_engineering.morphology_features import PhysiologicalFeatureExtractor,\
    PreprocessConfig
from tqdm import tqdm
from vitalDSP.notebooks import process_in_chunks

# Signal processing parameters
fs = 100  # Sampling frequency
duration = 60 * 5  # Duration of each window in seconds (5 minutes)
step_size = fs * 120  # Step size (30 seconds)
DATA_DIR = "src/RAW_DATA"
# Directory to save the segmented data
SEGMENT_OUTPUT_DIR = "src/output/Segmented_Data_24EI"
FEATURE_OUTPUT_DIR = "src/output/Feature_Data_24EI"

# Create the output directory if it doesn't exist
# os.makedirs(SEGMENT_OUTPUT_DIR, exist_ok=True)

def get_normal_segment(signal_col, date_col, segment_folder, rr_folder, feats_folder, file_path): 
    """
    Process a signal into normal segments and compute features for each segment.

    Parameters
    ----------
    signal_col : array_like
        The signal to be processed.
    date_col : array_like
        Timestamps corresponding to the signal.
    segment_folder : str
        Folder to save the segmented data.
    rr_folder : str
        Folder to save the RR intervals.
    feats_folder : str
        Folder to save the features.
    file_path : str
        The file path of the signal.

    Returns
    -------
    normal_signal : list
        List of normal segments of the signal.
    date_col_normal : list
        List of timestamps corresponding to the normal segments.
    """
    if not os.path.exists(segment_folder):
        os.makedirs(segment_folder,exist_ok=True)
    if not os.path.exists(rr_folder):
        os.makedirs(rr_folder,exist_ok=True)
    if not os.path.exists(feats_folder):
        os.makedirs(feats_folder,exist_ok=True)
    
    # Initialize Signal Quality Index
    sqi = SignalQualityIndex(signal_col)
    
    # Compute SQI and extract normal/abnormal segments
    sqi_values, normal_segments, abnormal_segments = sqi.signal_entropy_sqi(
        window_size=fs * duration, step_size=step_size, 
        threshold=-2, threshold_type='below'
    )

    # Prepare the normal segments along with corresponding timestamps
    normal_signal = []
    date_col_normal = []
    # rr_intervals = []
    # Initialize an empty DataFrame to store features
    # all_features_df = pd.DataFrame()
    
    file_path_col = []
    start_col = []
    end_col = []
    
    csv_file_name = (file_path.split('/')[-1]).split('.')[0]
    for start, end in tqdm(normal_segments):
        try:
            fname = f"{csv_file_name}_{start}_{end}.csv"
            rr_fname = f"{csv_file_name}_{start}_{end}_rr.txt"
            df_segment = pd.DataFrame({"TIMESTAMP_MS": date_col[start:end], "PLETH": signal_col[start:end]})
            df_segment.to_csv(os.path.join(segment_folder, fname), index=False)
            
            rr_transformation = RRTransformation(signal_col[start:end],fs=100, signal_type='ppg')
            rr_interval = rr_transformation.process_rr_intervals()*1000 # convert to ms
            
            hrv_features = HRVFeatures(signal_col[start:end], nn_intervals=rr_interval, fs=100, signal_type='ppg')
            hrv_feats = hrv_features.compute_all_features()
            
            preprocess_config = PreprocessConfig()
            extractor = PhysiologicalFeatureExtractor(signal_col[start:end], fs=100)
            morphology_feats = extractor.extract_features(signal_type="PPG", 
                                                        preprocess_config=preprocess_config)
            
            # Merge HRV and Morphology features
            combined_feats = {**hrv_feats, **morphology_feats}
            
            # Convert the merged dictionary to a DataFrame row
            combined_feats_df = pd.DataFrame([combined_feats])
            
            combined_feats_df['file_path'] = file_path
            combined_feats_df['start'] = start
            combined_feats_df['end'] = end
            combined_feats_df.to_csv(os.path.join(feats_folder, f'{csv_file_name}_{start}_{end}_features.csv'), index=False)
            
            # Append the new row to the overall DataFrame
            # all_features_df = pd.concat([all_features_df, combined_feats_df], ignore_index=True)
            
            file_path_col.append(file_path)
            start_col.append(start)
            end_col.append(end)
            
            # date_col_normal.append(date_col[start:end])
            # normal_signal.append(signal_col[start:end])
            
            # Save each segment to a CSV file
            
            np.savetxt(os.path.join(rr_folder, rr_fname), rr_interval)
        except Exception as e:
            print(f"Error processing segment {start} to {end}: {e}")
            continue
    
    # all_features_df['file_path'] = file_path_col
    # all_features_df['start'] = start_col
    # all_features_df['end'] = end_col
    # all_features_df.to_csv(os.path.join(feats_folder, f'{csv_file_name}_features.csv'), index=False)
    
    return normal_signal, date_col_normal

def segment_signal(row):
    """
    Process a single file and segment it into normal segments.

    Parameters
    ----------
    row : str
        The path to the file to be processed.

    Returns
    -------
    bool
        True if the file was processed successfully, False otherwise.
    """
    try:
        print(f"Processing file: {row}")
        
        file_path = row
        start_datetime = dt.datetime.strptime((file_path.split("/")[-1])[:-4], '%Y%m%dT%H%M%S.%f%z')
        
        df_ppg = pd.read_csv(file_path)
        
        # Extract signal and timestamp columns
        signal_col = np.array(df_ppg['PLETH'].values)
        timestamp_ms = np.array(df_ppg['TIMESTAMP_MS'].values)
        date_col = start_datetime + pd.to_timedelta(timestamp_ms, unit='ms')
        
        # signal_col, date_col = process_in_chunks(file_path,data_type='ppg', fs=fs)

        # Create a segment folder for the file
        folder = row.split('/')[7]
        segment_folder = os.path.join(SEGMENT_OUTPUT_DIR, folder, file_path.split('/')[2],'segments')
        rr_folder = os.path.join(SEGMENT_OUTPUT_DIR, folder, file_path.split('/')[2],'rr')
        feats_folder = os.path.join(FEATURE_OUTPUT_DIR, folder, file_path.split('/')[2],'features')
        
        # Process the signal into normal segments
        get_normal_segment(signal_col, date_col, segment_folder,rr_folder,feats_folder,file_path)
        
        print(f"Done processing file: {file_path}")
        return True
    except Exception as e:
        print(f"Error processing file {row}: {e}")
        return False

if __name__ == "__main__":
    # Process in batches of 10 files at a time, with 2 parallel workers
    # process_in_batches(df, batch_size=20, max_workers=4)
    rows = []
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),DATA_DIR)):
        for file_name in files:
            if 'csv' in file_name:
                rows.append(os.path.join(root, file_name))
    rows = np.sort(rows)
    for row in tqdm(rows):
        segment_signal(row)
    
    # process_concurrently(rows, num_workers=4)
    # segment_signal(rows[0])
    # print()

# def process_concurrently(rows, num_workers=2):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
#         # Submit the function for each row
#         futures = [executor.submit(segment_signal, row) for row in rows]

#         # Use tqdm to track progress as each future completes
#         for future in tqdm(concurrent.futures.as_completed(futures), total=len(rows)):
#             # Optionally handle results or exceptions if needed
#             try:
#                 future.result()  # This would raise an exception if one occurred
#             except Exception as e:
#                 print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     # Process in batches of 10 files at a time, with 2 parallel workers
#     # process_in_batches(df, batch_size=20, max_workers=4)
#     rows = []
#     for root, dirs, files in os.walk(DATA_DIR):
#         for file_name in files:
#             if 'csv' in file_name:
#                 rows.append(os.path.join(root, file_name))
    
#     process_concurrently(rows, num_workers=4)
#     # segment_signal(rows[0])
#     # print()