# src/core/data_processor/batch_processor.py
from typing import List, Dict
import concurrent.futures
from .line_processor import LineProcessor

class BatchProcessor:
    """Process data in batches"""
    
    def __init__(self, line_processor: LineProcessor):
        self.line_processor = line_processor

    def process_batch(self, lines: List[str]) -> List[Dict]:
        """Process a batch of lines in parallel"""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(self.line_processor.process_line, lines))
        return [item for sublist in results for item in sublist]