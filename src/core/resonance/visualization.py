# src/core/resonance/visualization.py
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, Optional
import numpy as np
from .config import ResonanceConfig
from .signal_processor import ProcessedSignal

class Visualizer:
    """Handle visualization of resonance analysis."""
    
    def __init__(self, config: ResonanceConfig):
        self.config = config
        self.config.PLOT_DIR.mkdir(parents=True, exist_ok=True)

    def plot_day_analysis(
        self,
        signal_data: ProcessedSignal,
        peaks: np.ndarray,
        peak_freqs: np.ndarray,
        detected: Dict,
        day: str,
        patient_id: str
    ) -> None:
        """Plot analysis results for a single day."""
        plt.figure(figsize=(12, 8))
        
        # Spectrogram
        plt.subplot(2, 1, 1)
        plt.pcolormesh(
            signal_data.times,
            signal_data.frequencies,
            np.log(signal_data.spectrogram + 1e-6),
            shading='gouraud'
        )
        plt.title(f'{day} Spectrogram - Patient {patient_id}')
        plt.ylabel('Frequency (Hz)')
        
        # Create custom legend entries for element bands
        legend_elements = []
        added_elements = set()
        
        for el, bands in detected.items():
            for b in bands:
                if el not in added_elements:
                    # Create a custom line for legend
                    line = plt.Line2D(
                        [0], [0],
                        color='white',
                        linestyle='--',
                        label=f'{el} bands'
                    )
                    legend_elements.append(line)
                    added_elements.add(el)
                    
                plt.axhline(
                    b,
                    color='white',
                    linestyle='--'
                )
        
        if legend_elements:  # Only add legend if we have elements
            plt.legend(handles=legend_elements)
        
        # Power Spectrum
        plt.subplot(2, 1, 2)
        plt.plot(
            signal_data.frequencies,
            signal_data.power_spectrum,
            label=f'{day} PSD',
            color='blue'
        )
        plt.plot(
            signal_data.frequencies[peaks],
            signal_data.power_spectrum[peaks],
            'ro',
            label='Detected Peaks'
        )
        
        # Add peak labels
        for freq, power in zip(peak_freqs, signal_data.power_spectrum[peaks]):
            plt.text(
                freq,
                power,
                f'{freq:.1f}',
                color='red',
                ha='center',
                va='bottom'
            )
        
        # Add element bands with proper legend handling
        added_elements = set()
        legend_elements = []
        
        for el, bands in self.config.get_harmonic_frequencies().items():
            for b in bands:
                if el not in added_elements:
                    # Create a custom line for legend
                    line = plt.Line2D(
                        [0], [0],
                        color='r',
                        linestyle='--',
                        alpha=0.5,
                        label=f'{el} reference'
                    )
                    legend_elements.append(line)
                    added_elements.add(el)
                    
                plt.axvline(
                    b,
                    color='r',
                    linestyle='--',
                    alpha=0.5
                )
        
        # Add all legend elements
        handles, labels = plt.gca().get_legend_handles_labels()
        handles.extend(legend_elements)
        plt.legend(handles=handles)
        
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        
        plt.tight_layout()
        plt.savefig(
            self.config.PLOT_DIR / f'{day.lower()}_{patient_id}.png',
            bbox_inches='tight',
            dpi=300
        )
        plt.close()

    def plot_day_comparison(
        self,
        day1_data: Optional[ProcessedSignal],
        day5_data: Optional[ProcessedSignal],
        patient_id: str
    ) -> None:
        """Plot comparison between Day 1 and Day 5."""
        plt.figure(figsize=(10, 6))
        
        # Plot data only if available
        if day1_data is not None:
            plt.plot(
                day1_data.frequencies,
                day1_data.power_spectrum,
                label='Day 1 PSD',
                color='blue',
                alpha=0.7
            )
            
        if day5_data is not None:
            plt.plot(
                day5_data.frequencies,
                day5_data.power_spectrum,
                label='Day 5 PSD',
                color='red',
                alpha=0.7
            )
            
        # Add element bands with proper legend handling
        added_elements = set()
        for el, bands in self.config.get_harmonic_frequencies().items():
            for b in bands:
                if el not in added_elements:
                    label = f'{el} reference'
                    added_elements.add(el)
                else:
                    label = '_nolegend_'
                    
                plt.axvline(
                    b,
                    color='gray',
                    linestyle='--',
                    alpha=0.5,
                    label=label
                )
                
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.title(f'Day 1 vs. Day 5 PSD - Patient {patient_id}')
        
        # Only add legend if we have plotted data
        if day1_data is not None or day5_data is not None:
            plt.legend()
            
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        plt.savefig(
            self.config.PLOT_DIR / f'day_comparison_{patient_id}.png',
            bbox_inches='tight',
            dpi=300
        )
        plt.close()