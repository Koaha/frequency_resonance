# src/main_resonance.py
import logging
from pathlib import Path
from core.resonance import ResonanceAnalyzer, ResonanceConfig

def setup_logging(config: ResonanceConfig) -> None:
    """Configure logging for resonance analysis."""
    # Create output directory if it doesn't exist
    config.OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    
    log_file = config.OUTPUT_PATH / 'resonance_analysis.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file)
        ]
    )

def main():
    """Main entry point for resonance analysis."""
    # Initialize configuration
    config = ResonanceConfig()
    
    # Create all required directories
    config.OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    config.PLOT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Setup logging
    setup_logging(config)
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize and run analyzer
        analyzer = ResonanceAnalyzer(config)
        results_df = analyzer.analyze_all_patients()
        
        logger.info("Resonance analysis completed successfully")
        logger.info(f"Results saved to {config.MASTER_CSV}")
        
    except Exception as e:
        logger.error(f"Resonance analysis failed: {e}")
        raise

if __name__ == "__main__":
    main()