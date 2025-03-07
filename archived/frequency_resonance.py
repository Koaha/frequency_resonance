import numpy as np
import pandas as pd
import os, sys
import shutil
import datetime as dt
import scipy.signal as signal
import matplotlib.pyplot as plt
# import pywt
from scipy.fftpack import fft
from scipy.stats import ttest_rel

SEGMENT_PATH = 'src/output/Segmented_Data_24EI'
FEATURE_PATH = 'src/output/Feature_Data_24EI'

data_list = []
for patient_id in filter(lambda x: os.path.isdir(os.path.join(SEGMENT_PATH, x)), os.listdir(SEGMENT_PATH)):
    data_path = os.path.join(SEGMENT_PATH, patient_id, "data")
    feature_path = os.path.join(FEATURE_PATH,patient_id, "data", "features")
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
            feature_path_content = os.path.join(feature_path,feature_file)
            data_list.append({
                "patient_id": patient_id,
                "rr_path": rr_path,
                "feature_path":feature_path_content,
                "segment_path": segment_path if os.path.exists(segment_path) else None
            })

# Create DataFrame

df = pd.DataFrame(data_list)
# # Display DataFrame
# import ace_tools as tools
# tools.display_dataframe_to_user(name="Patient Files Data", dataframe=df)
df.sort_values(by=["segment_path", "patient_id"])

#================================================================================================

def wavelength_to_frequency(wavelength_nm, scaling_factor=1e14):
    """
    Convert wavelength (nm) to a physiologically relevant frequency (Hz).
    """
    c = 3e8  # Speed of light in m/s
    freq_thz = c / (wavelength_nm * 1e-9)  # Convert nm to THz
    return freq_thz / scaling_factor  # Scale down to match PPG range

def preprocess_ppg(ppg_signal, fs=100, lowcut=0.5, highcut=10.0):
    """
    Bandpass filter the PPG signal.
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(2, [low, high], btype='band')
    filtered_signal = signal.filtfilt(b, a, ppg_signal)
    return filtered_signal

def compute_stft(ppg_signal, fs=100):
    """
    Compute Short-Time Fourier Transform (STFT) of the PPG signal.
    """
    f, t, Zxx = signal.stft(ppg_signal, fs, nperseg=512)
    return f, t, np.abs(Zxx)

def detect_elemental_presence(frequencies, power_spectrum, absorption_bands):
    """
    Check if any spectral peaks align with elemental frequencies and extract power values.
    """
    detected_elements = {}
    power_values = {}
    for element, bands in absorption_bands.items():
        detected = []
        powers = []
        for band in bands:
            idx = (np.abs(frequencies - band)).argmin()
            if power_spectrum[idx] > np.percentile(power_spectrum, 95):
                detected.append(band)
                powers.append(power_spectrum[idx])
        if detected:
            detected_elements[element] = detected
            power_values[element] = powers
    return detected_elements, power_values


def russell_harmonic_frequencies():
    """
    Assign Hz based on Russell's octave-tone positions (6th-8th octaves, scaled to PPG).
    """
    return {
        'Mg': [4.0],  # 6th octave, tone 2
        'Ca': [6.0],  # 7th octave, tone 2
        'Fe': [12.0], # 7th octave, tone 7
        'Zn': [18.0]  # 8th octave, tone 5
    }

def plot_spectral_verification(patient_id=None, fs=100, output_dir='plots'):
    """
    Load PPG CSV, analyze each segment, and detect elemental presence.
    """
    df_patient = df[df['patient_id'] == patient_id].copy()
    df_patient = df_patient.sort_values(by=['segment_path'])  # Ensure chronological order
    
    # absorption_bands = {
    #     'Fe': [wavelength_to_frequency(438), wavelength_to_frequency(527), wavelength_to_frequency(617)],
    #     'Zn': [wavelength_to_frequency(472), wavelength_to_frequency(481)],
    #     'Mg': [wavelength_to_frequency(518), wavelength_to_frequency(552)],
    #     'Ca': [wavelength_to_frequency(422), wavelength_to_frequency(445)]
    # }
    absorption_bands = russell_harmonic_frequencies()

    detected_summary = {}
    power_trends = {element: [] for element in absorption_bands.keys()}
    time_trends = {element: [] for element in absorption_bands.keys()}
    
    for i in range(len(df_patient)):
        segment = (pd.read_csv(df_patient['segment_path'].iloc[i]))['PLETH'].values
        ppg_signal = preprocess_ppg(segment, fs)
        
        f, t, Zxx = compute_stft(ppg_signal, fs)
        power_spectrum = np.mean(Zxx, axis=1)  # Average power across time
        
        detected, power_values = detect_elemental_presence(f, power_spectrum, absorption_bands)
        
        if detected:
            detected_summary[i] = detected
            start_time = dt.datetime.strptime(df_patient['segment_path'].iloc[i].split("/")[-1].split("_")[0], '%Y%m%dT%H%M%S')
            offset = int(df_patient['segment_path'].iloc[i].split("/")[-1].split("_")[1])
            converted_time = start_time + dt.timedelta(seconds=int(offset / 100))
            
            for element, powers in power_values.items():
                time_trends[element].append(converted_time)
                power_trends[element].extend(powers)
    
    if any(power_trends.values()):
        plt.figure(figsize=(12, 6))
        for element, powers in power_trends.items():
            if len(powers) > 0:
                sorted_times, sorted_powers = zip(*sorted(zip(time_trends[element], powers)))
                plt.plot(sorted_times, sorted_powers, label=f'{element} Power', marker='o')
        
        plt.xlabel('Time')
        plt.ylabel('Power (Normalized)')
        plt.title(f'Elemental Frequency Power Trends Over Time for Patient {patient_id}')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, f'frequency_resonance_{patient_id}.png'))
        plt.close()

    # Statistical Analysis: Paired t-test for significant power changes
    for element, powers in power_trends.items():
        if len(powers) > 1:
            stat, p_value = ttest_rel(powers[:-1], powers[1:])
            print(f'{element} Power Change: t-stat={stat:.3f}, p-value={p_value:.3f}')
    
    return detected_summary

if __name__ == "__main__":
    # Example Usage:
    patients = df['patient_id'].unique()
    # detected_summary = plot_spectral_verification("ppg_segments.csv")
    # print(detected_summary)  # View which elements were detected in each 5-min segment
    for patient in patients:
        detected_summary = plot_spectral_verification(patient)
    # print(detected_summary) 
    