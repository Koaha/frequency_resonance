# src/core/data_processor/file_handler.py
from pathlib import Path
from typing import Optional
import logging

class FileHandler:
    """Handle file operations"""
    
    def __init__(self, adult_path: Path, child_path: Path):
        self.adult_path = adult_path
        self.child_path = child_path
        self.logger = logging.getLogger(__name__)

    def find_file_path(self, patient_id: str, file_name: str) -> Optional[Path]:
        """Find file in Adults or Children directories"""
        # Check Adults directory
        adult_path = self.adult_path / patient_id / "PPG" / file_name
        if adult_path.exists():
            return adult_path

        # Search Children directory recursively
        child_base = self.child_path / patient_id / "PPG"
        if child_base.exists():
            for path in child_base.rglob(file_name):
                return path

        return None