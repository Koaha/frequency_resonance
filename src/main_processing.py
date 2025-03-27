# src/main_processing.py
import logging
import argparse
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

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Signal processing pipeline')
    parser.add_argument('--mode', type=str, choices=['directory', 'file_list'], 
                       default='directory', help='Processing mode')
    parser.add_argument('--file-list', type=str, help='Path to CSV file containing list of files to process')
    parser.add_argument('--data-dir', type=str, help='Directory containing data files to process')
    parser.add_argument('--output-dir', type=str, help='Output directory for processed files')
    return parser.parse_args()

def main():
    """Main entry point for signal processing pipeline."""
    args = parse_args()
    
    # Configure pipeline based on arguments
    config = SignalConfig()
    config.mode = args.mode
    
    if args.output_dir:
        config.output_base = Path(args.output_dir)
    
    if args.mode == 'directory' and args.data_dir:
        config.data_dir = Path(args.data_dir)
    elif args.mode == 'file_list':
        if not args.file_list:
            raise ValueError("--file-list must be provided when mode is 'file_list'")
        config.file_list_path = Path(args.file_list)
    
    setup_logging(config.output_base)
    logger = logging.getLogger(__name__)
    
    try:
        pipeline = SignalProcessingPipeline(config)
        pipeline.process_files()
        logger.info("Processing completed successfully")
        
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise

if __name__ == "__main__":
    # Directory mode (default)
    # python src/main_processing.py --mode directory --data-dir /path/to/data --output-dir /path/to/output
    # File list mode
    # python src/main_processing.py --mode file_list --file-list /path/to/file_list.csv --output-dir /path/to/output
    main()