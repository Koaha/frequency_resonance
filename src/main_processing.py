# src/main_processing.py
import logging
import argparse
from pathlib import Path
from core.signal_processing import SignalProcessingPipeline, SignalConfig


def setup_logging(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(output_dir / "processing.log"),
        ],
    )


def parse_args():
    p = argparse.ArgumentParser(description="Signal processing pipeline")
    p.add_argument("--config", type=str, default=None,
                   help="Path to YAML config file (default: <project>/config.yaml)")
    p.add_argument("--mode", type=str, choices=["directory", "file_list"],
                   default=None, help="Processing mode")
    p.add_argument("--file-list", type=str, default=None,
                   help="CSV file listing files to process")
    p.add_argument("--data-dir", type=str, default=None,
                   help="Directory containing data files")
    p.add_argument("--output-dir", type=str, default=None,
                   help="Output directory")
    p.add_argument("--signal-column", type=str, default=None,
                   help="PPG signal column in OUCRU CSV (e.g. pleth, ir, red)")
    p.add_argument("--signal-type", type=str, default=None,
                   choices=["auto", "PPG", "ECG"],
                   help="Signal type: auto (detect from filename), PPG, or ECG")
    p.add_argument("--ecg-signal-column", type=str, default=None,
                   help="ECG signal column in CSV (default: ecg)")
    p.add_argument("--max-patients", type=int, default=0,
                   help="Process only the first N patient folders (0 = all)")
    return p.parse_args()


def main():
    args = parse_args()

    yaml_path = Path(args.config) if args.config else None

    overrides = {}
    if args.mode:
        overrides["mode"] = args.mode
    if args.output_dir:
        overrides["output_base"] = Path(args.output_dir)
    if args.data_dir:
        overrides["data_dir"] = Path(args.data_dir)
    if args.file_list:
        overrides["file_list_path"] = Path(args.file_list)
    if args.signal_column:
        overrides["signal_column"] = args.signal_column
    if args.signal_type:
        overrides["signal_type"] = args.signal_type
    if args.ecg_signal_column:
        overrides["ecg_signal_column"] = args.ecg_signal_column

    if yaml_path:
        config = SignalConfig.from_yaml(yaml_path, **overrides)
    else:
        config = SignalConfig.from_yaml(**overrides)

    setup_logging(config.output_base)
    logger = logging.getLogger(__name__)
    logger.info(f"Config: signal_type={config.signal_type}, "
                f"ppg_column={config.signal_column}, ecg_column={config.ecg_signal_column}, "
                f"fs={config.fs}, duration={config.duration}s, data_dir={config.data_dir}")

    try:
        pipeline = SignalProcessingPipeline(config)
        pipeline.process_files(max_patients=args.max_patients)
        logger.info("Processing completed successfully")
        logger.info(f"Outputs written under {config.output_base} (mirroring data_dir hierarchy, one folder per file)")
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise


if __name__ == "__main__":
    main()
