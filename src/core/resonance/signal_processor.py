# src/core/resonance/signal_processor.py
import numpy as np
from scipy import signal
from typing import Tuple, Dict, List
from dataclasses import dataclass
from .config import ResonanceConfig

@dataclass
class ProcessedSignal:
    """Container for processed signal data."""
    frequencies: np.ndarray
    power_spectrum: np.ndarray  # Reduced to only what we need

class SignalProcessor:
    """Handle signal processing operations with memory efficiency."""
    
    def __init__(self, config: ResonanceConfig):
        self.config = config
        self.chunk_size = int(self.config.fs * 60)  # Process 1-minute chunks

    def preprocess_ppg(self, ppg_signal: np.ndarray) -> np.ndarray:
        """Apply bandpass filter to PPG signal."""
        nyq = 0.5 * self.config.fs
        low = self.config.lowcut / nyq
        high = self.config.highcut / nyq
        b, a = signal.butter(2, [low, high], btype='band')
        return signal.filtfilt(b, a, ppg_signal)

    def compute_spectral_features(self, ppg_signal: np.ndarray) -> ProcessedSignal:
        """Compute spectral features in chunks to manage memory."""
        if not ppg_signal.size:
            return ProcessedSignal(np.array([]), np.array([]))

        # Process signal in chunks
        n_samples = len(ppg_signal)
        chunk_size = min(self.chunk_size, n_samples)
        n_chunks = max(1, n_samples // chunk_size)
        
        # Initialize arrays with first chunk
        f, t, Zxx = signal.stft(  # Correctly unpack 3 values
            ppg_signal[:chunk_size],
            self.config.fs,
            nperseg=self.config.nperseg,
            return_onesided=True,
            boundary=None
        )
        power_spectrum = np.zeros_like(f, dtype=np.float64)
        
        # Process chunks
        for i in range(n_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, n_samples)
            chunk = self.preprocess_ppg(ppg_signal[start:end])
            
            f_chunk, t_chunk, Zxx = signal.stft(  # Correctly unpack 3 values here too
                chunk,
                self.config.fs,
                nperseg=self.config.nperseg,
                return_onesided=True,
                boundary=None
            )
            power_spectrum += np.mean(np.abs(Zxx), axis=1) / n_chunks
        
        return ProcessedSignal(f, power_spectrum)

    def detect_peaks(
        self,
        signal_data: ProcessedSignal,
        absorption_bands: Dict[str, List[float]]
    ) -> Tuple[Dict, Dict, np.ndarray, np.ndarray]:
        """Detect peaks in power spectrum."""
        if not signal_data.frequencies.size:
            return {}, {}, np.array([]), np.array([])

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