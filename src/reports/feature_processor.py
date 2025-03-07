# src/reports/feature_processor.py
from typing import Dict, Any
import pandas as pd
import numpy as np
from pathlib import Path
import logging

class FeatureProcessor:
    """Process and prepare features for report generation.
    
    This class handles the processing of feature data, including loading,
    preprocessing, and preparing the data for report generation.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def prepare_features(self, feature_data: pd.DataFrame) -> Dict[str, Any]:
        """Prepare features for report generation.
        
        Args:
            feature_data (pd.DataFrame): Raw feature data
            
        Returns:
            Dict[str, Any]: Processed features ready for report generation
            
        Raises:
            ValueError: If feature data is invalid or missing required columns
        """
        try:
            # Ensure start column is integer type
            feature_data['start'] = feature_data['start'].astype(int)
            feature_data = feature_data.sort_values(by='start')

            # Select all columns except the last n
            n = 3  # Number of columns to exclude
            selected_columns = feature_data.iloc[:, :-n]
            selected_columns = selected_columns.astype(float)

            # Convert to dictionary format
            return selected_columns.to_dict(orient='list')

        except Exception as e:
            self.logger.error(f"Error preparing features: {str(e)}")
            raise ValueError(f"Feature preparation failed: {str(e)}")