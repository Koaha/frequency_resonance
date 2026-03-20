# src/core/signal_processing/__init__.py
from .config import SignalConfig
from .processor import SignalProcessingPipeline
from .signal_processor import SignalProcessor
from .segment_handler import SegmentHandler
from .sqi_scorer import CompositeConfig, score_windows

__all__ = [
    'SignalConfig',
    'SignalProcessingPipeline',
    'SignalProcessor',
    'SegmentHandler',
    'CompositeConfig',
    'score_windows',
]