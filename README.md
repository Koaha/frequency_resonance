# Frequency Resonance

Signal processing pipeline for PPG (photoplethysmography) data from OUCRU SmartCare pulse-oximeters. Computes signal quality indices (SQI), RR intervals, and optionally HRV / morphology features, driven entirely by a single `config.yaml`.

Built on [vitalDSP](https://github.com/Oucru-Innovations/vital-DSP).

## Project Structure

```
frequency_resonance/
├── config.yaml                  # Single source of truth for all settings
├── data/                        # Input data (OUCRU SmartCare CSV files)
├── output/                      # Generated outputs
│   ├── sqi/                     #   Per-file SQI JSON + summary
│   ├── rr_intervals/            #   Per-file RR JSON + per-segment .txt
│   ├── segments/                #   Per-segment signal CSVs
│   └── features/                #   Per-segment feature CSVs (optional)
├── scripts/
│   ├── run_processing.sh        # Bash wrapper (Linux/Mac/Git Bash)
│   ├── run_processing.bat       # Windows Task Scheduler wrapper
│   └── install_cron.sh          # One-liner to install a crontab entry
├── src/
│   ├── main_processing.py       # CLI entry point
│   ├── main_resonance.py        # Resonance analysis entry point
│   ├── main_report.py           # Report generation entry point
│   ├── config/
│   │   └── settings.py          # Central YAML loader (load_config / resolve_path)
│   ├── core/
│   │   ├── signal_processing/   # SQI, RR, segmentation, feature extraction
│   │   └── resonance/           # Frequency resonance analysis
│   ├── reports/                 # Report generation
│   └── utils/
├── explore_and_report/          # Exploratory analysis notebooks & scripts
└── archived/                    # Legacy / old-project code (not used)
```

## Quick Start

### 1. Install dependencies

```bash
pip install vitalDSP pyyaml pandas numpy tqdm
```

### 2. Place data

Put OUCRU SmartCare CSV files in `data/` (or change `data_dir` in `config.yaml`).

### 3. Run

```bash
cd src
python main_processing.py
```

Outputs land in `output/sqi/`, `output/rr_intervals/`, and `output/segments/`.

## Configuration

Everything is controlled by `config.yaml` at the project root. No source code changes needed.

### Key settings

| Setting | Default | Description |
|---|---|---|
| `data_dir` | `data` | Input directory (relative to project root) |
| `output_dir` | `output` | Output directory |
| `signal_column` | `pleth` | Column to extract: `pleth`, `ir`, or `red` |
| `data_format` | `OUCRU_CSV` | Data loader format (vitalDSP `DataFormat`) |
| `sampling_rate` | `100` | Sampling rate in Hz |
| `segment_duration` | `300` | Window size in seconds (5 min) |
| `step_size` | `300` | Step between windows in seconds |
| `primary_sqi` | `signal_entropy_sqi` | SQI metric used to select segments for processing |
| `extract_features` | `false` | Enable HRV + morphology extraction (slow, ~2 min/segment) |

### Per-SQI thresholds

Each SQI metric has its own `threshold`, `threshold_type`, and `enabled` flag:

```yaml
sqi:
  signal_entropy_sqi:
    enabled: true
    threshold: -2
    threshold_type: below    # below | above | range

  snr_sqi:
    enabled: true
    threshold: -1.5
    threshold_type: below

  kurtosis_sqi:
    enabled: false           # skip this metric
    threshold: -2
    threshold_type: below
```

### CLI overrides

Any config value can be overridden from the command line:

```bash
python main_processing.py --signal-column ir --data-dir /other/data --output-dir /other/output
python main_processing.py --config /path/to/custom_config.yaml
```

## Outputs

### SQI JSON (`output/sqi/<filename>_sqi.json`)

Per-file signal quality assessment with all enabled SQI metrics:

```json
{
  "file": "SmartCareCsv_62EI-067-005_....csv",
  "total_samples": 294100,
  "total_duration_seconds": 2941.0,
  "sampling_rate": 100,
  "primary_sqi": "signal_entropy_sqi",
  "segments": [
    {
      "segment_index": 0,
      "window_index": 0,
      "start_sample": 0,
      "end_sample": 30000,
      "length_samples": 30000,
      "length_seconds": 300.0,
      "primary_sqi_quality": "normal",
      "quality_by_sqi": {
        "signal_entropy_sqi": "normal",
        "snr_sqi": "normal",
        "kurtosis_sqi": "abnormal",
        "...": "..."
      }
    }
  ],
  "sqi_metrics": {
    "signal_entropy_sqi": {
      "threshold": -2,
      "threshold_type": "below",
      "values": [0.54, -0.95, ...],
      "quality": ["normal", "normal", ...]
    }
  }
}
```

Each segment shows:
- `primary_sqi_quality` — the decision from the primary SQI (drives RR/feature extraction)
- `quality_by_sqi` — per-metric normal/abnormal label at that window index

### RR Intervals (`output/rr_intervals/`)

- `<filename>_rr.json` — summary per segment (count, mean, std, full interval list)
- `<filename>/<segment>_rr.txt` — raw RR intervals in ms (one per line)

### Segments (`output/segments/`)

Per-segment CSV files with `timestamp` and `signal` columns.

### Features (`output/features/`) — optional

Per-segment HRV + morphology feature CSVs. Only generated when `extract_features: true`.

### Summary (`output/sqi/sqi_summary.json`)

Array of all per-file SQI results in a single file.

## Available SQI Metrics

All metrics from vitalDSP's `SignalQualityIndex`:

| Metric | Description |
|---|---|
| `signal_entropy_sqi` | Signal entropy (complexity/predictability) |
| `snr_sqi` | Signal-to-noise ratio |
| `kurtosis_sqi` | Distribution kurtosis |
| `skewness_sqi` | Distribution skewness |
| `zero_crossing_sqi` | Zero-crossing rate |
| `energy_sqi` | Signal energy |
| `amplitude_variability_sqi` | Amplitude variability |
| `baseline_wander_sqi` | Baseline wander |
| `peak_to_peak_amplitude_sqi` | Peak-to-peak amplitude |
| `ppg_signal_quality_sqi` | PPG-specific quality |
| `respiratory_signal_quality_sqi` | Respiratory signal quality |

## Scheduled / Cron Execution

The `scripts/` folder contains ready-made wrappers so the pipeline can run unattended on a schedule. Each script auto-detects the project root, activates a virtualenv if present, and logs output.

### Linux / macOS / Git Bash

Run once manually:

```bash
./scripts/run_processing.sh                       # default config.yaml
./scripts/run_processing.sh /path/to/custom.yaml  # custom config
```

Install a crontab entry (daily at 02:00 by default):

```bash
./scripts/install_cron.sh

# Or pick a custom schedule (every 6 hours):
CRON_SCHEDULE="0 */6 * * *" ./scripts/install_cron.sh
```

The helper appends one line to your crontab and logs to `output/cron.log`. To remove it later: `crontab -e` and delete the `# frequency_resonance` line.

Common cron schedules for reference:

| Schedule | Cron expression |
|---|---|
| Every day at 02:00 | `0 2 * * *` |
| Every 6 hours | `0 */6 * * *` |
| Every Monday at 06:00 | `0 6 * * 1` |
| Every hour | `0 * * * *` |

### Windows (Task Scheduler)

Run once manually from Command Prompt:

```cmd
scripts\run_processing.bat
scripts\run_processing.bat C:\path\to\custom.yaml
```

To schedule via Task Scheduler:

1. Open **Task Scheduler** and click **Create Basic Task**.
2. Set the trigger (e.g. Daily, 02:00).
3. Action: **Start a program**.
4. Program/script: full path to `scripts\run_processing.bat`
   (e.g. `D:\Workspace\frequency_resonance\scripts\run_processing.bat`).
5. Start in: `D:\Workspace\frequency_resonance\scripts`
6. Finish.

Logs are written to `output/processing.log` and console output appears in the Task Scheduler history.

## Other Entry Points

```bash
cd src
python main_resonance.py       # Frequency resonance analysis
python main_report.py          # Report generation from processed features
```

## Dependencies

- [vitalDSP](https://github.com/Oucru-Innovations/vital-DSP) (>= 0.1.5) — signal loading, SQI, RR extraction, HRV, morphology
- PyYAML
- pandas, numpy, tqdm
