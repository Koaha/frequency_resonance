# src/reports/report_generator.py
from typing import Optional, List
from pathlib import Path
import os
import logging
import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from vitalDSP.health_analysis.health_report_generator import HealthReportGenerator
from .config import ReportConfig
from .feature_processor import FeatureProcessor
import datetime as dt

class Report:
    """Handle individual report generation.
    
    This class manages the generation of a single report, including
    feature processing and HTML generation.
    """
    
    def __init__(self, feature_data: pd.DataFrame, config: ReportConfig):
        """
        Args:
            feature_data (pd.DataFrame): Feature data for report generation
            config (ReportConfig): Configuration settings
        """
        self.feature_data = feature_data
        self.config = config
        self.feature_processor = FeatureProcessor()
        self.logger = logging.getLogger(__name__)

    def _get_date_from_file(self, file_path: str) -> dt.date:
        """Extract date from file path."""
        try:
            # Extract timestamp from file path (e.g., 20200831T141058.802+0700)
            timestamp = Path(file_path).stem.split('_')[0]
            # Parse the timestamp
            date = dt.datetime.strptime(timestamp, '%Y%m%dT%H%M%S.%f%z').date()
            return date
        except Exception as e:
            self.logger.error(f"Error parsing date from file {file_path}: {e}")
            raise

    def generate(self) -> Optional[Path]:
        """Generate a single report.
        
        Returns:
            Optional[Path]: Path to generated report, None if generation fails
            
        Raises:
            Exception: If report generation fails
        """
        try:
            # Get patient ID and date from file path
            patient_id = self.feature_data['patient_id'].iloc[0]
            file_path = self.feature_data['file_path'].iloc[0]
            date = self._get_date_from_file(file_path)
            
            # Prepare paths
            report_base_dir = self.config.event_dir / "reports" / patient_id / date.strftime('%Y-%m-%d')
            image_dir = report_base_dir / "visualizations"
            
            # Create directories
            image_dir.mkdir(parents=True, exist_ok=True)

            # Process features
            feature_dict = self.feature_processor.prepare_features(self.feature_data)

            # Generate report
            report_generator = HealthReportGenerator(
                feature_data=feature_dict,
                segment_duration="5_min"
            )

            # Change to report directory
            original_dir = Path.cwd()
            os.chdir(report_base_dir)

            try:
                # Generate HTML report
                report_html = report_generator.generate(output_dir='visualizations')
                report_path = report_base_dir / 'report.html'
                
                with open(report_path, 'w', encoding='utf-8') as f:
                    f.write(report_html)
                
                return report_path

            finally:
                # Ensure we return to original directory
                os.chdir(original_dir)

        except Exception as e:
            self.logger.error(f"Error generating report for patient {patient_id}: {str(e)}")
            return None

class ReportGenerator:
    """Manage batch report generation.
    
    This class coordinates the generation of multiple reports,
    handling parallel processing and error management.
    """
    
    def __init__(self, config: ReportConfig = ReportConfig()):
        """
        Args:
            config (ReportConfig): Configuration settings
        """
        self.config = config
        self.logger = logging.getLogger(__name__)

    def generate_reports(self, df_features: pd.DataFrame, max_workers: int = 6) -> List[Optional[Path]]:
        """Generate reports for multiple patients in parallel.
        
        Args:
            df_features (pd.DataFrame): Feature data for all reports
            max_workers (int): Maximum number of parallel workers
            
        Returns:
            List[Optional[Path]]: List of paths to generated reports, with None for failed generations
            
        Raises:
            Exception: If batch report generation fails
        """
        try:
            # Group data by patient_id and file_path (which contains the date)
            grouped_data = df_features.groupby(['patient_id', 'file_path'])
            report_paths = []
            
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                # Create generator for all reports
                future_to_group = {
                    executor.submit(Report(group, self.config).generate): (patient_id, file_path)
                    for (patient_id, file_path), group in grouped_data
                }
                
                # Process reports with progress bar and collect results
                for future in tqdm(as_completed(future_to_group), total=len(future_to_group)):
                    patient_id, file_path = future_to_group[future]
                    try:
                        report_path = future.result()
                        if report_path:
                            report_paths.append(report_path)
                            self.logger.info(f"Successfully generated report for patient {patient_id} from {file_path}")
                        else:
                            self.logger.warning(f"Failed to generate report for patient {patient_id} from {file_path}")
                    except Exception as e:
                        self.logger.error(f"Error processing report for patient {patient_id} from {file_path}: {str(e)}")
                        report_paths.append(None)

            return report_paths

        except Exception as e:
            self.logger.error(f"Error in batch report generation: {str(e)}")
            raise