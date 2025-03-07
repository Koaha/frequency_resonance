import numpy as np
import pandas as pd
import os
import datetime as dt
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel

SEGMENT_PATH = 'src/output/Segmented_Data_24EI'
FEATURE_PATH = 'src/output/Feature_Data_24EI'
MASTER_CSV = 'master.csv'  # Output file

# Data loading
data_list = []
for patient_id in filter(lambda x: os.path.isdir(os.path.join(SEGMENT_PATH, x)), os.listdir(SEGMENT_PATH)):
    data_path = os.path.join(SEGMENT_PATH, patient_id, "data")
    feature_path = os.path.join(FEATURE_PATH, patient_id, "data", "features")
    if not os.path.isdir(data_path):
        continue
    
    rr_folder = os.path.join(data_path, "rr")
    segments_folder = os.path.join(data_path, "segments")
    
    if os.path.isdir(rr_folder) and os.path.isdir(segments_folder):
        rr_files = [f for f in os.listdir(rr_folder) if f.endswith("_rr.txt")]
        
        for rr_file in rr_files:
            rr_path = os.path.join(rr_folder, rr_file)
            segment_file = rr_file.replace('_rr.txt', '.csv')
            segment_path = os.path.join(segments_folder, segment_file)
            feature_file = rr_file.replace('_rr.txt', '_features.csv')
            feature_path_content = os.path.join(feature_path, feature_file)
            data_list.append({
                "patient_id": patient_id,
                "rr_path": rr_path,
                "feature_path": feature_path_content,
                "segment_path": segment_path if os.path.exists(segment_path) else None
            })

df = pd.DataFrame(data_list)
df.sort_values(by=["segment_path", "patient_id"])

# Functions
def russell_harmonic_frequencies():
    return {
        'Mg': [4.0],
        'Ca': [6.0],
        'Fe': [12.0],
        'Zn': [18.0]
    }

def preprocess_ppg(ppg_signal, fs=100, lowcut=0.5, highcut=20.0):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(2, [low, high], btype='band')
    return signal.filtfilt(b, a, ppg_signal)

def compute_stft(ppg_signal, fs=100, nperseg=1024):
    f, t, Zxx = signal.stft(ppg_signal, fs, nperseg=nperseg)
    return f, t, np.abs(Zxx)

def detect_peaks(frequencies, power_spectrum, absorption_bands, height_percentile=95, distance=5):
    height = np.percentile(power_spectrum, height_percentile)
    peaks, _ = signal.find_peaks(power_spectrum, height=height, distance=distance)
    all_peak_freqs = frequencies[peaks]
    
    detected_elements = {}
    power_values = {}
    for element, bands in absorption_bands.items():
        detected = []
        powers = []
        for band in bands:
            close_peaks = all_peak_freqs[np.abs(all_peak_freqs - band) <= 0.5]
            if len(close_peaks) > 0:
                idx = np.argmin(np.abs(frequencies - band))
                detected.append(band)
                powers.append(power_spectrum[idx])
        if detected:
            detected_elements[element] = detected
            power_values[element] = powers
    
    return detected_elements, power_values, peaks, all_peak_freqs

def plot_spectral_verification(df_patient, patient_id, fs=100, output_dir='concat_plots'):
    print(f"\nProcessing patient: {patient_id}")
    df_patient = df_patient.sort_values(by=['segment_path'])
    print(f"Total segments for {patient_id}: {len(df_patient)}")
    
    absorption_bands = russell_harmonic_frequencies()
    segment_duration = 300  # 5 minutes in seconds
    samples_per_segment = segment_duration * fs
    
    # Get the earliest date as Day 1
    first_segment_time = dt.datetime.strptime(df_patient['segment_path'].iloc[0].split("/")[-1].split("_")[0], '%Y%m%dT%H%M%S')
    day1_date = first_segment_time.date()
    print(f"Day 1 date for {patient_id}: {day1_date}")
    
    # Process segments
    day1_signals = []
    day5_signals = []
    time_points = []
    day1_count = 0
    day5_count = 0
    
    for i, row in df_patient.iterrows():
        try:
            segment = pd.read_csv(row['segment_path'])['PLETH'].values
            start_time = dt.datetime.strptime(row['segment_path'].split("/")[-1].split("_")[0], '%Y%m%dT%H%M%S')
            offset = int(row['segment_path'].split("/")[-1].split("_")[1]) / 100
            segment_start = start_time + dt.timedelta(seconds=offset)
            segment_end = segment_start + dt.timedelta(seconds=segment_duration)
            
            # Split by first day (Day 1) vs. others (Day 5)
            is_day1 = segment_start.date() == day1_date
            
            # Trim overlap
            if time_points:
                last_end = time_points[-1][1]
                if segment_start < last_end:
                    overlap_seconds = (last_end - segment_start).total_seconds()
                    overlap_samples = int(overlap_seconds * fs)
                    segment = segment[overlap_samples:]
            
            if len(segment) > 0:
                time_points.append((segment_start, segment_end))
                if is_day1:
                    day1_signals.append(segment)
                    day1_count += 1
                else:
                    day5_signals.append(segment)
                    day5_count += 1
        except Exception as e:
            print(f"Error processing segment {row['segment_path']}: {e}")
    
    print(f"Day 1 segments: {day1_count}, Day 5 segments: {day5_count}")
    
    # Concatenate signals
    day1_signal = np.concatenate(day1_signals) if day1_signals else np.array([])
    day5_signal = np.concatenate(day5_signals) if day5_signals else np.array([])
    print(f"Day 1 signal length: {len(day1_signal)}, Day 5 signal length: {len(day5_signal)}")
    
    # Process signals
    detected_summary = {'Day1': {}, 'Day5': {}}
    master_data = []
    
    if len(day1_signal) > 0:
        day1_processed = preprocess_ppg(day1_signal, fs)
        f1, t1, Zxx1 = compute_stft(day1_processed, fs)
        power_spectrum1 = np.mean(Zxx1, axis=1)
        detected1, power_values1, peaks1, peak_freqs1 = detect_peaks(f1, power_spectrum1, absorption_bands)
        detected_summary['Day1'] = detected1
        
        # Log Day 1 data
        day1_powers = {el: power_spectrum1[np.argmin(np.abs(f1 - b))] if b in [b for sublist in detected1.values() for b in sublist] else power_spectrum1[np.argmin(np.abs(f1 - b))] for el, bands in absorption_bands.items() for b in bands}
        master_data.append({
            'patient_id': patient_id,
            'day': day1_date.strftime('%Y-%m-%d'),
            'peak_frequencies': str(peak_freqs1.tolist()),
            'peak_frequencies_bpm': str((peak_freqs1 * 60).tolist()),
            'num_files': day1_count,
            'Mg_4Hz_power': day1_powers.get('Mg', 0),
            'Ca_6Hz_power': day1_powers.get('Ca', 0),
            'Fe_12Hz_power': day1_powers.get('Fe', 0),
            'Zn_18Hz_power': day1_powers.get('Zn', 0),
            'Mg_4Hz_diff': 0,  # No diff for Day 1
            'Ca_6Hz_diff': 0,
            'Fe_12Hz_diff': 0,
            'Zn_18Hz_diff': 0
        })
    else:
        f1, power_spectrum1, peak_freqs1 = np.array([]), np.array([]), np.array([])
        print(f"No Day 1 signal for {patient_id}")
    
    if len(day5_signal) > 0:
        day5_processed = preprocess_ppg(day5_signal, fs)
        f5, t5, Zxx5 = compute_stft(day5_processed, fs)
        power_spectrum5 = np.mean(Zxx5, axis=1)
        detected5, power_values5, peaks5, peak_freqs5 = detect_peaks(f5, power_spectrum5, absorption_bands)
        detected_summary['Day5'] = detected5
        
        # Log Day 5 data with differences
        day5_powers = {el: power_spectrum5[np.argmin(np.abs(f5 - b))] if b in [b for sublist in detected5.values() for b in sublist] else power_spectrum5[np.argmin(np.abs(f5 - b))] for el, bands in absorption_bands.items() for b in bands}
        diffs = {el: day5_powers[el] - day1_powers.get(el, 0) if len(day1_signal) > 0 else 0 for el in day5_powers}
        master_data.append({
            'patient_id': patient_id,
            'day': time_points[-1][0].date().strftime('%Y-%m-%d'),  # Last segment date as Day 5
            'peak_frequencies': str(peak_freqs5.tolist()),
            'peak_frequencies_bpm': str((peak_freqs5 * 60).tolist()),
            'num_files': day5_count,
            'Mg_4Hz_power': day5_powers.get('Mg', 0),
            'Ca_6Hz_power': day5_powers.get('Ca', 0),
            'Fe_12Hz_power': day5_powers.get('Fe', 0),
            'Zn_18Hz_power': day5_powers.get('Zn', 0),
            'Mg_4Hz_diff': diffs.get('Mg', 0),
            'Ca_6Hz_diff': diffs.get('Ca', 0),
            'Fe_12Hz_diff': diffs.get('Fe', 0),
            'Zn_18Hz_diff': diffs.get('Zn', 0)
        })
    else:
        f5, power_spectrum5, peak_freqs5 = np.array([]), np.array([]), np.array([])
        print(f"No Day 5 signal for {patient_id}")
    
    # Append to master CSV
    master_df = pd.DataFrame(master_data)
    if os.path.exists(MASTER_CSV):
        existing_df = pd.read_csv(MASTER_CSV)
        master_df = pd.concat([existing_df, master_df], ignore_index=True)
    master_df.to_csv(MASTER_CSV, index=False)
    print(f"Logged data to {MASTER_CSV}")
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Plot Day 1
    if len(day1_signal) > 0:
        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.pcolormesh(t1, f1, np.log(Zxx1 + 1e-6), shading='gouraud')
        plt.title(f'Day 1 Spectrogram - Patient {patient_id}')
        plt.ylabel('Frequency (Hz)')
        for el, bands in detected1.items():
            for b in bands:
                plt.axhline(b, color='white', linestyle='--', label=f'{el} {b:.1f} Hz')
        plt.legend()
        
        plt.subplot(2, 1, 2)
        plt.plot(f1, power_spectrum1, label='Day 1 PSD')
        plt.plot(f1[peaks1], power_spectrum1[peaks1], 'ro', label='Detected Peaks')
        for peak_freq, peak_power in zip(peak_freqs1, power_spectrum1[peaks1]):
            plt.text(peak_freq, peak_power, f'{peak_freq:.1f}', color='red', ha='center', va='bottom')
        for el, bands in absorption_bands.items():
            for b in bands:
                plt.axvline(b, color='r', linestyle='--', alpha=0.5, label=f'{el} {b:.1f} Hz')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.legend()
        plt.savefig(os.path.join(output_dir, f'day1_{patient_id}.png'), bbox_inches='tight')
        plt.close()
    
    # Plot Day 5
    if len(day5_signal) > 0:
        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.pcolormesh(t5, f5, np.log(Zxx5 + 1e-6), shading='gouraud')
        plt.title(f'Day 5 Spectrogram - Patient {patient_id}')
        plt.ylabel('Frequency (Hz)')
        for el, bands in detected5.items():
            for b in bands:
                plt.axhline(b, color='white', linestyle='--', label=f'{el} {b:.1f} Hz')
        plt.legend()
        
        plt.subplot(2, 1, 2)
        plt.plot(f5, power_spectrum5, label='Day 5 PSD')
        plt.plot(f5[peaks5], power_spectrum5[peaks5], 'ro', label='Detected Peaks')
        for peak_freq, peak_power in zip(peak_freqs5, power_spectrum5[peaks5]):
            plt.text(peak_freq, peak_power, f'{peak_freq:.1f}', color='red', ha='center', va='bottom')
        for el, bands in absorption_bands.items():
            for b in bands:
                plt.axvline(b, color='r', linestyle='--', alpha=0.5, label=f'{el} {b:.1f} Hz')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.legend()
        plt.savefig(os.path.join(output_dir, f'day5_{patient_id}.png'), bbox_inches='tight')
        plt.close()
    
    # Combined Day 1 vs. Day 5 PSD
    plt.figure(figsize=(8, 6))
    if len(day1_signal) > 0:
        plt.plot(f1, power_spectrum1, label='Day 1 PSD')
    if len(day5_signal) > 0:
        plt.plot(f5, power_spectrum5, label='Day 5 PSD')
    for el, bands in absorption_bands.items():
        for b in bands:
            plt.axvline(b, color='r', linestyle='--', alpha=0.5, label=f'{el} {b:.1f} Hz')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.title(f'Day 1 vs. Day 5 PSD - Patient {patient_id}')
    plt.legend()
    plt.savefig(os.path.join(output_dir, f'day_comparison_{patient_id}.png'), bbox_inches='tight')
    plt.close()
    
    return detected_summary

if __name__ == "__main__":
    patients = df['patient_id'].unique()
    print(f"Total patients: {len(patients)}")
    
    for patient_id, patient_df in df.groupby('patient_id'):
        detected_summary = plot_spectral_verification(patient_df, patient_id)