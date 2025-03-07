import numpy as np
import pandas as pd
import os
import datetime as dt
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel

SEGMENT_PATH = 'src/output/Segmented_Data_24EI'
FEATURE_PATH = 'src/output/Feature_Data_24EI'

# Data loading (unchanged)
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
    """
    Russell's octave-tone Hz for PPG range.
    """
    return {
        'Mg': [4.0],
        'Ca': [6.0],
        'Fe': [12.0],
        'Zn': [18.0]
    }

def preprocess_ppg(ppg_signal, fs=100, lowcut=0.1, highcut=40.0):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(2, [low, high], btype='band')
    return signal.filtfilt(b, a, ppg_signal)

def compute_stft(ppg_signal, fs=100):
    f, t, Zxx = signal.stft(ppg_signal, fs, nperseg=512)
    return f, t, np.abs(Zxx)

def detect_peaks(frequencies, power_spectrum, absorption_bands, height_percentile=95, distance=5):
    """
    Detect peaks and align with Russell frequencies.
    """
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

def plot_spectral_verification(patient_id=None, fs=100, output_dir='element_plots'):
    df_patient = df[df['patient_id'] == patient_id].copy()
    df_patient = df_patient.sort_values(by=['segment_path'])
    
    absorption_bands = russell_harmonic_frequencies()
    
    detected_summary = {}
    power_trends = {element: [] for element in absorption_bands.keys()}
    time_trends = {element: [] for element in absorption_bands.keys()}
    day1_psd = []
    day5_psd = []
    
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(len(df_patient)):
        segment = pd.read_csv(df_patient['segment_path'].iloc[i])['PLETH'].values
        ppg_signal = preprocess_ppg(segment, fs)
        
        f, t, Zxx = compute_stft(ppg_signal, fs)
        power_spectrum = np.mean(Zxx, axis=1)
        
        detected, power_values, peaks, all_peak_freqs = detect_peaks(f, power_spectrum, absorption_bands)
        
        # Day 1 vs. Day 5 split (adjust if metadata exists)
        if i < len(df_patient) // 2:
            day1_psd.append(power_spectrum)
        else:
            day5_psd.append(power_spectrum)
        
        if detected:
            detected_summary[i] = detected
            start_time = dt.datetime.strptime(df_patient['segment_path'].iloc[i].split("/")[-1].split("_")[0], '%Y%m%dT%H%M%S')
            offset = int(df_patient['segment_path'].iloc[i].split("/")[-1].split("_")[1])
            converted_time = start_time + dt.timedelta(seconds=int(offset / 100))
            
            for element, powers in power_values.items():
                time_trends[element].append(converted_time)
                power_trends[element].extend(powers)
        
        # Plot spectrogram and PSD with peak frequencies labeled
        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.pcolormesh(t, f, np.log(Zxx + 1e-6), shading='gouraud')
        plt.title(f'Segment {i} Spectrogram - Patient {patient_id}')
        plt.ylabel('Frequency (Hz)')
        for el, bands in detected.items():
            for b in bands:
                plt.axhline(b, color='white', linestyle='--', label=f'{el} {b:.1f} Hz')
        plt.legend()
        
        plt.subplot(2, 1, 2)
        plt.plot(f, power_spectrum, label='Power Spectrum')
        plt.plot(f[peaks], power_spectrum[peaks], 'ro', label='Detected Peaks')
        # Label all peak frequencies
        for peak_freq, peak_power in zip(all_peak_freqs, power_spectrum[peaks]):
            plt.text(peak_freq, peak_power, f'{peak_freq:.1f}', color='red', ha='center', va='bottom')
        for el, bands in absorption_bands.items():
            for b in bands:
                plt.axvline(b, color='r', linestyle='--', alpha=0.5, label=f'{el} {b:.1f} Hz')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.legend()
        plt.savefig(os.path.join(output_dir, f'segment_{patient_id}_{i}.png'), bbox_inches='tight')
        plt.close()
    
    # Power trends plot
    if any(power_trends.values()):
        plt.figure(figsize=(12, 6))
        for element, powers in power_trends.items():
            if len(powers) > 0:
                sorted_times, sorted_powers = zip(*sorted(zip(time_trends[element], powers)))
                plt.plot(sorted_times, sorted_powers, label=f'{element} ({absorption_bands[element][0]} Hz)', marker='o')
        plt.xlabel('Time')
        plt.ylabel('Power')
        plt.title(f'Elemental Frequency Power Trends - Patient {patient_id}')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, f'power_trends_{patient_id}.png'), bbox_inches='tight')
        plt.close()
    
    # Day 1 vs. Day 5 comparison
    if day1_psd and day5_psd:
        day1_avg_psd = np.mean(day1_psd, axis=0)
        day5_avg_psd = np.mean(day5_psd, axis=0)
        plt.figure(figsize=(8, 6))
        plt.plot(f, day1_avg_psd, label='Day 1 Avg PSD')
        plt.plot(f, day5_avg_psd, label='Day 5 Avg PSD')
        for el, bands in absorption_bands.items():
            for b in bands:
                plt.axvline(b, color='r', linestyle='--', alpha=0.5, label=f'{el} {b:.1f} Hz')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.title(f'Day 1 vs. Day 5 PSD - Patient {patient_id}')
        plt.legend()
        plt.savefig(os.path.join(output_dir, f'day_comparison_{patient_id}.png'), bbox_inches='tight')
        plt.close()
        
        # T-test
        for el, bands in absorption_bands.items():
            for b in bands:
                idx = np.argmin(np.abs(f - b))
                day1_power = [psd[idx] for psd in day1_psd]
                day5_power = [psd[idx] for psd in day5_psd]
                if len(day1_power) == len(day5_power) and len(day1_power) > 1:
                    stat, p_value = ttest_rel(day1_power, day5_power)
                    print(f'{el} ({b} Hz) Day 1 vs. Day 5: t-stat={stat:.3f}, p-value={p_value:.3f}')
    
    return detected_summary

if __name__ == "__main__":
    patients = df['patient_id'].unique()
    for patient in patients:
        detected_summary = plot_spectral_verification(patient)