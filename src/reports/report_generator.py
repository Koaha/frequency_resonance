# src/reports/report_generator.py
from typing import Optional
from pathlib import Path
import os
import logging
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
from vitalDSP.health_analysis.health_report_generator import HealthReportGenerator
from .config import ReportConfig
from .feature_processor import FeatureProcessor

class Report:
    """Handle individual report generation.
    
    This class manages the generation of a single report, including
    feature processing and HTML generation.
    """
    
    def __init__(self, event_data: pd.Series, config: ReportConfig):
        """
        Args:
            event_data (pd.Series): Event data for report generation
            config (ReportConfig): Configuration settings
        """
        self.event_data = event_data
        self.config = config
        self.feature_processor = FeatureProcessor()
        self.logger = logging.getLogger(__name__)

    def generate(self) -> Optional[Path]:
        """Generate a single report.
        
        Returns:
            Optional[Path]: Path to generated report, None if generation fails
            
        Raises:
            Exception: If report generation fails
        """
        try:
            fname = self.event_data['Join_Event']
            if not fname:
                return None

            # Prepare paths
            feature_path = self.config.event_dir / 'events' / fname
            report_base_dir = self.config.event_dir / "reports" / fname.split('.')[0]
            image_dir = report_base_dir / "visualizations"
            
            # Create directories
            image_dir.mkdir(parents=True, exist_ok=True)

            # Process features
            df_event_feature = pd.read_csv(feature_path)
            feature_data = self.feature_processor.prepare_features(df_event_feature)

            # Generate report
            report_generator = HealthReportGenerator(
                feature_data=feature_data,
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
            self.logger.error(f"Error generating report for {self.event_data['Join_Event']}: {str(e)}")
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

    def generate_reports(self, df_event: pd.DataFrame, max_workers: int = 6) -> None:
        """Generate reports for multiple events in parallel.
        
        Args:
            df_event (pd.DataFrame): Event data for all reports
            max_workers (int): Maximum number of parallel workers
            
        Raises:
            Exception: If batch report generation fails
        """
        try:
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                # Create generator for all reports
                report_futures = [
                    executor.submit(Report(row, self.config).generate)
                    for _, row in df_event.iterrows()
                ]
                
                # Process reports with progress bar
                for _ in tqdm(report_futures, total=len(df_event)):
                    pass

        except Exception as e:
            self.logger.error(f"Error in batch report generation: {str(e)}")
            raise