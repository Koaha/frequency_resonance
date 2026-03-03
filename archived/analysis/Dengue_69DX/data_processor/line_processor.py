# src/core/data_processor/line_processor.py
from typing import Dict, List, Optional
import logging
from pathlib import Path
from .file_handler import FileHandler

class LineProcessor:
    """Process individual data lines"""
    
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler
        self.logger = logging.getLogger(__name__)

    def process_line(self, line: str) -> List[Dict]:
        """Process a single line of data"""
        try:
            data = line.strip().split(',')
            patient_id = data[0]
            results = []
            
            i = 1
            while i + 3 < len(data):
                if not data[i]:
                    break
                    
                result = self._process_segment(patient_id, data[i:i+4])
                if result:
                    results.append(result)
                i += 4
                
            return results
            
        except Exception as e:
            self.logger.error(f"Error processing line: {line.strip()} - {str(e)}")
            return []

    def _process_segment(self, patient_id: str, segment: List[str]) -> Optional[Dict]:
        """Process a single data segment"""
        file_name, start, end, duration = segment
        
        file_path = self.file_handler.find_file_path(patient_id, file_name)
        if file_path:
            return {
                'patient_id': patient_id,
                'file': file_name,
                'start': start,
                'end': end,
                'duration': duration,
                'file_path': str(file_path)
            }
        else:
            self.logger.warning(f"File not found: {file_name} for patient {patient_id}")
            return None