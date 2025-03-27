# src/core/resonance/analyzer.py
import pandas as pd
import numpy as np
from typing import Dict, Optional, List
import logging
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from .config import ResonanceConfig
from .data_manager import DataManager, PatientData
from .signal_processor import SignalProcessor, ProcessedSignal
from .visualization import Visualizer
from tqdm import tqdm

class ResonanceAnalyzer:
    """Main class for coordinating resonance analysis of patient data."""
    
    def __init__(self, config: ResonanceConfig = None):
        """Initialize the analyzer with configuration and components."""
        self.config = config or ResonanceConfig()
        self.data_manager = DataManager(self.config)
        self.signal_processor = SignalProcessor(self.config)
        self.visualizer = Visualizer(self.config)
        self.logger = logging.getLogger(__name__)
        self.config.OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    def _process_day_data(
        self,
        signal: np.ndarray,
        day_label: str,
        patient_id: str
    ) -> tuple[Optional[ProcessedSignal], Dict, Dict, np.ndarray, np.ndarray]:
        """Process signal data for a specific day."""
        if not signal.size:
            return None, {}, {}, np.array([]), np.array([])
            
        processed = self.signal_processor.compute_spectral_features(signal)
        detected, powers, peaks, peak_freqs = self.signal_processor.detect_peaks(
            processed,
            self.config.get_harmonic_frequencies()
        )
        # Note: We can't plot spectrogram anymore since we don't store it
        # Modify visualization to use power spectrum only
        self.visualizer.plot_day_analysis(
            processed, peaks, peak_freqs, detected, day_label, patient_id
        )
        return processed, detected, powers, peaks, peak_freqs

    def analyze_patient(self, patient_data: PatientData, patient_id: str) -> List[Dict]:
        """Analyze resonance patterns for a single patient across days."""
        try:
            self.logger.info(f"Processing patient: {patient_id}")
            
            # Process Day 1 and Day 5 concurrently
            with ProcessPoolExecutor(max_workers=2) as executor:
                day1_future = executor.submit(
                    self._process_day_data, patient_data.day1_signal, "Day 1", patient_id
                )
                day5_future = executor.submit(
                    self._process_day_data, patient_data.day5_signal, "Day 5", patient_id
                )
                
                day1_result = day1_future.result()
                day5_result = day5_future.result()

            day1_processed, _, day1_powers, _, _ = day1_result
            day5_processed, _, day5_powers, _, _ = day5_result

            # Generate comparison plot
            self.visualizer.plot_day_comparison(day1_processed, day5_processed, patient_id)
            
            return self._prepare_analysis_results(
                patient_id, patient_data, day1_processed, day5_processed,
                day1_powers, day5_powers
            )
            
        except Exception as e:
            self.logger.error(f"Error analyzing patient {patient_id}: {str(e)}")
            raise

    def analyze_all_patients(self) -> pd.DataFrame:
        """Analyze all patients in the dataset with parallel processing."""
        try:
            df = self.data_manager.load_patient_files()
            patients = df['patient_id'].unique()
            self.logger.info(f"Processing {len(patients)} patients")
            
            all_results = []
            patient_groups = [(pid, group) for pid, group in df.groupby('patient_id')]
            
            with ProcessPoolExecutor() as executor:
                process_func = partial(self._process_patient_wrapper, config=self.config)
                results = list(tqdm(
                    executor.map(process_func, patient_groups),
                    total=len(patients),
                    desc="Processing patients"
                ))
                all_results.extend([r for sublist in results for r in sublist])
            
            master_df = pd.DataFrame(all_results)
            master_df.to_csv(self.config.MASTER_CSV, index=False, compression='gzip')
            self.logger.info(f"Results saved to {self.config.MASTER_CSV}")
            return master_df
            
        except Exception as e:
            self.logger.error(f"Batch analysis failed: {str(e)}")
            raise

    def _process_patient_wrapper(self, patient_group: tuple, config: ResonanceConfig) -> List[Dict]:
        """Wrapper for parallel patient processing."""
        patient_id, patient_df = patient_group
        analyzer = ResonanceAnalyzer(config)
        patient_data = analyzer.data_manager.process_patient_data(patient_df, patient_id)
        return analyzer.analyze_patient(patient_data, patient_id)

    def _prepare_analysis_results(
        self,
        patient_id: str,
        patient_data: PatientData,
        day1_processed: Optional[ProcessedSignal],
        day5_processed: Optional[ProcessedSignal],
        day1_powers: Dict,
        day5_powers: Dict
    ) -> List[Dict]:
        """Prepare structured results for storage."""
        results = []
        harmonic_freqs = self.config.get_harmonic_frequencies()
        
        if day1_processed:
            day1_result = {
                'patient_id': patient_id,
                'day': patient_data.day1_date.strftime('%Y-%m-%d'),
                'num_files': patient_data.day1_count
            }
            for element, bands in harmonic_freqs.items():
                for band in bands:
                    power_key = f'{element}_{int(band)}Hz_power'
                    day1_result[power_key] = day1_powers.get(element, [0])[0]
                    day1_result[f'{power_key}_diff'] = 0
            results.append(day1_result)
        
        if day5_processed:
            day5_result = {
                'patient_id': patient_id,
                'day': patient_data.time_points[-1][0].date().strftime('%Y-%m-%d'),
                'num_files': patient_data.day5_count
            }
            for element, bands in harmonic_freqs.items():
                for band in bands:
                    power_key = f'{element}_{int(band)}Hz_power'
                    day5_power = day5_powers.get(element, [0])[0]
                    day1_power = day1_powers.get(element, [0])[0] if day1_processed else 0
                    day5_result[power_key] = day5_power
                    day5_result[f'{power_key}_diff'] = day5_power - day1_power
            results.append(day5_result)
        
        return results