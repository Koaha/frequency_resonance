# src/main.py
from pathlib import Path
import logging
from core.data_processor import DataProcessor
from config.settings import load_config, resolve_path


def setup_logging(log_path: Optional[Path] = None) -> None:
    """Configure logging"""
    cfg = load_config()
    default_log = resolve_path(cfg.get("output_dir", "output")) / "data_processing.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path or default_log)
        ]
    )

def main():
    """Main entry point"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        processor = DataProcessor()
        output_path = processor.convert_to_csv()
        logger.info(f"Processing completed successfully. Output: {output_path}")
        
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        raise

if __name__ == "__main__":
    # from core.data_processor import DataProcessor
    # processor = DataProcessor()
    # output_path = processor.convert_to_csv(batch_size=1000)
    main()