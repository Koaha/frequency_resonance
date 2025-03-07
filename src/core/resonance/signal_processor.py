# src/core/resonance/signal_processor.py
import numpy as np
from scipy import signal
from typing import Tuple, Dict, List
from dataclasses import dataclass
from .config import ResonanceConfig  # Add this import

@dataclass
class ProcessedSignal:
    """Container for processed signal data."""
    frequencies: np.ndarray
    times: np.ndarray
    spectrogram: np.ndarray
    power_spectrum: np.ndarray
class SignalProcessor:
    """Handle signal processing operations."""
    
    def __init__(self, config: ResonanceConfig):
        self.config = config

    def preprocess_ppg(self, ppg_signal: np.ndarray) -> np.ndarray:
        """Apply bandpass filter to PPG signal."""
        nyq = 0.5 * self.config.fs
        low = self.config.lowcut / nyq
        high = self.config.highcut / nyq
        b, a = signal.butter(2, [low, high], btype='band')
        return signal.filtfilt(b, a, ppg_signal)

    def compute_spectral_features(self, ppg_signal: np.ndarray) -> ProcessedSignal:
        """Compute STFT and power spectrum."""
        processed_signal = self.preprocess_ppg(ppg_signal)
        f, t, Zxx = signal.stft(
            processed_signal, 
            self.config.fs, 
            nperseg=self.config.nperseg
        )
        power_spectrum = np.mean(np.abs(Zxx), axis=1)
        
        return ProcessedSignal(f, t, np.abs(Zxx), power_spectrum)

    def detect_peaks(
        self, 
        signal_data: ProcessedSignal,
        absorption_bands: Dict[str, List[float]]
    ) -> Tuple[Dict, Dict, np.ndarray, np.ndarray]:
        """Detect peaks in power spectrum."""
        height = np.percentile(
            signal_data.power_spectrum, 
            self.config.peak_height_percentile
        )
        peaks, _ = signal.find_peaks(
            signal_data.power_spectrum,
            height=height,
            distance=self.config.peak_distance
        )
        
        peak_freqs = signal_data.frequencies[peaks]
        
        detected_elements = {}
        power_values = {}
        
        for element, bands in absorption_bands.items():
            detected = []
            powers = []
            for band in bands:
                close_peaks = peak_freqs[np.abs(peak_freqs - band) <= 0.5]
                if len(close_peaks) > 0:
                    idx = np.argmin(np.abs(signal_data.frequencies - band))
                    detected.append(band)
                    powers.append(signal_data.power_spectrum[idx])
            if detected:
                detected_elements[element] = detected
                power_values[element] = powers
        
        return detected_elements, power_values, peaks, peak_freqs