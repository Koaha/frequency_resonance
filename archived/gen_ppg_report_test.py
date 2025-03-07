import numpy as np
import pandas as pd
import os
import logging
from tqdm import tqdm
from vitalDSP.health_analysis.health_report_generator import HealthReportGenerator
import argparse
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
# Setup logging to capture any errors
logging.basicConfig(filename="report_generation.log", level=logging.ERROR)
logging.disable(logging.ERROR)

# Signal processing parameters
fs = 100  # Sampling frequency
duration = 60 * 5  # Duration of each window in seconds (5 minutes)
step_size = fs * 120  # Step size (120 seconds)
report_duration = 30 * 60  # Duration of the report in seconds
report_segment = int(report_duration // (step_size / fs))  # Number of segments in the report

# Directory to save the segmented data
BASE_WORK_DIR = "src/output"
FEATURE_OUTPUT_DIR = "src/output/Feature_Data_24EI"

# Helper functions
def list_files(directory):
    file_list = []
    for entry in os.scandir(directory):
        if entry.is_file():
            file_list.append(entry.path)
        elif entry.is_dir():
            file_list.extend(list_files(entry.path))
    return file_list

def get_df(directory):
    file_list = list_files(directory)
    df = pd.DataFrame(columns=['path'], data=np.sort(file_list))
    df['patient_id'] = df['path'].apply(lambda x: x.split('/')[3])
    df['file_id'] = df['path'].apply(lambda x: x.split('/')[-1].split('_')[0])
    df['start'] = df['path'].apply(lambda x: x.split('/')[-1].split('_')[1])
    df['end'] = df['path'].apply(lambda x: x.split('/')[-1].split('_')[2].split('.')[0])
    return df

def join_event(chunk):
    df_event_features = None
    for feature_file in chunk['path'].values:
        if df_event_features is None:
            df_event_features = pd.read_csv(feature_file)
        else:
            df_event_features = pd.concat([df_event_features, pd.read_csv(feature_file)])
    return df_event_features

def prepare_report_data(chunk):
    """
    Prepare data needed for report generation.
    """
    df_event_feature = join_event(chunk)
    df_event_feature['start'] = df_event_feature['start'].astype(int)
    df_event_feature = df_event_feature.sort_values(by='start')

    # Select all rows and columns from the beginning to the last n-3 columns
    n = 3
    selected_columns_df = df_event_feature.iloc[:, :-n]
    selected_columns_df = selected_columns_df.astype(float)

    feature_data = selected_columns_df.to_dict(orient='list')
    return feature_data

def generate_report_data(chunk, fname):
    """
    Handle the report generation (excluding plots).
    """
    try:
        feature_data = prepare_report_data(chunk)
        return (fname, feature_data)  # Return the data to be used for plotting
    except Exception as e:
        logging.error(f"Error processing {fname}: {str(e)}", exc_info=True)
        return None

def generate_plots(fname, feature_data):
    """
    Generate the plots using the gathered data.
    """
    try:
        report_generator = HealthReportGenerator(feature_data=feature_data, segment_duration="5_min")
        report_dir = os.path.join(BASE_WORK_DIR, "reports", fname.split('_')[0], fname.split('.')[0])
        image_dir = os.path.join("visualizations")

        # Make sure the directory exists
        os.makedirs(os.path.join(report_dir, image_dir), exist_ok=True)
        os.chdir(report_dir)

        # Generate the report and visualizations
        report_html = report_generator.generate(output_dir=image_dir)
        with open('report.html', 'w', encoding='utf-8') as f:
            f.write(report_html)
    except Exception as e:
        logging.error(f"Error generating report {fname}: {str(e)}", exc_info=True)
    finally:
        # Change back to the base working directory after processing
        os.chdir("/media/data/Workspace/24EIa")

# Main execution
# if __name__ == "__main__":
#     df = get_df(FEATURE_OUTPUT_DIR)
#     grouped = df.groupby(['patient_id', 'file_id'])

#     # Sequential processing for debugging
#     for index, ((patient_id, event_id), group) in enumerate(tqdm(grouped)):
#         if index < 10:  # Skip 
#             continue
#         for i in range(0, len(group), report_segment):
#             chunk = group.iloc[i:i + report_segment]
#             if len(chunk) > 0:
#                 fname = f"{patient_id}_{event_id}_{i}.csv"
#                 result = generate_report_data(chunk, fname)
#                 if result:
#                     fname, feature_data = result
#                     generate_plots(fname, feature_data)

def main(start_batch, end_batch):
    df = get_df(FEATURE_OUTPUT_DIR)
    grouped = df.groupby(['patient_id', 'file_id'])

    # Sequential processing for debugging
    for index, ((patient_id, event_id), group) in enumerate(tqdm(grouped)):
        # if index < start_batch or index >= end_batch:  # Skip batches outside the specified range
        if index < start_batch:  # Skip batches outside the specified range
            continue
        for i in range(0, len(group), report_segment):
            chunk = group.iloc[i:i + report_segment]
            if len(chunk) > 0:
                fname = f"{patient_id}_{event_id}_{i}.csv"
                result = generate_report_data(chunk, fname)
                if result:
                    fname, feature_data = result
                    generate_plots(fname, feature_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process data in batches.")
    parser.add_argument(
        "--start_batch", type=int, required=True, help="The starting batch index (inclusive)."
    )
    parser.add_argument(
        "--end_batch", type=int, required=True, help="The ending batch index (exclusive)."
    )
    args = parser.parse_args()

    main(args.start_batch, args.end_batch)