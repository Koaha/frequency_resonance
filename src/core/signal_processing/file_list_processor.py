import pandas as pd
from pathlib import Path
from typing import List, Generator
import logging

class FileListProcessor:
    """Process files from a CSV list."""
    
    def __init__(self, file_list_path: Path):
        """Initialize the file list processor.
        
        Args:
            file_list_path: Path to CSV file containing list of files to process
                          CSV should have columns: [patientid, date, path]
        """
        self.file_list_path = file_list_path
        self.logger = logging.getLogger(__name__)
        
    def get_file_paths(self) -> Generator[Path, None, None]:
        """Read file paths from CSV and yield them one at a time."""
        try:
            df = pd.read_csv(self.file_list_path)
            required_columns = ['patientid', 'date', 'path']
            
            # Verify required columns exist
            if not all(col in df.columns for col in required_columns):
                missing = [col for col in required_columns if col not in df.columns]
                raise ValueError(f"Missing required columns in CSV: {missing}")
            
            # Convert paths to Path objects and verify they exist
            for _, row in df.iterrows():
                file_path = Path(row['path'])
                if not file_path.exists():
                    self.logger.warning(f"File not found: {file_path}")
                    continue
                    
                yield {
                    'path': file_path,
                    'patient_id': row['patientid'],
                    'date': row['date']
                }
                
        except Exception as e:
            self.logger.error(f"Error reading file list: {e}")
            raise 