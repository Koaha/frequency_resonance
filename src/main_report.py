# src/main_report.py
import logging
from pathlib import Path
import pandas as pd
from reports import ReportGenerator, ReportConfig
from core.resonance.data_manager import DataManager
from core.resonance.config import ResonanceConfig
from config.settings import load_config, resolve_path
import os
import datetime as dt


def setup_logging() -> None:
    """Configure logging for report generation."""
    cfg = load_config()
    log_dir = resolve_path(cfg.get("output_dir", "output")) / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_dir / 'report_generation.log')
        ]
    )

def _get_date_from_file(file_path: str) -> dt.date:
    """Extract date from file path."""
    try:
        # Extract timestamp from file path (e.g., 20200831T141058.802+0700)
        timestamp = Path(file_path).stem.split('_')[0]
        # Parse the timestamp
        date = dt.datetime.strptime(timestamp, '%Y%m%dT%H%M%S.%f%z').date()
        return date
    except Exception as e:
        logging.error(f"Error parsing date from file {file_path}: {e}")
        raise

def compile_feature_data(data_manager: DataManager) -> pd.DataFrame:
    """Compile feature data from all processed files."""
    logger = logging.getLogger(__name__)
    
    # Load all patient files
    df_patients = data_manager.load_patient_files()
    
    feature_data = []
    
    # Process each patient's data
    for patient_id in df_patients['patient_id'].unique():
        try:
            # Get patient's data
            df_patient = df_patients[df_patients['patient_id'] == patient_id]
            
            # Process patient data
            patient_data = data_manager.process_patient_data(df_patient, patient_id)
            
            # Read feature files for this patient
            patient_features = df_patient['feature_path'].unique()
            for feature_file in patient_features:
                try:
                    df_features = pd.read_csv(feature_file)
                    
                    # Add patient metadata
                    df_features['patient_id'] = patient_id
                    df_features['day1_date'] = patient_data.day1_date
                    df_features['day_date'] = _get_date_from_file(feature_file)
                    
                    feature_data.append(df_features)
                    
                except Exception as e:
                    logger.warning(f"Error reading feature file {feature_file}: {e}")
                    continue
                    
        except Exception as e:
            logger.warning(f"Error processing patient {patient_id}: {e}")
            continue
    
    # Combine all feature data
    if feature_data:
        return pd.concat(feature_data, ignore_index=True)
    else:
        raise ValueError("No feature data found to process")

def prepare_data():
    """Main entry point for report generation.
    
    This function coordinates the overall report generation process,
    including loading feature data and initiating report generation.
    """
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize configurations
        resonance_config = ResonanceConfig()
        # report_config = ReportConfig()
        
        # Load event data
        # event_path = config.event_dir / 'event.csv'
        # df_event = pd.read_csv(event_path)
        # Initialize data manager
        data_manager = DataManager(resonance_config)
        
        # Compile feature data
        logger.info("Compiling feature data...")
        df_features = compile_feature_data(data_manager)
        df_features.to_csv("compile_feature_data.csv")
        # Generate reports
        # generator = ReportGenerator(config)
        # generator.generate_reports(df_event)
        # logger.info("Generating reports...")
        # generator = ReportGenerator(report_config)
        # generator.generate_reports(df_features)
        
        # logger.info("Report generation completed successfully")
        
    except Exception as e:
        logger.error(f"Report generation failed: {str(e)}")
        raise

def main():
    """Main entry point for report generation.
    
    This function coordinates the overall report generation process,
    including loading feature data and initiating report generation.
    """
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize configurations
        # resonance_config = ResonanceConfig()
        report_config = ReportConfig()
        
        # Load event data
        # event_path = config.event_dir / 'event.csv'
        # df_event = pd.read_csv(event_path)
        # Initialize data manager
        # data_manager = DataManager(resonance_config)
        
        # # Compile feature data
        # logger.info("Compiling feature data...")
        # df_features = compile_feature_data(data_manager)
        # df_features.to_csv("compile_feature_data.csv")
        
        if not os.path.exists("compile_feature_data.csv"):
            prepare_data()
            
        df_features = pd.read_csv("compile_feature_data.csv")
        
        # Generate reports
        # generator = ReportGenerator(config)
        # generator.generate_reports(df_event)
        logger.info("Generating reports...")
        generator = ReportGenerator(report_config)
        generator.generate_reports(df_features)
        
        logger.info("Report generation completed successfully")
            
    except Exception as e:
        logger.error(f"Report generation failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 
    # from reports import ReportGenerator
    # import pandas as pd

    # # Load event data
    # df_event = pd.read_csv('path/to/event.csv')

    # # Generate reports
    # generator = ReportGenerator()
    # generator.generate_reports(df_event, max_workers=6)
    main()