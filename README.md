# 24EI Analysis Project

This project contains signal processing and analysis pipelines for PPG (Photoplethysmography) data analysis, focusing on heart rate variability (HRV) features and catecholamine correlations.

## Project Structure

```
24EIa/
├── src/                          # Main analysis pipeline
│   ├── main_processing.py        # Signal processing pipeline
│   ├── main_resonance.py         # Resonance analysis
│   ├── main_report.py            # Report generation
│   ├── core/                     # Core processing modules
│   ├── analysis/                 # Analysis modules
│   └── reports/                  # Report generation modules
├── explore_and_report/           # Data exploration and reporting
│   ├── analysis.py               # Main analysis script
│   ├── analyze_new.py            # Alternative analysis script
│   ├── markdown_report.py        # Markdown report generation
│   └── plots/                    # Generated plots and visualizations
├── data/                         # Input data directory
├── output/                       # Processing outputs
└── plots/                        # Generated plots
```

## Prerequisites

### Python Dependencies

Install the required Python packages:

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
pip install statsmodels pingouin tableone colorlog
pip install vitalDSP  # For signal quality assessment
pip install openpyxl  # For Excel file support
```

### Required Data Files

Ensure you have the following data files in the project root:
- `24EI+03TS-raw-merge(in).csv` - Clinical data
- `features_24EI_compiled.csv` - Compiled feature data
- `ppg_files.csv` - PPG file list (if using file list mode)

## Running the Analysis

### 1. Signal Processing Pipeline (`src/`)

The main processing pipeline extracts features from PPG signals and performs quality assessment.

#### Directory Mode (Recommended)
Process all files in a directory:

```bash
cd src
python main_processing.py --mode directory --data-dir ../data --output-dir ../output
```

#### File List Mode
Process specific files from a CSV list:

```bash
cd src
python main_processing.py --mode file_list --file-list ../ppg_files.csv --output-dir ../output
```

#### Resonance Analysis
Run resonance analysis on processed data:

```bash
cd src
python main_resonance.py
```

#### Report Generation
Generate reports from processed features:

```bash
cd src
python main_report.py
```

### 2. Data Exploration and Reporting (`explore_and_report/`)

The exploration module performs statistical analysis and generates comprehensive reports.

#### Main Analysis
Run the complete analysis pipeline:

```bash
cd explore_and_report
python analysis.py
```

This will:
- Load and preprocess clinical data
- Merge with feature data
- Generate HRV analysis
- Create summary tables
- Generate plots for PPG features
- Analyze catecholamine correlations

#### Alternative Analysis
Run the alternative analysis script:

```bash
cd explore_and_report
python analyze_new.py
```

#### Markdown Report Generation
Generate markdown reports:

```bash
cd explore_and_report
python markdown_report.py
```

## Output Files

### Processing Outputs (`src/`)
- `output/features/` - Extracted feature files
- `output/segments/` - Processed signal segments
- `output/reports/` - Generated reports
- `output/resonance_analysis/` - Resonance analysis results
- `compile_feature_data.csv` - Compiled feature data

### Analysis Outputs (`explore_and_report/`)
- `plots/` - Generated visualizations organized by feature type
- `summaries/` - Statistical summary tables
- `analysis_report.html` - HTML report
- `analysis_report.pdf` - PDF report
- `analysis_report.md` - Markdown report
- `merged_preprocessed.csv` - Preprocessed merged data
- `merged_processed.csv` - Final processed data

## Key Features Analyzed

### PPG Features
- Heart rate variability (HRV) metrics
- Systolic and diastolic characteristics
- Signal quality and morphology
- Time and frequency domain features

### Clinical Correlations
- Catecholamine levels (Adrenalin, Noradrenalin, Dopamin)
- ANSD (Autonomic Nervous System Dysfunction) analysis
- Day 1 vs Day 5 comparisons
- Statistical significance testing

## Configuration

### Signal Processing Configuration
The processing pipeline uses configuration classes:
- `SignalConfig` - Signal processing parameters
- `ResonanceConfig` - Resonance analysis parameters
- `ReportConfig` - Report generation parameters

### Analysis Parameters
Key parameters in `analysis.py`:
- `RAW_MERGE_FILE` - Clinical data file
- `FEATURES_FILE` - Feature data file
- `PPG_FEATURES` - List of PPG features to analyze
- `CLINICAL_COLUMNS` - Clinical variables of interest

## Troubleshooting

### Common Issues

1. **Missing Data Files**
   - Ensure all required CSV/Excel files are in the correct locations
   - Check file paths in configuration

2. **Import Errors**
   - Install all required dependencies
   - Ensure Python path includes the project directory

3. **Memory Issues**
   - Process data in smaller batches
   - Use file list mode instead of directory mode for large datasets

4. **Plot Generation Errors**
   - Ensure output directories exist
   - Check matplotlib backend configuration

### Logging

All modules generate detailed logs:
- `src/logs/` - Processing logs
- `output/resonance_analysis/resonance_analysis.log` - Resonance analysis logs
- `output/report_generation.log` - Report generation logs

## Development

### Adding New Features
1. Add feature extraction logic in `src/core/signal_processing/`
2. Update feature lists in analysis scripts
3. Add visualization functions in `explore_and_report/`

### Customizing Analysis
1. Modify `PPG_FEATURES` list for different feature sets
2. Update `CLINICAL_COLUMNS` for different clinical variables
3. Adjust statistical tests in analysis functions

## Support

For issues or questions:
1. Check the logs for detailed error messages
2. Verify all dependencies are installed
3. Ensure data files are in the correct format and location
