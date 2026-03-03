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
                   help="Signal column in OUCRU CSV (e.g. pleth, ir, red)")
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

    if yaml_path:
        config = SignalConfig.from_yaml(yaml_path, **overrides)
    else:
        config = SignalConfig.from_yaml(**overrides)

    setup_logging(config.output_base)
    logger = logging.getLogger(__name__)
    logger.info(f"Config: signal_column={config.signal_column}, fs={config.fs}, "
                f"duration={config.duration}s, data_dir={config.data_dir}")

    try:
        pipeline = SignalProcessingPipeline(config)
        pipeline.process_files()
        logger.info("Processing completed successfully")
        logger.info(f"SQI  JSONs -> {config.sqi_dir}")
        logger.info(f"RR   JSONs -> {config.rr_dir}")
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise


if __name__ == "__main__":
    main()
