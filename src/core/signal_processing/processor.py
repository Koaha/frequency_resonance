# src/core/signal_processing/processor.py
from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from typing import List, Dict
from .config import SignalConfig
from .signal_processor import SignalProcessor
from .segment_handler import SegmentHandler

class SignalProcessingPipeline:
    """Coordinates the entire signal processing pipeline."""
    
    def __init__(self, config: SignalConfig = SignalConfig()):
        self.config = config
        self.signal_processor = SignalProcessor(config)
        self.segment_handler = SegmentHandler(config)
        self.logger = logging.getLogger(__name__)

    def process_file(self, file_path: Path) -> bool:
        """Process a single file through the pipeline."""
        try:
            # Load signal
            signal_data = self.signal_processor.load_signal(file_path)
            
            # Get quality segments
            _, normal_segments = self.signal_processor.get_quality_segments(
                signal_data.signal
            )
            
            # Prepare output directories
            output_dirs = self._prepare_output_dirs(file_path)
            
            # Process segments
            for start, end in normal_segments:
                self.segment_handler.process_segment(
                    signal_data,
                    start,
                    end,
                    output_dirs
                )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {e}")
            return False

    def process_files(self, max_workers: int = 4) -> None:
        """Process all files in the data directory."""
        files = list(self.config.data_dir.rglob("*.csv"))
        files.sort()
        
        for file_path in tqdm(files):
            self.process_file(file_path)

    def _prepare_output_dirs(self, file_path: Path) -> Dict[str, Path]:
        """Prepare output directories for a file."""
        folder = file_path.parent.name
        patient_id = file_path.parents[2].name
        base_dirs = {
            'segments': self.config.segment_dir / patient_id / 'data' /  'segments',
            'rr': self.config.segment_dir / patient_id / 'data' / 'rr',
            'features': self.config.feature_dir / patient_id / 'data' / 'features'
        }
        
        for dir_path in base_dirs.values():
            dir_path.mkdir(parents=True, exist_ok=True)
            
        return base_dirs