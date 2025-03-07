import unittest
import numpy as np
import pandas as pd
import os
from unittest.mock import patch, MagicMock
from src.analysis.quality_assurance_and_segmentation_nonin import get_normal_segment

class TestGetNormalSegment(unittest.TestCase):
    pass
def test_get_normal_segment_creates_folders(self):
    # Mock input data
    signal_col = np.array([1, 2, 3, 4, 5])
    date_col = np.array(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'])
    segment_folder = '/tmp/test_segment'
    rr_folder = '/tmp/test_rr'
    feats_folder = '/tmp/test_feats'
    file_path = '/tmp/test_file.csv'

    # Ensure folders don't exist initially
    for folder in [segment_folder, rr_folder, feats_folder]:
        if os.path.exists(folder):
            os.rmdir(folder)

    # Mock SignalQualityIndex to avoid actual computation
    with patch('src.analysis.quality_assurance_and_segmentation_nonin.SignalQualityIndex') as mock_sqi:
        mock_sqi.return_value.signal_entropy_sqi.return_value = (None, [], None)

        # Call the function
        get_normal_segment(signal_col, date_col, segment_folder, rr_folder, feats_folder, file_path)

        # Check if folders were created
        self.assertTrue(os.path.exists(segment_folder))
        self.assertTrue(os.path.exists(rr_folder))
        self.assertTrue(os.path.exists(feats_folder))

    # Clean up
    for folder in [segment_folder, rr_folder, feats_folder]:
        if os.path.exists(folder):
            os.rmdir(folder)
def test_get_normal_segment_empty_inputs(self):
    signal_col = []
    date_col = []
    segment_folder = 'test_segment_folder'
    rr_folder = 'test_rr_folder'
    feats_folder = 'test_feats_folder'
    file_path = 'test_file.csv'

    with patch('os.path.exists', return_value=False), \
         patch('os.makedirs') as mock_makedirs, \
         patch('src.analysis.quality_assurance_and_segmentation_nonin.SignalQualityIndex') as mock_sqi:

        mock_sqi_instance = MagicMock()
        mock_sqi_instance.signal_entropy_sqi.return_value = ([], [], [])
        mock_sqi.return_value = mock_sqi_instance

        result = get_normal_segment(signal_col, date_col, segment_folder, rr_folder, feats_folder, file_path)

        self.assertEqual(result, ([], []), "Expected empty lists for empty inputs")
        mock_makedirs.assert_any_call(segment_folder, exist_ok=True)
        mock_makedirs.assert_any_call(rr_folder, exist_ok=True)
        mock_makedirs.assert_any_call(feats_folder, exist_ok=True)
        mock_sqi.assert_called_once_with([])
        mock_sqi_instance.signal_entropy_sqi.assert_called_once_with(
            window_size=22500, step_size=2250, threshold=-2, threshold_type='below'
        )
def test_get_normal_segment_extracts_normal_segments(self):
    # Mock input data
    signal_col = np.random.rand(10000)
    date_col = pd.date_range(start='2023-01-01', periods=10000, freq='10ms')
    segment_folder = '/tmp/test_segment'
    rr_folder = '/tmp/test_rr'
    feats_folder = '/tmp/test_feats'
    file_path = '/tmp/test_file.csv'

    # Mock SignalQualityIndex
    with patch('src.analysis.quality_assurance_and_segmentation_nonin.SignalQualityIndex') as mock_sqi:
        mock_sqi_instance = MagicMock()
        mock_sqi_instance.signal_entropy_sqi.return_value = (
            [1, -3, 2, -4],  # SQI values
            [(1000, 2000), (3000, 4000)],  # Normal segments
            [(0, 1000), (2000, 3000)]  # Abnormal segments
        )
        mock_sqi.return_value = mock_sqi_instance

        # Mock other dependencies
        with patch('src.analysis.quality_assurance_and_segmentation_nonin.RRTransformation'):
            with patch('src.analysis.quality_assurance_and_segmentation_nonin.HRVFeatures'):
                with patch('src.analysis.quality_assurance_and_segmentation_nonin.PhysiologicalFeatureExtractor'):
                    with patch('pandas.DataFrame.to_csv'):
                        with patch('numpy.savetxt'):
                            # Call the function
                            normal_signal, date_col_normal = get_normal_segment(
                                signal_col, date_col, segment_folder, rr_folder, feats_folder, file_path
                            )

    # Assert that the function correctly identified normal segments
    self.assertEqual(len(normal_signal), 2)
    self.assertEqual(len(date_col_normal), 2)
    self.assertEqual(len(normal_signal[0]), 1000)  # First normal segment
    self.assertEqual(len(normal_signal[1]), 1000)  # Second normal segment
    self.assertEqual(len(date_col_normal[0]), 1000)
    self.assertEqual(len(date_col_normal[1]), 1000)

    # Check if the segments correspond to the expected ranges
    np.testing.assert_array_equal(normal_signal[0], signal_col[1000:2000])
    np.testing.assert_array_equal(normal_signal[1], signal_col[3000:4000])
    np.testing.assert_array_equal(date_col_normal[0], date_col[1000:2000])
    np.testing.assert_array_equal(date_col_normal[1], date_col[3000:4000])
def test_get_normal_segment_saves_csv_files(self):
    # Mock input data
    signal_col = np.random.rand(10000)
    date_col = pd.date_range(start='2023-01-01', periods=10000, freq='10ms')
    segment_folder = '/tmp/test_segment'
    rr_folder = '/tmp/test_rr'
    feats_folder = '/tmp/test_feats'
    file_path = '/tmp/test_file.csv'

    # Mock SignalQualityIndex
    with patch('src.analysis.quality_assurance_and_segmentation_nonin.SignalQualityIndex') as mock_sqi:
        mock_sqi_instance = MagicMock()
        mock_sqi_instance.signal_entropy_sqi.return_value = (
            [1, -3, 2, -4],  # SQI values
            [(1000, 2000), (3000, 4000)],  # Normal segments
            [(0, 1000), (2000, 3000)]  # Abnormal segments
        )
        mock_sqi.return_value = mock_sqi_instance

        # Mock other dependencies
        with patch('src.analysis.quality_assurance_and_segmentation_nonin.RRTransformation'):
            with patch('src.analysis.quality_assurance_and_segmentation_nonin.HRVFeatures'):
                with patch('src.analysis.quality_assurance_and_segmentation_nonin.PhysiologicalFeatureExtractor'):
                    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
                        with patch('numpy.savetxt') as mock_savetxt:
                            # Call the function
                            get_normal_segment(signal_col, date_col, segment_folder, rr_folder, feats_folder, file_path)

    # Assert that CSV files were saved
    mock_to_csv.assert_called()
    self.assertEqual(mock_to_csv.call_count, 4)  # 2 segment files + 2 feature files

    # Assert that RR interval files were saved
    mock_savetxt.assert_called()
    self.assertEqual(mock_savetxt.call_count, 2)  # 2 RR interval files

    # Check if the correct file names were used
    expected_csv_calls = [
        call(os.path.join(segment_folder, 'test_file_1000_2000.csv'), index=False),
        call(os.path.join(segment_folder, 'test_file_3000_4000.csv'), index=False),
        call(os.path.join(feats_folder, 'test_file_1000_2000_features.csv'), index=False),
        call(os.path.join(feats_folder, 'test_file_3000_4000_features.csv'), index=False)
    ]
    mock_to_csv.assert_has_calls(expected_csv_calls, any_order=True)

    expected_savetxt_calls = [
        call(os.path.join(rr_folder, 'test_file_1000_2000_rr.txt'), ANY),
        call(os.path.join(rr_folder, 'test_file_3000_4000_rr.txt'), ANY)
    ]
    mock_savetxt.assert_has_calls(expected_savetxt_calls, any_order=True)
    


if __name__ == '__main__':
    unittest.main()
