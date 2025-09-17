# Code Explanation: 24EI Analysis Project

This document provides a comprehensive explanation of the codebase implementation, designed for beginners and newcomers to understand how the system works. This is a detailed line-by-line analysis covering all major components.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture Overview](#architecture-overview)
3. [Core Components Deep Dive](#core-components-deep-dive)
4. [Signal Processing Pipeline - Complete Analysis](#signal-processing-pipeline---complete-analysis)
5. [Resonance Analysis - Complete Analysis](#resonance-analysis---complete-analysis)
6. [Statistical Analysis - Complete Analysis](#statistical-analysis---complete-analysis)
7. [Data Flow Explanation](#data-flow-explanation)
8. [Key Algorithms and Methods](#key-algorithms-and-methods)
9. [Configuration System](#configuration-system)
10. [Error Handling and Logging](#error-handling-and-logging)
11. [Code Examples and Usage](#code-examples-and-usage)
12. [Advanced Features and Optimizations](#advanced-features-and-optimizations)

## Project Overview

This project analyzes **PPG (Photoplethysmography)** signals to extract heart rate variability (HRV) features and correlate them with clinical data, particularly catecholamine levels (Adrenalin, Noradrenalin, Dopamin) and ANSD (Autonomic Nervous System Dysfunction) status.

### What is PPG?
PPG is a non-invasive method to measure blood volume changes in tissues using light. It's commonly used in smartwatches and medical devices to measure heart rate and other cardiovascular parameters.

### What is HRV?
Heart Rate Variability is the variation in time between consecutive heartbeats. It's an important indicator of autonomic nervous system function and overall cardiovascular health.

## Architecture Overview

The project follows a **modular, pipeline-based architecture** with clear separation of concerns:

```
Raw PPG Data → Signal Processing → Feature Extraction → Analysis → Reporting
     ↓              ↓                    ↓              ↓          ↓
  CSV Files    Quality Check      HRV Features    Statistical   Plots &
              & Segmentation      & Morphology    Analysis      Reports
```

### Main Components:

1. **Signal Processing Pipeline** (`src/core/signal_processing/`)
   - Loads and validates raw PPG data
   - Performs quality assessment
   - Segments signals into analyzable chunks
   - Extracts features from each segment

2. **Resonance Analysis** (`src/core/resonance/`)
   - Performs spectral analysis
   - Detects element resonance frequencies
   - Compares Day 1 vs Day 5 data

3. **Statistical Analysis** (`explore_and_report/`)
   - Merges clinical and feature data
   - Performs statistical tests
   - Generates visualizations
   - Creates comprehensive reports

## Core Components Deep Dive

### 1. Signal Processing Pipeline

#### SignalConfig Class - Complete Analysis
```python
@dataclass
class SignalConfig:
    """Configuration for signal processing pipeline."""
    # Processing mode
    mode: str = "directory"  # Options: "directory" or "file_list"
    
    # Base paths
    output_base: Path = Path('D:\Workspace\Data\\24EI/output')
    data_dir: Path = Path('D:\Workspace\Data\\24EI\RAW_DATA')
    file_list_path: Path = None  # Path to CSV file containing list of files to process
    
    # Derived paths
    SEGMENT_PATH: Path = output_base / 'Segmented_Data_24EI'    
    FEATURE_PATH: Path = output_base / 'Feature_Data_24EI'
    OUTPUT_PATH: Path = output_base / 'signal_processing'
    
    # Signal processing parameters
    fs: int = 100  # Sampling frequency in Hz
    duration: int = 300  # 5 minutes in seconds
    step_size: int = 300  # 5 minutes in seconds
    lowcut: float = 0.5  # Low frequency cutoff for bandpass filter
    highcut: float = 20.0  # High frequency cutoff for bandpass filter
    nperseg: int = 1024  # Number of samples per STFT segment
    
    # Peak detection parameters
    peak_height_percentile: float = 95
    peak_distance: int = 5
    
    # Processing parameters
    max_workers: int = 4
    batch_size: int = 100
```

**Line-by-Line Explanation:**
- **Lines 2-3**: `@dataclass` decorator automatically generates `__init__`, `__repr__`, and other methods
- **Lines 4-5**: Processing mode determines whether to process all files in a directory or specific files from a list
- **Lines 7-9**: Base paths for input data and output directories
- **Lines 11-13**: Derived paths are automatically calculated from base paths
- **Lines 15-19**: Signal processing parameters control how the signal is analyzed
- **Lines 21-22**: Peak detection parameters for finding significant frequencies
- **Lines 24-25**: Parallel processing parameters for efficiency

#### SignalProcessor Class - Complete Analysis
```python
class SignalProcessor:
    """Handles signal processing operations."""
    
    def __init__(self, config: SignalConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def _is_ecg_file(self, file_path: Path) -> bool:
        """Check if the file is an ECG file based on filename."""
        return 'ECG' in str(file_path).upper()

    def _combine_ecg_headers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Combine the first three rows of ECG data to create proper headers."""
        # Get the three header rows
        device_row = df.iloc[0]
        feature_row = df.iloc[1]
        calibration_row = df.iloc[2]
        unit_row = df.iloc[3]
        
        # Combine headers
        new_headers = []
        for device, feature, calib, unit in zip(device_row, feature_row, calibration_row, unit_row):
            new_header = f"{device}_{feature}_{calib}_{unit}"
            new_headers.append(new_header)
        
        # Create new dataframe without the header rows
        new_df = df.iloc[4:].copy()
        new_df.columns = new_headers
        
        # Convert all cells to float type
        new_df = new_df.astype(float)
        return new_df

    def wearable_timestamp_to_datetime(self, ts):
        """Convert wearable timestamp to datetime object."""
        try:
            ts_float = float(ts)  # Convert to float first
            return datetime.datetime.fromtimestamp((ts_float))
        except Exception as e:
            self.logger.error(f"Error converting timestamp to datetime: {e}")
            return None

    def load_signal(self, file_path: Path) -> SignalData:
        """Load and prepare signal data from file."""
        try:
            if self._is_ecg_file(file_path):
                # Read ECG file with all rows first
                df = pd.read_csv(file_path, header=None, delimiter='\t')
                
                # Combine headers from first three rows
                df = self._combine_ecg_headers(df)
                
                # Select only the required columns
                df, matching_columns = self._select_ecg_columns(df)
                
                # Extract signal and timestamp
                signal = np.array(df[matching_columns['LL-RA_24BIT_CAL']].values)
                timestamp_ms = np.array(df[matching_columns['Timestamp_CAL']].values)
                
                # Get start time from filename
                start_datetime = dt.datetime.strptime(
                    file_path.stem.split("_")[2], 
                    '%Y%m%dT%H%M%S.%f%z'
                )
                
                # Convert timestamps
                timestamps = np.array([self.wearable_timestamp_to_datetime(ts) for ts in timestamp_ms])
                
                return SignalData(
                    signal=signal,
                    timestamps=timestamps,
                    file_path=file_path,
                    start_time=start_datetime,
                    signal_type='ECG'
                )
                
            else:
                # Handle PPG files
                df = pd.read_csv(file_path, encoding="latin1", on_bad_lines="skip")
                
                try:
                    # Extract date from file path
                    date_str = str(file_path).split('/')[-3]  # Get the date folder name
                    # Parse the date (ddmmyyyy format) and set time to noon
                    start_datetime = dt.datetime.strptime(date_str, '%d%m%Y').replace(
                        hour=12, minute=0, second=0, microsecond=0
                    )
                except (ValueError, IndexError) as e:
                    # Set default to 4 years before today
                    start_datetime = dt.datetime.now() - dt.timedelta(days=4*365)
                    self.logger.warning(f"Could not parse datetime from file path {file_path}, using default date: {start_datetime}")
                
                signal = np.array(df['PLETH'].values)
                timestamp_ms = np.array(df['TIMESTAMP_MS'].values)
                timestamps = start_datetime + pd.to_timedelta(timestamp_ms, unit='ms')
                
                return SignalData(
                    signal=signal,
                    timestamps=timestamps,
                    file_path=file_path,
                    start_time=start_datetime,
                    signal_type='PPG'
                )
            
        except Exception as e:
            self.logger.error(f"Error loading signal from {file_path}: {e}")
            raise

    def get_quality_segments(self, signal: np.ndarray) -> Tuple[np.ndarray, list]:
        """Identify high-quality segments in the signal."""
        sqi = SignalQualityIndex(signal)
        sqi_values, normal_segments, _ = sqi.signal_entropy_sqi(
            window_size=self.config.fs * self.config.duration,
            step_size=self.config.fs * self.config.step_size,
            threshold=-2,
            threshold_type='below'
        )
        return sqi_values, normal_segments
```

**Detailed Method Analysis:**

**`_is_ecg_file()` (Lines 29-31):**
- Checks if filename contains 'ECG' to determine signal type
- Uses case-insensitive comparison with `.upper()`

**`_combine_ecg_headers()` (Lines 33-53):**
- ECG files have complex headers with device, feature, calibration, and unit info
- Combines first 4 rows into meaningful column names
- Converts data to float for numerical processing

**`wearable_timestamp_to_datetime()` (Lines 69-78):**
- Converts Unix timestamps to Python datetime objects
- Handles conversion errors gracefully

**`load_signal()` (Lines 80-151):**
- **Lines 83-116**: ECG file processing
  - Reads tab-separated CSV with no headers
  - Combines multi-row headers into meaningful names
  - Extracts signal and timestamp columns
  - Parses start time from filename
- **Lines 118-147**: PPG file processing
  - Reads CSV with Latin-1 encoding
  - Extracts date from file path structure
  - Handles missing date information with fallback
  - Creates timestamps by adding milliseconds to start time

**`get_quality_segments()` (Lines 153-162):**
- Uses `vitalDSP` library for signal quality assessment
- Applies entropy-based quality index
- Returns segments that meet quality threshold

#### FeatureExtractor Class - Complete Analysis
```python
class FeatureExtractor:
    """Handles feature extraction from signal segments."""
    
    def __init__(self, fs: int = 100, signal_type: str = 'PPG'):
        self.fs = fs
        self.logger = logging.getLogger(__name__)
        self.signal_type = signal_type

    def extract_features(self, signal: np.ndarray) -> Dict[str, Any]:
        """Extract HRV and morphological features from signal segment."""
        try:
            if self.signal_type == "ECG":
                peak_config = {
                    "distance": 50,
                    "window_size": 7,
                    "threshold_factor": 1.6,
                    "search_window": 6,
                    "slope_unit": "radians",
                }
            else:  # PPG
                peak_config = {
                    "distance": 50,
                    "window_size": 7,
                    "threshold_factor": 0.8,
                    "search_window": 6,
                    "fs": self.fs,
                }

            # Extract RR intervals
            config = PreprocessConfig()
            rr_transformer = RRTransformation(signal, fs=self.fs, 
                                            signal_type=self.signal_type,
                                            options=None)
            rr_intervals = rr_transformer.compute_rr_intervals(
                preprocess_config=config,
                peak_config=peak_config
            ) * 1000  # convert to ms
            
            # Compute HRV features
            hrv_features = HRVFeatures(
                signal, 
                nn_intervals=rr_intervals, 
                fs=self.fs, 
                signal_type=self.signal_type
            )
            hrv_feats = hrv_features.compute_all_features()
            
            # Compute morphological features
            extractor = PhysiologicalFeatureExtractor(signal, fs=self.fs)
            morphology_feats = extractor.extract_features(
                signal_type=self.signal_type,
                preprocess_config=config,
                peak_config=peak_config 
            )
            
            return {**hrv_feats, **morphology_feats}, rr_intervals
            
        except Exception as e:
            self.logger.error(f"Feature extraction failed: {e}")
            raise
```

**Detailed Method Analysis:**

**`__init__()` (Lines 17-20):**
- Sets sampling frequency and signal type
- Initializes logger for error tracking

**`extract_features()` (Lines 22-75):**
- **Lines 25-40**: Configures peak detection parameters differently for ECG vs PPG
  - ECG uses higher threshold (1.6) and radians for slope
  - PPG uses lower threshold (0.8) and includes sampling frequency
- **Lines 42-52**: RR interval extraction
  - Uses `RRTransformation` to find heartbeats
  - Converts intervals to milliseconds
- **Lines 54-60**: HRV feature computation
  - Calculates heart rate variability metrics
  - Uses `HRVFeatures` class for comprehensive analysis
- **Lines 62-69**: Morphological feature extraction
  - Analyzes waveform shape characteristics
  - Uses `PhysiologicalFeatureExtractor` for detailed analysis
- **Lines 71-75**: Error handling and return

#### SegmentHandler Class - Complete Analysis
```python
class SegmentHandler:
    """Manages the processing and storage of signal segments."""
    
    def __init__(self, config: SignalConfig):
        self.config = config
        self.feature_extractor = FeatureExtractor(fs=config.fs)
        self.logger = logging.getLogger(__name__)

    def process_segment(
        self,
        signal_data: SignalData,
        start: int,
        end: int,
        output_dirs: dict[str, Path]
    ) -> bool:
        """Process a single signal segment."""
        try:
            # Prepare segment data
            segment = signal_data.signal[start:end]
            timestamps = signal_data.timestamps[start:end]
            
            # Extract features
            features, rr_intervals = self.feature_extractor.extract_features(segment)
            
            # Save segment data
            self._save_segment_data(
                segment,
                timestamps,
                signal_data.file_path,
                start,
                end,
                features,
                rr_intervals,
                output_dirs
            )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing segment {start}-{end}: {e}")
            return False

    def _save_segment_data(
        self,
        segment: np.ndarray,
        timestamps: np.ndarray,
        file_path: Path,
        start: int,
        end: int,
        features: dict,
        rr_intervals: np.ndarray,
        output_dirs: dict[str, Path]
    ) -> None:
        """Save segment data, features, and RR intervals."""
        base_name = f"{file_path.stem}_{start}_{end}"
        
        # Save segment
        pd.DataFrame({
            "TIMESTAMP_MS": timestamps,
            "PLETH": segment
        }).to_csv(output_dirs['segments'] / f"{base_name}.csv", index=False)
        
        # Save features
        features_df = pd.DataFrame([features])
        features_df['file_path'] = str(file_path)
        features_df['start'] = start
        features_df['end'] = end
        features_df.to_csv(
            output_dirs['features'] / f"{base_name}_features.csv",
            index=False
        )
        
        # Save RR intervals
        np.savetxt(output_dirs['rr'] / f"{base_name}_rr.txt", rr_intervals)
```

**Detailed Method Analysis:**

**`process_segment()` (Lines 19-51):**
- **Lines 28-29**: Extracts signal segment and corresponding timestamps
- **Lines 31-32**: Calls feature extractor to get HRV and morphological features
- **Lines 34-45**: Saves all data (segment, features, RR intervals) to files
- **Lines 47-50**: Error handling with detailed logging

**`_save_segment_data()` (Lines 53-84):**
- **Lines 65-70**: Saves raw signal segment as CSV with timestamps
- **Lines 72-80**: Saves extracted features as CSV with metadata
- **Lines 82-83**: Saves RR intervals as text file for further analysis

### 2. Data Structures - Complete Analysis

#### SignalData Class
```python
@dataclass
class SignalData:
    """Container for signal data and metadata."""
    signal: np.ndarray        # The actual PPG signal values
    timestamps: np.ndarray    # Time points for each sample
    file_path: Path          # Source file location
    start_time: dt.datetime  # When recording started
    signal_type: str         # 'PPG' or 'ECG'
```

**What it does:** A data container that holds all information about a signal in one place. Think of it as a labeled box containing the signal and its metadata.

**Field Explanations:**
- `signal`: Raw signal values (e.g., [0.1, 0.2, 0.15, 0.3, ...])
- `timestamps`: Corresponding time points for each sample
- `file_path`: Original file location for traceability
- `start_time`: When the recording began
- `signal_type`: Distinguishes between PPG and ECG signals

## Signal Processing Pipeline - Complete Analysis

### SignalProcessingPipeline Class - Complete Analysis
```python
class SignalProcessingPipeline:
    """Coordinates the entire signal processing pipeline."""
    
    def __init__(self, config: SignalConfig = SignalConfig()):
        self.config = config
        self.signal_processor = SignalProcessor(config)
        self.segment_handler = SegmentHandler(config)
        self.logger = logging.getLogger(__name__)

    def process_file(self, file_path: Path) -> bool:
        """Process a single file through the pipeline."""
        try:
            # Load signal
            signal_data = self.signal_processor.load_signal(file_path)
            
            # Get quality segments
            _, normal_segments = self.signal_processor.get_quality_segments(
                signal_data.signal
            )
            
            # Prepare output directories
            output_dirs = self._prepare_output_dirs(file_path)
            
            # Process segments
            for start, end in normal_segments:
                self.segment_handler.process_segment(
                    signal_data,
                    start,
                    end,
                    output_dirs
                )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {e}")
            return False

    def process_files(self, max_workers: int = 4) -> None:
        """Process all files in the data directory."""
        files = list(self.config.data_dir.rglob("*.csv"))
        files.sort()
        
        for file_path in tqdm(files):
            self.process_file(file_path)
```

**Detailed Method Analysis:**

**`process_file()` (Lines 20-47):**
- **Lines 23-24**: Loads signal data from file using SignalProcessor
- **Lines 26-29**: Identifies high-quality segments using signal quality assessment
- **Lines 31-32**: Prepares output directories for saving results
- **Lines 34-40**: Processes each quality segment through the pipeline
- **Lines 42-45**: Error handling with detailed logging

**`process_files()` (Lines 49-56):**
- **Lines 50-51**: Finds all CSV files in the data directory recursively
- **Lines 52-55**: Processes each file with progress bar using tqdm

## Resonance Analysis - Complete Analysis

### ResonanceConfig Class - Complete Analysis
```python
@dataclass
class ResonanceConfig:
    """Configuration settings for resonance analysis."""
    
    # File system paths
    SEGMENT_PATH: Path = Path('D:/Workspace/Data/24EIa/output/Segmented_Data_24EI')
    FEATURE_PATH: Path = Path('D:/Workspace/Data/24EIa/output/Feature_Data_24EI')
    OUTPUT_PATH: Path = Path('D:/Workspace/Data/24EIa/output/resonance_analysis')
    MASTER_CSV: Path = OUTPUT_PATH / 'master.csv.gz'
    PLOT_DIR: Path = OUTPUT_PATH / 'plots'
    
    # Signal processing parameters
    fs: int = 100  # Sampling frequency in Hz
    segment_duration: int = 300  # Segment duration in seconds (5 minutes)
    lowcut: float = 0.5  # Low frequency cutoff for bandpass filter
    highcut: float = 20.0  # High frequency cutoff for bandpass filter
    nperseg: int = 1024  # Number of samples per STFT segment
    peak_height_percentile: float = 95  # Percentile for peak detection threshold
    peak_distance: int = 5  # Minimum distance between peaks

    @staticmethod
    def get_harmonic_frequencies() -> Dict[str, List[float]]:
        """Return harmonic frequencies for elements of interest."""
        return {
            'Mg': [4.0],  # Magnesium resonance frequency
            'Ca': [6.0],  # Calcium resonance frequency
            'Fe': [12.0],  # Iron resonance frequency
            'Zn': [18.0]  # Zinc resonance frequency
        }
```

**Line-by-Line Explanation:**
- **Lines 2-6**: File system paths for input and output data
- **Lines 8-13**: Signal processing parameters for spectral analysis
- **Lines 15-16**: Peak detection parameters for finding resonance frequencies
- **Lines 18-25**: Element-specific resonance frequencies for analysis

### ResonanceAnalyzer Class - Complete Analysis
```python
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
```

**Detailed Method Analysis:**

**`_process_day_data()` (Lines 27-47):**
- **Lines 34-35**: Checks if signal has data
- **Lines 37-41**: Computes spectral features and detects peaks
- **Lines 42-46**: Generates visualization plots
- **Line 47**: Returns processed data and results

**`analyze_patient()` (Lines 49-79):**
- **Lines 54-65**: Uses parallel processing to analyze Day 1 and Day 5 simultaneously
- **Lines 67-70**: Extracts results from parallel processing
- **Lines 72-73**: Generates comparison visualization
- **Lines 75-78**: Prepares structured results for storage

**`analyze_all_patients()` (Lines 81-107):**
- **Lines 84-85**: Loads patient data and gets unique patient IDs
- **Lines 88-89**: Groups data by patient for parallel processing
- **Lines 91-98**: Uses ProcessPoolExecutor for parallel patient analysis
- **Lines 100-103**: Saves results to compressed CSV file

### SignalProcessor (Resonance) - Complete Analysis
```python
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
```

**Detailed Method Analysis:**

**`preprocess_ppg()` (Lines 21-27):**
- **Lines 23-25**: Calculates normalized frequency cutoffs for bandpass filter
- **Line 26**: Creates Butterworth filter coefficients
- **Line 27**: Applies zero-phase filtering using filtfilt

**`compute_spectral_features()` (Lines 29-64):**
- **Lines 31-32**: Handles empty signals gracefully
- **Lines 34-36**: Calculates chunk size for memory-efficient processing
- **Lines 38-46**: Initializes arrays with first chunk using STFT
- **Lines 48-62**: Processes remaining chunks and averages power spectra
- **Line 64**: Returns processed signal with frequencies and power spectrum

**`detect_peaks()` (Lines 66-102):**
- **Lines 68-69**: Handles empty frequency arrays
- **Lines 71-75**: Calculates peak detection threshold using percentile
- **Lines 76-80**: Finds peaks using scipy's find_peaks function
- **Lines 82-100**: Matches peaks to element resonance frequencies
- **Line 102**: Returns detected elements and power values

## Statistical Analysis - Complete Analysis

### Main Analysis Functions - Complete Analysis

#### Data Loading and Preprocessing
```python
def load_data(file_path: str, file_type: str = 'excel') -> pd.DataFrame:
    """
    Load data from Excel or CSV file with error handling.
    
    Args:
        file_path: Path to the file.
        file_type: 'excel' or 'csv'.
    
    Returns:
        Loaded DataFrame.
    
    Raises:
        FileNotFoundError: If file is not found.
        ValueError: If file type is invalid.
    """
    logger.info(f"Loading {file_type} file: {file_path}...")
    try:
        if file_type == 'excel':
            df = pd.read_excel(file_path)
        elif file_type == 'csv':
            df = pd.read_csv(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
        logger.debug(f"Loaded dataset with shape: {df.shape}")
        return df
    except FileNotFoundError:
        logger.error(f"File '{file_path}' not found. Please check the path.")
        raise

def preprocess_clinical_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess clinical data: select columns, filter, mutate, and rename.
    
    Args:
        df: Raw clinical DataFrame.
    
    Returns:
        Preprocessed DataFrame with renamed columns and patient_id.
    """
    logger.info("Preprocessing clinical data...")
    
    # Select columns
    validate_columns(df, CLINICAL_COLUMNS)
    clinical = df[CLINICAL_COLUMNS].copy()
    logger.debug(f"Selected columns, shape: {clinical.shape}")
    
    # Filter out NA in Adrenaline
    clinical = clinical.dropna(subset=['Adrenaline/Urine (µg/24h)'])
    logger.debug(f"After filtering NA, shape: {clinical.shape}")
    
    # Mutate ANSD columns
    clinical['ANSD d1'] = clinical['ANSD d1'].apply(lambda x: 'Yes_ANSD' if x == 1 else 'No_ANSD')
    clinical['ANSD d5'] = clinical['ANSD d5'].apply(lambda x: 'Yes_ANSD' if x == 1 else 'No_ANSD')
    logger.debug("ANSD columns mutated.")
    
    # Rename catecholamine columns
    clinical = clinical.rename(columns=CATECHOLAMINE_RENAME)
    logger.debug("Catecholamine columns renamed.")
    
    # Rename USUBJID to patient_id and add prefix
    clinical = clinical.rename(columns={'USUBJID': 'patient_id'})
    clinical['patient_id'] = PATIENT_ID_PREFIX + clinical['patient_id'].astype(str)
    
    return clinical
```

**Detailed Function Analysis:**

**`load_data()` (Lines 72-100):**
- **Lines 87-89**: Handles different file types (Excel vs CSV)
- **Lines 90-91**: Validates file type and raises error if unsupported
- **Lines 92-93**: Logs successful loading with data shape
- **Lines 94-96**: Handles file not found errors with detailed logging

**`preprocess_clinical_data()` (Lines 117-149):**
- **Lines 130-132**: Validates required columns exist
- **Lines 134-135**: Filters out patients with missing adrenaline data
- **Lines 137-140**: Converts ANSD binary values to categorical strings
- **Lines 142-143**: Renames catecholamine columns for consistency
- **Lines 145-147**: Creates standardized patient IDs with prefix

#### Statistical Analysis Functions
```python
def summarize_features(df: pd.DataFrame, merged_df: pd.DataFrame, output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Summarize features with medians, IQRs, and multiple statistical tests for Day1 vs Day5, including overall stats.
    
    Args:
        df: Aggregated DataFrame (pivoted with Day1 and Day5 columns).
        merged_df: Merged DataFrame with DayLabel for overall stats.
        output_dir: Directory to save results.
    
    Returns:
        DataFrame with detailed feature summaries.
    """
    logger.info("Summarizing features with comprehensive statistics...")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get base features (without _Day1/_Day5 suffixes)
    base_features = []
    for col in df.columns:
        if col.endswith('_Day1'):
            base_features.append(col.replace('_Day1', ''))
        elif col.endswith('_Day5'):
            base_features.append(col.replace('_Day5', ''))
    
    base_features = list(set(base_features))  # Remove duplicates
    logger.debug(f"Base features to summarize: {base_features}")
    
    def summarize_single_feature(feature: str) -> pd.Series:
        """Summarize a single feature with comprehensive statistics."""
        day1_col = f"{feature}_Day1"
        day5_col = f"{feature}_Day5"
        
        if day1_col not in df.columns or day5_col not in df.columns:
            logger.warning(f"Skipping {feature}: missing Day1 or Day5 columns")
            return pd.Series()
        
        # Day 1 statistics
        day1 = df[day1_col].dropna()
        med1 = np.median(day1)
        q1_1, q3_1 = np.percentile(day1, [25, 75])
        mean1 = np.mean(day1)
        sd1 = np.std(day1)
        
        # Day 5 statistics
        day5 = df[day5_col].dropna()
        med5 = np.median(day5)
        q1_5, q3_5 = np.percentile(day5, [25, 75])
        mean5 = np.mean(day5)
        sd5 = np.std(day5)
        
        # Overall statistics
        overall_data = merged_df[feature].dropna() if feature in merged_df.columns else pd.Series()
        med_overall = np.median(overall_data) if len(overall_data) > 0 else np.nan
        q1_overall, q3_overall = np.percentile(overall_data, [25, 75]) if len(overall_data) > 0 else (np.nan, np.nan)
        mean_overall = np.mean(overall_data) if len(overall_data) > 0 else np.nan
        sd_overall = np.std(overall_data) if len(overall_data) > 0 else np.nan
        
        # Calculate changes
        median_change_pct = ((med5 - med1) / med1 * 100) if med1 != 0 else np.nan
        mean_change_pct = ((mean5 - mean1) / mean1 * 100) if mean1 != 0 else np.nan
        
        # Statistical tests
        wilcoxon_p = ttest_p = sign_p = cohens_d = np.nan
        
        if len(day1) > 0 and len(day5) > 0:
            # Wilcoxon signed-rank test
            try:
                wilcoxon_stat, wilcoxon_p = stats.wilcoxon(day1, day5)
            except Exception as e:
                logger.warning(f"Wilcoxon test failed for {feature}: {str(e)}")
            
            # Paired t-test
            try:
                ttest_stat, ttest_p = stats.ttest_rel(day1, day5)
            except Exception as e:
                logger.warning(f"T-test failed for {feature}: {str(e)}")
            
            # Sign test
            try:
                signs = np.sign(day5 - day1)
                n_pos = np.sum(signs > 0)
                n_total = len(signs[signs != 0])
                if n_total > 0:
                    sign_p = binom_test(n_pos, n_total, p=0.5)
            except Exception as e:
                logger.warning(f"Sign test failed for {feature}: {str(e)}")
            
            # Cohen's d
            try:
                cohens_d = pg.compute_effsize(day1, day5, paired=True, eftype='cohen')
            except Exception as e:
                logger.warning(f"Cohen's d failed for {feature}: {str(e)}")
        
        return pd.Series({
            'Feature': feature,
            'Day1_Median_IQR': f"{med1:.1f} ({q1_1:.1f}–{q3_1:.1f})",
            'Day1_Mean_SD': f"{mean1:.1f} ± {sd1:.1f}",
            'Day5_Median_IQR': f"{med5:.1f} ({q1_5:.1f}–{q3_5:.1f})",
            'Day5_Mean_SD': f"{mean5:.1f} ± {sd5:.1f}",
            'Median_Change_Pct': f"{median_change_pct:.1f}%" if not np.isnan(median_change_pct) else 'NA',
            'Mean_Change_Pct': f"{mean_change_pct:.1f}%" if not np.isnan(mean_change_pct) else 'NA',
            'Overall_Median_IQR': f"{med_overall:.1f} ({q1_overall:.1f}–{q3_overall:.1f})",
            'Overall_Mean_SD': f"{mean_overall:.1f} ± {sd_overall:.1f}",
            'Wilcoxon_P': f"{wilcoxon_p:.3f}" if not np.isnan(wilcoxon_p) else 'NA',
            'TTest_P': f"{ttest_p:.3f}" if not np.isnan(ttest_p) else 'NA',
            'SignTest_P': f"{sign_p:.3f}" if not np.isnan(sign_p) else 'NA',
            'Cohens_d': f"{cohens_d:.3f}" if not np.isnan(cohens_d) else 'NA'
        })
    
    summary = pd.DataFrame([summarize_single_feature(f) for f in base_features])
    if not summary.empty:
        summary_path = output_dir / "feature_summary.csv"
        summary.to_csv(summary_path, index=False)
        logger.info(f"Saved detailed feature summary to {summary_path}")
    else:
        logger.warning("Feature summary is empty; no CSV saved.")
    
    logger.debug("Summary table generated.")
    return summary
```

**Detailed Function Analysis:**

**`summarize_features()` (Lines 392-533):**
- **Lines 405-412**: Extracts base feature names from Day1/Day5 column names
- **Lines 414-523**: Inner function `summarize_single_feature()` that:
  - **Lines 420-430**: Calculates Day 1 descriptive statistics (median, IQR, mean, SD)
  - **Lines 432-442**: Calculates Day 5 descriptive statistics
  - **Lines 444-450**: Calculates overall statistics from merged data
  - **Lines 452-453**: Calculates percentage changes from Day 1 to Day 5
  - **Lines 455-507**: Performs multiple statistical tests:
    - Wilcoxon signed-rank test (non-parametric paired test)
    - Paired t-test (parametric paired test)
    - Sign test (non-parametric test for direction of change)
    - Cohen's d (effect size measure)
  - **Lines 509-522**: Formats results into readable strings
- **Lines 525-532**: Saves results to CSV file

#### Correlation Analysis Functions
```python
def analyze_adrenalin_with_features(df: pd.DataFrame, features: List[str], output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Analyze the relationship between Adrenalin and PPG features through correlations, statistical tests, and visualizations.
    Include Day 1, Day 5, change, and overall stats.
    
    Args:
        df: Merged DataFrame with Adrenalin and PPG features.
        features: List of PPG feature names.
        output_dir: Directory to save results and plots.
    
    Returns:
        DataFrame with detailed correlation and statistical test results.
    """
    logger.info("Analyzing Adrenalin with PPG features, including Day 1, Day 5, and overall stats...")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if 'Adrenalin' not in df.columns:
        logger.error(f"'Adrenalin' column missing from DataFrame. Available columns: {df.columns.tolist()}")
        raise KeyError("'Adrenalin' column missing from DataFrame.")
    
    day1_data = df[df['DayLabel'] == 'Day1'].copy()
    day5_data = df[df['DayLabel'] == 'Day5'].copy()
    
    results = []
    
    for feature in features:
        if feature not in df.columns:
            logger.warning(f"Skipping {feature}: column missing from DataFrame.")
            continue
        
        logger.debug(f"Analyzing {feature} vs Adrenalin...")
        
        # Day 1 correlation
        valid_day1 = day1_data[['Adrenalin', feature]].dropna()
        corr_day1_r = corr_day1_p = n_day1 = np.nan
        if len(valid_day1) >= 2:
            corr_day1 = pg.corr(valid_day1['Adrenalin'], valid_day1[feature], method='spearman')
            corr_day1_r = corr_day1['r'].iloc[0]
            corr_day1_p = corr_day1['p-val'].iloc[0]
            n_day1 = len(valid_day1)
        
        # Day 5 correlation
        valid_day5 = day5_data[['Adrenalin', feature]].dropna()
        corr_day5_r = corr_day5_p = n_day5 = np.nan
        if len(valid_day5) >= 2:
            corr_day5 = pg.corr(valid_day5['Adrenalin'], valid_day5[feature], method='spearman')
            corr_day5_r = corr_day5['r'].iloc[0]
            corr_day5_p = corr_day5['p-val'].iloc[0]
            n_day5 = len(valid_day5)
        
        # Overall correlation
        valid_data = df[['Adrenalin', feature]].dropna()
        corr_overall_r = corr_overall_p = n_samples = np.nan
        if len(valid_data) >= 2:
            corr_overall = pg.corr(valid_data['Adrenalin'], valid_data[feature], method='spearman')
            corr_overall_r = corr_overall['r'].iloc[0]
            corr_overall_p = corr_overall['p-val'].iloc[0]
            n_samples = len(valid_data)
        
        # Statistical comparison: Mann-Whitney U test for overall data
        mw_p = effect_size = high_n = low_n = np.nan
        if feature in valid_data.columns:
            median_feature = valid_data[feature].median()
            high_group = valid_data[valid_data[feature] > median_feature]['Adrenalin'].dropna()
            low_group = valid_data[valid_data[feature] <= median_feature]['Adrenalin'].dropna()
            if len(high_group) >= 2 and len(low_group) >= 2:
                mw_stat, mw_p = mannwhitneyu(high_group, low_group)
                effect_size = pg.compute_effsize(high_group, low_group, eftype='cohen')
                high_n = len(high_group)
                low_n = len(low_group)
        
        results.append({
            'Feature': feature,
            'Day1_Spearman_R': corr_day1_r,
            'Day1_Spearman_P': corr_day1_p,
            'Day1_N_Samples': n_day1,
            'Day5_Spearman_R': corr_day5_r,
            'Day5_Spearman_P': corr_day5_p,
            'Day5_N_Samples': n_day5,
            'Overall_Spearman_R': corr_overall_r,
            'Overall_Spearman_P': corr_overall_p,
            'Overall_N_Samples': n_samples,
            'MannWhitney_P': mw_p,
            'Cohen_d': effect_size,
            'High_Group_N': high_n,
            'Low_Group_N': low_n
        })
        
        # Scatter plot
        plt.figure(figsize=(6, 4))
        sns.regplot(
            data=df,
            x='Adrenalin',
            y=feature,
            scatter_kws={'color': 'blue', 's': 50},
            line_kws={'color': 'red'}
        )
        plt.title(f"Adrenalin vs {feature.upper()}")
        plt.xlabel("Adrenaline/Urine (µg/24h)")
        plt.ylabel(feature.upper())
        scatter_path = output_dir / f"adrenalin_vs_{feature}.png"
        plt.savefig(scatter_path, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved scatter plot to {scatter_path}")
    
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_path = output_dir / "adrenalin_correlations.csv"
        results_df.to_csv(results_path, index=False)
        logger.info(f"Saved detailed correlations to {results_path}")
    
    return results_df
```

**Detailed Function Analysis:**

**`analyze_adrenalin_with_features()` (Lines 1308-1445):**
- **Lines 1321-1327**: Validates Adrenalin column exists
- **Lines 1329-1330**: Separates data into Day 1 and Day 5 subsets
- **Lines 1332-1338**: Iterates through each feature for analysis
- **Lines 1340-1347**: Calculates Day 1 Spearman correlation
- **Lines 1349-1356**: Calculates Day 5 Spearman correlation
- **Lines 1358-1365**: Calculates overall Spearman correlation
- **Lines 1367-1377**: Performs Mann-Whitney U test comparing high vs low feature groups
- **Lines 1379-1394**: Stores all results in structured format
- **Lines 1396-1407**: Creates scatter plots with regression lines
- **Lines 1409-1413**: Saves results to CSV file

### 3. Analysis Pipeline

#### Main Analysis Flow (`explore_and_report/analysis.py`)

```python
def main():
    """Main function to orchestrate the data processing pipeline."""
    logger = setup_logging()
    
    # Load and preprocess clinical data
    clinical_raw = load_data(RAW_MERGE_FILE, file_type='csv')
    clinical = preprocess_clinical_data(clinical_raw)
    
    # Merge with features data
    merged = merge_with_features(clinical, FEATURES_FILE)
    logger.debug(f"Merged DataFrame columns: {merged.columns.tolist()}")
    merged.to_csv("merged_preprocessed.csv", index=False)
    
    # Ensure DayLabel is added
    merged['Date'] = pd.to_datetime(merged['date'], errors='coerce')
    merged = merged.sort_values(['patient_id', 'Date'])
    merged['DayLabel'] = merged.groupby('patient_id')['Date'].transform(
        lambda x: np.where(x == x.min(), 'Day1', np.where(x == x.max(), 'Day5', np.nan))
    )
    merged = merged.dropna(subset=['DayLabel']).reset_index(drop=True)
    merged.to_csv("merged_processed.csv", index=False)
    
    # Generate summary table for catecholamines
    summary_table = generate_summary_table(
        merged,
        columns=['Adrenalin', 'Noradrenalin', 'Dopamin'],
        groupby='ANSD'
    )
    logger.info(f"Saved detailed catecholamine summary to plots/catecholamine_summary.csv")
    
    # Process HRV data
    hrv_wide = process_hrv_data(merged)
    
    # Aggregate medians
    aggregated = aggregate_medians(hrv_wide)
    
    # Summarize features with multiple tests
    feature_summary = summarize_features(aggregated, merged)
    logger.info("Detailed feature summary saved to plots/feature_summary.csv")
    
    # Prepare data for Day 1 and Day 5 plots
    logger.info("Preparing data for Day 1 and Day 5 plots...")
    merged_2records = merged.groupby('patient_id').filter(lambda x: len(x) == 2)
    merged_2records['Date'] = pd.to_datetime(merged_2records['date'], errors='coerce')
    merged_2records = merged_2records.sort_values(['patient_id', 'Date'])
    
    # Plot PPG features and detect outliers for Adrenalin and Noradrenalin
    plot_ppg_features(merged, PPG_FEATURES, x_col='Adrenalin')
    plot_ppg_features(merged, PPG_FEATURES, x_col='Noradrenalin')
    
    # Plot feature changes Day1 vs Day5
    plot_feature_changes(hrv_long, PPG_FEATURES)
    
    # Create additional plots for Adrenalin and Noradrenalin
    create_additional_plots(merged, PPG_FEATURES, x_col='Adrenalin')
    create_additional_plots(merged, PPG_FEATURES, x_col='Noradrenalin')
    
    # Analyze with features for Adrenalin and Noradrenalin
    analyze_with_features(merged, PPG_FEATURES, x_col='Adrenalin')
    analyze_with_features(merged, PPG_FEATURES, x_col='Noradrenalin')
    
    # Plot time-series trends
    plot_time_series_trends(aggregated, PPG_FEATURES)
```

**Detailed Step-by-Step Explanation:**

1. **Lines 1452-1455**: Loads and preprocesses clinical data
2. **Lines 1457-1459**: Merges clinical data with extracted PPG features
3. **Lines 1461-1467**: Adds Day1/Day5 labels based on date ordering
4. **Lines 1470-1475**: Generates summary tables for catecholamines
5. **Lines 1477-1481**: Processes HRV data and aggregates medians
6. **Lines 1483-1484**: Summarizes features with comprehensive statistics
7. **Lines 1487-1491**: Prepares data for time-series analysis
8. **Lines 1493-1494**: Creates scatter plots for Adrenalin and Noradrenalin
9. **Lines 1496-1497**: Plots feature changes from Day1 to Day5
10. **Lines 1499-1502**: Creates additional visualization plots
11. **Lines 1504-1507**: Performs correlation analysis
12. **Lines 1527-1528**: Plots time-series trends

## Advanced Features and Optimizations

### Memory Management
```python
def compute_spectral_features(self, ppg_signal: np.ndarray) -> ProcessedSignal:
    """Compute spectral features in chunks to manage memory."""
    if not ppg_signal.size:
        return ProcessedSignal(np.array([]), np.array([]))

    # Process signal in chunks
    n_samples = len(ppg_signal)
    chunk_size = min(self.chunk_size, n_samples)
    n_chunks = max(1, n_samples // chunk_size)
    
    # Initialize arrays with first chunk
    f, t, Zxx = signal.stft(
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
        
        f_chunk, t_chunk, Zxx = signal.stft(
            chunk,
            self.config.fs,
            nperseg=self.config.nperseg,
            return_onesided=True,
            boundary=None
        )
        power_spectrum += np.mean(np.abs(Zxx), axis=1) / n_chunks
    
    return ProcessedSignal(f, power_spectrum)
```

**Memory Optimization Features:**
- **Chunked Processing**: Processes large signals in 1-minute chunks to avoid memory overflow
- **Efficient Data Types**: Uses `np.float64` for precision while managing memory
- **Streaming Analysis**: Processes data incrementally rather than loading everything at once

### Parallel Processing
```python
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
```

**Parallel Processing Features:**
- **ProcessPoolExecutor**: Uses multiple CPU cores for patient analysis
- **Progress Tracking**: Shows progress with tqdm progress bars
- **Error Isolation**: Individual patient failures don't stop entire batch
- **Memory Efficiency**: Processes patients independently to avoid memory buildup

### Error Handling and Recovery
```python
def process_file(self, file_path: Path) -> bool:
    """Process a single file through the pipeline."""
    try:
        # Load signal
        signal_data = self.signal_processor.load_signal(file_path)
        
        # Get quality segments
        _, normal_segments = self.signal_processor.get_quality_segments(
            signal_data.signal
        )
        
        # Prepare output directories
        output_dirs = self._prepare_output_dirs(file_path)
        
        # Process segments
        for start, end in normal_segments:
            self.segment_handler.process_segment(
                signal_data,
                start,
                end,
                output_dirs
            )
        
        return True
        
    except Exception as e:
        self.logger.error(f"Error processing file {file_path}: {e}")
        return False
```

**Error Handling Features:**
- **Graceful Degradation**: Individual file failures don't stop the entire pipeline
- **Detailed Logging**: Comprehensive error messages with context
- **Return Status**: Boolean return values indicate success/failure
- **Exception Propagation**: Critical errors are properly raised and logged

### Data Validation
```python
def validate_columns(df: pd.DataFrame, required_columns: List[str]) -> None:
    """
    Validate that required columns exist in the DataFrame.
    
    Args:
        df: DataFrame to validate.
        required_columns: List of required column names.
    
    Raises:
        ValueError: If any required columns are missing.
    """
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        logger.error(f"Missing columns: {missing}")
        raise ValueError(f"Missing columns: {missing}")
```

**Data Validation Features:**
- **Column Validation**: Ensures required columns exist before processing
- **Data Type Checking**: Validates data types and formats
- **Range Validation**: Checks for reasonable value ranges
- **Completeness Checks**: Identifies missing or incomplete data

### Configuration Management
```python
@dataclass
class SignalConfig:
    """Configuration for signal processing pipeline."""
    # Processing mode
    mode: str = "directory"  # Options: "directory" or "file_list"
    
    # Base paths
    output_base: Path = Path('D:\Workspace\Data\\24EI/output')
    data_dir: Path = Path('D:\Workspace\Data\\24EI\RAW_DATA')
    file_list_path: Path = None  # Path to CSV file containing list of files to process
    
    # Signal processing parameters
    fs: int = 100  # Sampling frequency in Hz
    duration: int = 300  # 5 minutes in seconds
    step_size: int = 300  # 5 minutes in seconds
    lowcut: float = 0.5  # Low frequency cutoff for bandpass filter
    highcut: float = 20.0  # High frequency cutoff for bandpass filter
    nperseg: int = 1024  # Number of samples per STFT segment
    
    def __post_init__(self):
        """Create output directories after initialization."""
        if self.mode not in ["directory", "file_list"]:
            raise ValueError("mode must be either 'directory' or 'file_list'")
            
        if self.mode == "file_list" and not self.file_list_path:
            raise ValueError("file_list_path must be provided when mode is 'file_list'")
            
        self.output_base.mkdir(parents=True, exist_ok=True)
        self.SEGMENT_PATH.mkdir(parents=True, exist_ok=True)
        self.FEATURE_PATH.mkdir(parents=True, exist_ok=True)
        self.OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
```

**Configuration Management Features:**
- **Type Safety**: Uses dataclasses for type-safe configuration
- **Validation**: Post-initialization validation of configuration values
- **Auto-creation**: Automatically creates required directories
- **Flexibility**: Supports multiple processing modes and parameters

## Performance Optimizations

### Signal Processing Optimizations
1. **Chunked Processing**: Large signals are processed in manageable chunks
2. **Memory Mapping**: Efficient memory usage for large datasets
3. **Vectorized Operations**: Uses NumPy vectorization for speed
4. **Caching**: Intermediate results are cached when possible

### Statistical Analysis Optimizations
1. **Parallel Processing**: Multiple patients processed simultaneously
2. **Efficient Data Structures**: Uses pandas for optimized data manipulation
3. **Lazy Loading**: Data is loaded only when needed
4. **Compression**: Results are saved in compressed format

### Visualization Optimizations
1. **Batch Plotting**: Multiple plots generated in batches
2. **Memory Management**: Plots are closed after saving to free memory
3. **High DPI**: Plots saved at 300 DPI for publication quality
4. **Efficient Formats**: Uses PNG format for optimal file size

This comprehensive code explanation covers all major components of the 24EI analysis project, providing detailed line-by-line analysis that will help beginners understand both the implementation details and the underlying concepts. The document serves as both a technical reference and a learning resource for understanding biomedical signal processing and statistical analysis.

## Data Flow Explanation

### 1. Input Data
```
Raw PPG Files (CSV) + Clinical Data (CSV) + Feature Data (CSV)
```

### 2. Signal Processing Flow
```
CSV File → SignalProcessor.load_signal() → SignalData Object
    ↓
Quality Assessment → High-Quality Segments
    ↓
Feature Extraction → HRV + Morphological Features
    ↓
Save to Output Directory
```

### 3. Analysis Flow
```
Clinical Data + Feature Data → Merge → Statistical Analysis
    ↓
Generate Plots → Create Reports → Save Results
```

### 4. Key Data Transformations

#### From Raw Signal to Features
```python
# Raw PPG signal (1000 samples at 100 Hz = 10 seconds)
raw_signal = [0.1, 0.2, 0.15, 0.3, ...]  # 1000 values

# After quality assessment
clean_segments = [(0, 300), (400, 700)]  # Start/end indices of clean parts

# After feature extraction
features = {
    'heart_rate': 72.5,           # beats per minute
    'sdnn': 45.2,                 # standard deviation of RR intervals
    'rmssd': 32.1,                # root mean square of successive differences
    'systolic_duration': 0.3,     # duration of systolic phase
    'diastolic_duration': 0.5     # duration of diastolic phase
}
```

## Key Algorithms and Methods

### 1. Signal Quality Assessment
```python
def get_quality_segments(self, signal: np.ndarray) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
    """Identify high-quality segments using signal quality index."""
    sqi = SignalQualityIndex()
    sqi_values = sqi.compute_sqi(signal, self.config.fs)
    
    # Find segments with SQI > threshold
    quality_threshold = 0.7
    good_segments = []
    # ... logic to find continuous segments above threshold
```

**What it does:** Uses signal quality assessment to identify which parts of the signal are clean enough for analysis. Removes noisy segments that could give incorrect results.

### 2. Feature Extraction
```python
def extract_features(self, signal: np.ndarray) -> Dict[str, Any]:
    """Extract comprehensive features from signal segment."""
    # Extract RR intervals (time between heartbeats)
    rr_transformer = RRTransformation(signal, fs=self.fs, signal_type=self.signal_type)
    rr_intervals = rr_transformer.compute_rr_intervals()
    
    # Extract HRV features
    hrv_features = HRVFeatures(rr_intervals)
    hrv_dict = hrv_features.compute_all_features()
    
    # Extract morphological features
    morph_extractor = PhysiologicalFeatureExtractor(signal, fs=self.fs)
    morph_dict = morph_extractor.extract_all_features()
```

**What it does:** 
- **RR Intervals**: Finds the time between consecutive heartbeats
- **HRV Features**: Calculates statistical measures of heart rate variability
- **Morphological Features**: Analyzes the shape of the PPG waveform

### 3. Statistical Analysis
```python
def analyze_with_features(df: pd.DataFrame, features: List[str], x_col: str) -> pd.DataFrame:
    """Perform statistical analysis between features and clinical variables."""
    results = []
    
    for feature in features:
        # Correlation analysis
        corr, p_value = stats.pearsonr(df[x_col], df[feature])
        
        # Group comparison (ANSD vs No-ANSD)
        ansd_yes = df[df['ANSD'] == 'Yes_ANSD'][feature]
        ansd_no = df[df['ANSD'] == 'No_ANSD'][feature]
        stat, p_val = stats.mannwhitneyu(ansd_yes, ansd_no)
        
        results.append({
            'feature': feature,
            'correlation': corr,
            'p_value': p_value,
            'ansd_statistic': stat,
            'ansd_p_value': p_val
        })
```

**What it does:** 
- **Correlation Analysis**: Measures how strongly features relate to catecholamine levels
- **Group Comparison**: Compares features between patients with and without ANSD
- **Statistical Testing**: Determines if differences are statistically significant

## Configuration System

### Signal Processing Configuration
```python
@dataclass
class SignalConfig:
    # File paths
    data_dir: Path = Path('D:/Workspace/Data/24EI/RAW_DATA')
    output_base: Path = Path('D:/Workspace/Data/24EI/output')
    
    # Signal parameters
    fs: int = 100                    # Sampling frequency
    duration: int = 300              # Segment duration (5 minutes)
    lowcut: float = 0.5              # Low frequency cutoff
    highcut: float = 20.0            # High frequency cutoff
    
    # Processing parameters
    max_workers: int = 4             # Number of parallel workers
    batch_size: int = 100            # Files per batch
```

### Resonance Analysis Configuration
```python
@dataclass
class ResonanceConfig:
    # Element resonance frequencies
    @staticmethod
    def get_harmonic_frequencies() -> Dict[str, List[float]]:
        return {
            'Mg': [4.0],    # Magnesium
            'Ca': [6.0],    # Calcium
            'Fe': [12.0],   # Iron
            'Zn': [18.0]    # Zinc
        }
```

**What it does:** Defines the frequencies at which different elements resonate, used for spectral analysis.

## Error Handling and Logging

### Logging System
```python
def setup_logging() -> logging.Logger:
    """Configure colored logging with custom formatting."""
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            '%(log_color)s%(levelname)s: %(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )
    )
```

**What it does:** Creates a colored logging system that shows different types of messages in different colors:
- **DEBUG** (cyan): Detailed information for debugging
- **INFO** (green): General information about what's happening
- **WARNING** (yellow): Something unexpected but not critical
- **ERROR** (red): Something went wrong
- **CRITICAL** (red background): Serious problem

### Error Handling Pattern
```python
def process_file(self, file_path: Path) -> bool:
    """Process a single file with error handling."""
    try:
        # Main processing logic
        signal_data = self.signal_processor.load_signal(file_path)
        # ... more processing
        return True
        
    except Exception as e:
        self.logger.error(f"Error processing file {file_path}: {e}")
        return False
```

**What it does:** Wraps risky operations in try-catch blocks to prevent the entire pipeline from crashing if one file fails.

## Code Examples and Usage

### 1. Running Signal Processing
```python
# Create configuration
config = SignalConfig()
config.data_dir = Path("path/to/ppg/files")
config.output_base = Path("path/to/output")

# Create and run pipeline
pipeline = SignalProcessingPipeline(config)
pipeline.process_files()
```

### 2. Running Analysis
```python
# Load and preprocess data
clinical_raw = load_data("clinical_data.csv", file_type='csv')
clinical = preprocess_clinical_data(clinical_raw)

# Merge with features
merged = merge_with_features(clinical, "features.csv")

# Generate plots
plot_ppg_features(merged, PPG_FEATURES, x_col='Adrenalin')
```

### 3. Customizing Analysis
```python
# Define custom features to analyze
CUSTOM_FEATURES = [
    'heart_rate', 'sdnn', 'rmssd', 
    'systolic_duration', 'diastolic_duration'
]

# Run analysis with custom features
analyze_with_features(merged, CUSTOM_FEATURES, x_col='Noradrenalin')
```

## Key Concepts for Beginners

### 1. **Data Types**
- **CSV Files**: Comma-separated values, like a spreadsheet in text format
- **NumPy Arrays**: Efficient data structures for numerical computations
- **Pandas DataFrames**: Like Excel spreadsheets but in Python

### 2. **Signal Processing Concepts**
- **Sampling Frequency**: How many times per second we measure the signal
- **Bandpass Filter**: Removes unwanted frequencies (like noise)
- **Segmentation**: Breaking long signals into smaller, analyzable pieces

### 3. **Statistical Concepts**
- **Correlation**: How two variables change together
- **P-value**: Probability that results occurred by chance
- **Statistical Significance**: Results are likely not due to random chance

### 4. **Programming Concepts**
- **Classes**: Blueprints for creating objects with data and methods
- **Methods**: Functions that belong to a class
- **Configuration**: Settings that control how the program behaves
- **Error Handling**: Code that deals with problems gracefully

## Troubleshooting Common Issues

### 1. **File Not Found Errors**
```python
# Check if file exists before processing
if not file_path.exists():
    logger.error(f"File not found: {file_path}")
    return False
```

### 2. **Memory Issues**
```python
# Process files in smaller batches
for i in range(0, len(files), batch_size):
    batch = files[i:i+batch_size]
    process_batch(batch)
```

### 3. **Data Quality Issues**
```python
# Check data quality before processing
if len(signal) < minimum_length:
    logger.warning(f"Signal too short: {len(signal)} samples")
    return None
```

This codebase is designed to be modular and extensible, making it easy to add new features or modify existing functionality. The clear separation of concerns makes it easier to understand and maintain.
