from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any
from .config import SignalConfig
from .file_list_processor import FileListProcessor

class SignalProcessingPipeline:
    """Main signal processing pipeline."""
    
    def __init__(self, config: SignalConfig):
        """Initialize the pipeline with configuration."""
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        if config.mode == "file_list":
            self.file_processor = FileListProcessor(config.file_list_path)
    
    def get_files_to_process(self) -> List[Dict[str, Any]]:
        """Get list of files to process based on configured mode."""
        if self.config.mode == "directory":
            # Process all files in directory
            files = []
            for file_path in self.config.data_dir.glob("**/*.csv"):
                files.append({
                    'path': file_path,
                    'patient_id': file_path.stem,  # Use filename as patient ID
                    'date': None  # Date not available in directory mode
                })
            return files
        else:
            # Process files from list
            return list(self.file_processor.get_file_paths())
    
    def process_file(self, file_info: Dict[str, Any]) -> None:
        """Process a single file."""
        try:
            file_path = file_info['path']
            patient_id = file_info['patient_id']
            date = file_info.get('date')
            
            self.logger.info(f"Processing file: {file_path} for patient {patient_id}")
            
            # TODO: Implement actual signal processing logic here
            # This is where you would call your existing processing functions
            # Example:
            # - Read the signal data
            # - Apply preprocessing
            # - Extract features
            # - Save results
            
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {e}")
            raise
    
    def process_files(self) -> None:
        """Process all files using configured number of workers."""
        files = self.get_files_to_process()
        self.logger.info(f"Found {len(files)} files to process")
        
        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            list(executor.map(self.process_file, files)) 