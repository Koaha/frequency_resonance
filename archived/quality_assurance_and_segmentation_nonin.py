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
from vitalDSP.notebooks import process_in_chunks

# Signal processing parameters
fs = 75  # Sampling frequency
duration = 60 * 5  # Duration of each window in seconds (5 minutes)
step_size = fs * 30  # Step size (30 seconds)
DATA_DIR = "Nonin"
# Directory to save the segmented data
SEGMENT_OUTPUT_DIR = "Segmented_Data_Nonin"
FEATURE_OUTPUT_DIR = "Feature_Data_Nonin"

# Create the output directory if it doesn't exist
# os.makedirs(SEGMENT_OUTPUT_DIR, exist_ok=True)

def get_normal_segment(signal_col, date_col, segment_folder, rr_folder, feats_folder, file_path): 
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
    try:
        print(f"Processing file: {row}")
        
        file_path = row
        # df_ppg = pd.read_csv(file_path)
        signal_col, date_col = process_in_chunks(file_path,data_type='ppg', fs=fs)

        # Create a segment folder for the file
        segment_folder = os.path.join(SEGMENT_OUTPUT_DIR, file_path.split('/')[1],'segments')
        rr_folder = os.path.join(SEGMENT_OUTPUT_DIR, file_path.split('/')[1],'rr')
        feats_folder = os.path.join(FEATURE_OUTPUT_DIR, file_path.split('/')[1],'features')
        
        # Process the signal into normal segments
        get_normal_segment(signal_col, date_col, segment_folder,rr_folder,feats_folder,file_path)
        
        print(f"Done processing file: {file_path}")
        return True
    except Exception as e:
        print(f"Error processing file {row}: {e}")
        return False

def process_concurrently(rows, num_workers=2):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        # Submit the function for each row
        futures = [executor.submit(segment_signal, row) for row in rows]

        # Use tqdm to track progress as each future completes
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(rows)):
            # Optionally handle results or exceptions if needed
            try:
                future.result()  # This would raise an exception if one occurred
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Process in batches of 10 files at a time, with 2 parallel workers
    # process_in_batches(df, batch_size=20, max_workers=4)
    rows = []
    done_files = os.listdir(SEGMENT_OUTPUT_DIR)
    for root, dirs, files in os.walk(DATA_DIR):
        for file_name in files:
            if ('csv' in file_name):
                rows.append(os.path.join(root, file_name))
    final_list = []
    for row in rows:
        patient_id = row.split("/")[1]
        if patient_id not in done_files:
            final_list.append(row)
    
    # print(len(rows))
    # print(len(final_list))
    
    process_concurrently(final_list, num_workers=4)
    # segment_signal(rows[0])