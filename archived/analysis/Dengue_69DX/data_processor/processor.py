# src/core/data_processor/processor.py
from typing import Optional
from pathlib import Path
import logging
import pandas as pd
from .config import DataPaths
from .file_handler import FileHandler
from .line_processor import LineProcessor
from .batch_processor import BatchProcessor
from ...utils.helpers import ProcessingError

class DataProcessor:
    """Main data processing coordinator"""
    
    def __init__(self, config: DataPaths = DataPaths()):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self._validate_paths()
        
        self.file_handler = FileHandler(config.ADULT_PATH, config.CHILD_PATH)
        self.line_processor = LineProcessor(self.file_handler)
        self.batch_processor = BatchProcessor(self.line_processor)

    def _validate_paths(self) -> None:
        """Validate existence of required paths"""
        for path_name, path in vars(self.config).items():
            if not path.exists():
                raise ProcessingError(f"Required path does not exist: {path_name} - {path}")

    def convert_to_csv(self, batch_size: int = 1000) -> Path:
        """Convert input data to CSV format"""
        try:
            self.logger.info("Starting data conversion process")
            
            df_columns = ['patient_id', 'file', 'start', 'end', 'duration', 'file_path']
            all_results = self._process_file(batch_size)
            
            # Convert results to DataFrame and save
            df = pd.DataFrame(all_results, columns=df_columns)
            df.to_csv(self.config.OUTPUT_PATH, index=False)
            
            self.logger.info(f"Data conversion completed. Output saved to {self.config.OUTPUT_PATH}")
            return self.config.OUTPUT_PATH
            
        except Exception as e:
            self.logger.error(f"Error in data conversion: {str(e)}")
            raise ProcessingError(f"Data conversion failed: {str(e)}")

    def _process_file(self, batch_size: int) -> List[Dict]:
        """Process input file in batches"""
        all_results = []
        
        with open(self.config.SC_INSTRUCTION_PATH, 'r') as infile:
            batch = []
            
            for line in infile:
                batch.append(line)
                
                if len(batch) >= batch_size:
                    results = self.batch_processor.process_batch(batch)
                    all_results.extend(results)
                    batch = []
            
            # Process remaining lines
            if batch:
                results = self.batch_processor.process_batch(batch)
                all_results.extend(results)
                
        return all_results