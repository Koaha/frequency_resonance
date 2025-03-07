# src/utils/helpers.py
from typing import Any, Optional
import logging
from pathlib import Path

# Custom exceptions
class SignalProcessingError(Exception):
    pass

class AnalysisError(Exception):
    pass

class ReportGenerationError(Exception):
    pass

def setup_logging(log_path: Optional[Path] = None) -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path or 'application.log')
        ]
    )