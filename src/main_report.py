# src/main_report.py
import logging
from pathlib import Path
import pandas as pd
from reports import ReportGenerator, ReportConfig
from config.settings import paths

def setup_logging() -> None:
    """Configure logging for report generation."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(paths.OUTPUT_DIR / 'report_generation.log')
        ]
    )

def main():
    """Main entry point for report generation.
    
    This function coordinates the overall report generation process,
    including loading event data and initiating batch processing.
    """
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize configuration
        config = ReportConfig()
        
        # Load event data
        event_path = config.event_dir / 'event.csv'
        df_event = pd.read_csv(event_path)
        
        # Generate reports
        generator = ReportGenerator(config)
        generator.generate_reports(df_event)
        
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