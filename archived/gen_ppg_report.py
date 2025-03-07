import numpy as np
import pandas as pd
import os
import logging
import concurrent.futures
import warnings
from multiprocessing import Queue, Process
from tqdm import tqdm
from vitalDSP.health_analysis.health_report_generator import HealthReportGenerator

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Setup logging to capture any errors
logging.basicConfig(filename="report_generation.log", level=logging.ERROR)

# Signal processing parameters
fs = 100  # Sampling frequency
duration = 60 * 5  # Duration of each window in seconds (5 minutes)
step_size = fs * 120  # Step size (120 seconds)
report_duration = 30 * 60  # Duration of the report in seconds
report_segment = int(report_duration // (step_size / fs))  # Number of segments in the report

# Directory to save the segmented data
BASE_WORK_DIR = "/media/data/Workspace/24EIa/src/output"
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
    df_event_feature = join_event(chunk)
    df_event_feature['start'] = df_event_feature['start'].astype(int)
    df_event_feature = df_event_feature.sort_values(by='start')
    n = 3
    selected_columns_df = df_event_feature.iloc[:, :-n]
    selected_columns_df = selected_columns_df.astype(float)
    feature_data = selected_columns_df.to_dict(orient='list')
    return feature_data

def process_data(chunk, fname):
    try:
        feature_data = prepare_report_data(chunk)
        return (fname, feature_data)
    except Exception as e:
        logging.error(f"Error processing {fname}: {str(e)}", exc_info=True)
        return None

def generate_plots_worker(fname, feature_data):
    """
    Generate the plots in parallel.
    """
    try:
        report_generator = HealthReportGenerator(feature_data=feature_data, segment_duration="5_min")
        report_dir = os.path.join(BASE_WORK_DIR, "reports", fname.split('_')[0], fname.split('.')[0])
        image_dir = os.path.join("visualizations")
        os.makedirs(os.path.join(report_dir, image_dir), exist_ok=True)
        os.chdir(report_dir)
        report_html = report_generator.generate(output_dir=image_dir)
        with open('report.html', 'w', encoding='utf-8') as f:
            f.write(report_html)
    except Exception as e:
        logging.error(f"Error generating report {fname}: {str(e)}", exc_info=True)
    finally:
        os.chdir(BASE_WORK_DIR)

def plot_worker(result_queue):
    """
    Worker function to handle plotting in a separate process.
    """
    while True:
        task = result_queue.get()
        if task is None:
            break
        fname, feature_data = task
        generate_plots_worker(fname, feature_data)

# Main execution
if __name__ == "__main__":
    df = get_df(FEATURE_OUTPUT_DIR)
    grouped = df.groupby(['patient_id', 'file_id'])
    result_queue = Queue()

    # Start the plotting process
    plot_process = Process(target=plot_worker, args=(result_queue,))
    plot_process.start()

    # Step 1: Process data in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_chunk = {}
        for index, ((patient_id, event_id), group) in enumerate(tqdm(grouped)):
            if index < 10:  # Skip 
                continue
            for i in range(0, len(group), report_segment):
                chunk = group.iloc[i:i + report_segment]
                if len(chunk) > 0:
                    fname = f"{patient_id}_{event_id}_{i}.csv"
                    future = executor.submit(process_data, chunk, fname)
                    future_to_chunk[future] = fname

        for future in tqdm(concurrent.futures.as_completed(future_to_chunk)):
            try:
                result = future.result()
                if result:
                    result_queue.put(result)
            except Exception as e:
                logging.error(f"Error in processing data: {str(e)}", exc_info=True)

    # Stop the plotting process
    result_queue.put(None)
    plot_process.join()
