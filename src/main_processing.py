# src/main_processing.py
import logging
from pathlib import Path
from core.signal_processing import SignalProcessingPipeline, SignalConfig

def setup_logging(output_dir: Path) -> None:
    """Configure logging for the processing pipeline."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(output_dir / 'processing.log')
        ]
    )

def main():
    """Main entry point for signal processing pipeline."""
    config = SignalConfig()
    setup_logging(config.output_base)
    logger = logging.getLogger(__name__)
    
    try:
        pipeline = SignalProcessingPipeline(config)
        pipeline.process_files()
        logger.info("Processing completed successfully")
        
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise

if __name__ == "__main__":\
    # from core.signal_processing import SignalProcessingPipeline
    # # Initialize and run the pipeline
    # pipeline = SignalProcessingPipeline()
    # pipeline.process_files(max_workers=4)
    main()