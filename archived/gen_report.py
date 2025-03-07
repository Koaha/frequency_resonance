import numpy as np
import pandas as pd
import os
import concurrent.futures
import matplotlib
from tqdm import tqdm
import datetime as dt
from vitalDSP.health_analysis.health_report_generator import HealthReportGenerator
from vitalDSP.signal_quality_assessment.signal_quality_index import SignalQualityIndex
from vitalDSP.transforms.beats_transformation import RRTransformation
from vitalDSP.physiological_features.hrv_analysis import HRVFeatures
from vitalDSP.feature_engineering.morphology_features import PhysiologicalFeatureExtractor, PreprocessConfig

# Use non-interactive backend for matplotlib
matplotlib.use('Agg')

# SC_FILES_PATH = "../Data/df_data_path.csv"
# EVENT_FILES_PATH = "../Data/events_prereshock-postfluid_2h_windows.csv"

# Signal processing parameters
fs = 100  # Sampling frequency
duration = 60 * 5  # Duration of each window in seconds (5 minutes)
step_size = fs * 120  # Step size (30 seconds)

# Base working directory to reset after each task
BASE_WORK_DIR = "src/RAW_DATA"

os.chdir(BASE_WORK_DIR)
SEGMENT_OUTPUT_DIR = "src/output/Segmented_Data_24EI"
FEATURE_OUTPUT_DIR = "src/output/Feature_Data_24EI"
# EVENT_DATA_DIR = "../Event_Data"

# df_event = pd.read_csv(os.path.join(EVENT_DATA_DIR, 'event.csv'))

def gen_report(row):
    try:
        fname = row['Join_Event']
        if fname != '':
            df_event_feature = pd.read_csv(os.path.join(EVENT_DATA_DIR, 'events', fname))
            df_event_feature['start'] = df_event_feature['start'].astype(int)
            df_event_feature = df_event_feature.sort_values(by='start')

            # Select all rows and columns from the beginning to the last n-3 columns
            n = 3
            selected_columns_df = df_event_feature.iloc[:, :-n]
            selected_columns_df = selected_columns_df.astype(float)

            # Convert the selected columns to a dictionary
            feature_data = selected_columns_df.to_dict(orient='list')
            report_generator = HealthReportGenerator(
                feature_data=feature_data, segment_duration="5_min"
            )

            image_dir = os.path.join(EVENT_DATA_DIR, "reports", fname.split('.')[0], "visualizations")
            os.makedirs(image_dir, exist_ok=True)

            # Change to the report directory for generating and saving the report
            report_dir = os.path.join(EVENT_DATA_DIR, "reports", fname.split('.')[0])
            os.chdir(report_dir)
            
            # Generate the report (HTML)
            report_html = report_generator.generate(output_dir='visualizations')
            with open('report.html', 'w', encoding='utf-8') as f:
                f.write(report_html)

    except Exception as e:
        print(f"Error processing {row['Join_Event']}: {e}")
    
    finally:
        # Ensure we return to the base working directory after report generation
        os.chdir(BASE_WORK_DIR)

def process_reports_concurrently(df_event, max_workers=6):
    # Process reports concurrently using a process pool
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(tqdm(executor.map(gen_report, [row for _, row in df_event.iterrows()]), total=len(df_event)))

if __name__ == "__main__":
    # Process all reports concurrently using multiprocessing
    process_reports_concurrently(df_event)
    # gen_report(df_event.iloc[3])
