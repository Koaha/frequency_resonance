# src/core/resonance/analyzer.py
import pandas as pd
import numpy as np
from typing import Dict, Optional
import logging
from pathlib import Path
from .config import ResonanceConfig
from .data_manager import DataManager, PatientData
from .signal_processor import SignalProcessor, ProcessedSignal
from .visualization import Visualizer
from tqdm import tqdm

class ResonanceAnalyzer:
    """Main class for resonance analysis coordination."""
    
    def __init__(self, config: ResonanceConfig = ResonanceConfig()):
        self.config = config
        self.data_manager = DataManager(config)
        self.signal_processor = SignalProcessor(config)
        self.visualizer = Visualizer(config)
        self.logger = logging.getLogger(__name__)
        
        # Create output directories
        self.config.OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    def analyze_patient(
        self,
        patient_data: PatientData,
        patient_id: str
    ) -> Dict:
        """Analyze resonance patterns for a single patient."""
        try:
            self.logger.info(f"Processing patient: {patient_id}")
            
            # Process Day 1 data
            day1_processed = None
            day1_detected = {}
            day1_powers = {}
            
            if len(patient_data.day1_signal) > 0:
                day1_processed = self.signal_processor.compute_spectral_features(
                    patient_data.day1_signal
                )
                day1_detected, day1_powers, peaks1, peak_freqs1 = self.signal_processor.detect_peaks(
                    day1_processed,
                    self.config.get_harmonic_frequencies()
                )
                
                # Plot Day 1 analysis
                self.visualizer.plot_day_analysis(
                    day1_processed,
                    peaks1,
                    peak_freqs1,
                    day1_detected,
                    "Day 1",
                    patient_id
                )
            
            # Process Day 5 data
            day5_processed = None
            day5_detected = {}
            day5_powers = {}
            
            if len(patient_data.day5_signal) > 0:
                day5_processed = self.signal_processor.compute_spectral_features(
                    patient_data.day5_signal
                )
                day5_detected, day5_powers, peaks5, peak_freqs5 = self.signal_processor.detect_peaks(
                    day5_processed,
                    self.config.get_harmonic_frequencies()
                )
                
                # Plot Day 5 analysis
                self.visualizer.plot_day_analysis(
                    day5_processed,
                    peaks5,
                    peak_freqs5,
                    day5_detected,
                    "Day 5",
                    patient_id
                )
            
            # Plot day comparison
            self.visualizer.plot_day_comparison(
                day1_processed,
                day5_processed,
                patient_id
            )
            
            # Prepare analysis results
            results = self._prepare_analysis_results(
                patient_id,
                patient_data,
                day1_processed,
                day5_processed,
                day1_powers,
                day5_powers
            )
            
            return results
            
        except Exception as e:
            self.logger.error(f"Error analyzing patient {patient_id}: {e}")
            raise

    def analyze_all_patients(self) -> pd.DataFrame:
        """Analyze all patients in the dataset."""
        try:
            # Load patient data
            df = self.data_manager.load_patient_files()
            patients = df['patient_id'].unique()
            self.logger.info(f"Processing {len(patients)} patients")
            
            all_results = []
            
            # Add progress bar for patient processing
            with tqdm(total=len(patients), desc="Processing patients") as pbar:
                for patient_id, patient_df in df.groupby('patient_id'):
                    try:
                        # Get patient data
                        patient_data = self.data_manager.process_patient_data(
                            patient_df,
                            patient_id
                        )
                        
                        # Analyze patient
                        results = self.analyze_patient(patient_data, patient_id)
                        all_results.extend(results)
                        
                    except Exception as e:
                        self.logger.error(f"Error processing patient {patient_id}: {e}")
                        continue
                    finally:
                        pbar.update(1)
                        pbar.set_postfix({"Current": patient_id})
            
            # Create and save master DataFrame
            master_df = pd.DataFrame(all_results)
            master_df.to_csv(self.config.MASTER_CSV, index=False)
            self.logger.info(f"Results saved to {self.config.MASTER_CSV}")
            
            return master_df
            
        except Exception as e:
            self.logger.error(f"Error in batch analysis: {e}")
            raise

    def _prepare_analysis_results(
        self,
        patient_id: str,
        patient_data: PatientData,
        day1_processed: Optional[ProcessedSignal],
        day5_processed: Optional[ProcessedSignal],
        day1_powers: Dict,
        day5_powers: Dict
    ) -> list:
        """Prepare analysis results for database storage."""
        results = []
        
        # Process Day 1 results
        if day1_processed is not None:
            day1_result = {
                'patient_id': patient_id,
                'day': patient_data.day1_date.strftime('%Y-%m-%d'),
                'num_files': patient_data.day1_count
            }
            
            # Add power values for each element
            for element, bands in self.config.get_harmonic_frequencies().items():
                for band in bands:
                    power_key = f'{element}_{int(band)}Hz_power'
                    diff_key = f'{element}_{int(band)}Hz_diff'
                    day1_result[power_key] = day1_powers.get(element, [0])[0]
                    day1_result[diff_key] = 0  # No diff for Day 1
            
            results.append(day1_result)
        
        # Process Day 5 results
        if day5_processed is not None:
            day5_result = {
                'patient_id': patient_id,
                'day': patient_data.time_points[-1][0].date().strftime('%Y-%m-%d'),
                'num_files': patient_data.day5_count
            }
            
            # Add power values and differences for each element
            for element, bands in self.config.get_harmonic_frequencies().items():
                for band in bands:
                    power_key = f'{element}_{int(band)}Hz_power'
                    diff_key = f'{element}_{int(band)}Hz_diff'
                    day5_power = day5_powers.get(element, [0])[0]
                    day1_power = day1_powers.get(element, [0])[0] if day1_processed else 0
                    
                    day5_result[power_key] = day5_power
                    day5_result[diff_key] = day5_power - day1_power
            
            results.append(day5_result)
        
        return results