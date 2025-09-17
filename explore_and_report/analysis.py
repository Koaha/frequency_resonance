import pandas as pd
import numpy as np
from tableone import TableOne
import pingouin as pg
import seaborn as sns
import colorlog
import logging
import statsmodels.formula.api as smf
from pathlib import Path
from typing import List, Dict
import matplotlib.pyplot as plt
import os
from scipy.stats import ttest_rel, binom_test, mannwhitneyu
from sklearn.cluster import KMeans

# Constants
# RAW_MERGE_FILE = "24EI+03TS-raw-merge.xlsx"
RAW_MERGE_FILE = "24EI+03TS-raw-merge(in).csv"
FEATURES_FILE = "features_24EI_compiled.csv"
PATIENT_ID_PREFIX = "24EI-"
PLOTS_DIR = Path("plots")
CLINICAL_COLUMNS = [
    'USUBJID', 'AGE', 'SEX', 'OUTCOME',
    'Adrenaline/Urine (µg/24h)', 'Noradrenaline/Urine (µg/24h)', 'Dopamine/Urine (µg/24h)',
    'ANSD d1', 'ANSD d5', 'ANSD'
]
HRV_COLUMNS = [
    'patient_id', 'date', 'sdnn', 'rmssd', 'nn50', 'pnn50',
    'hrv_triangular_index', 'lf_power', 'hf_power', 'poincare_sd1', 'poincare_sd2',
    'systolic_duration', 'diastolic_duration', 'systolic_area', 'diastolic_area',
    'systolic_slope', 'diastolic_slope', 'signal_skewness', 'peak_trend_slope',
    'systolic_amplitude_variability', 'diastolic_amplitude_variability', 'dfa'
]
CATECHOLAMINE_RENAME = {
    'Adrenaline/Urine (µg/24h)': 'Adrenalin',
    'Noradrenaline/Urine (µg/24h)': 'Noradrenalin',
    'Dopamine/Urine (µg/24h)': 'Dopamin'
}
PPG_FEATURES = [
    'sdnn', 'rmssd', 'poincare_sd1', 'poincare_sd2',
    'systolic_duration', 'diastolic_duration', 'systolic_slope', 'diastolic_slope',
    'heart_rate', 'sample_entropy', 'nn50', 'pnn50',
    'hrv_triangular_index', 'lf_power', 'hf_power',
    'signal_skewness', 'peak_trend_slope', 'systolic_area', 'diastolic_area',
    'systolic_amplitude_variability', 'diastolic_amplitude_variability'
]

# Setup colored logging
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
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logging()

# Load and validate data
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
    logger.debug("Patient_id renamed and prefixed.")
    
    return clinical

def generate_summary_table(df: pd.DataFrame, columns: List[str], groupby: str, output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Generate a summary table using TableOne, enhanced with Day 1, Day 5, change, and overall stats.
    
    Args:
        df: DataFrame to summarize (merged data with DayLabel).
        columns: Columns to include in the summary (e.g., ['Adrenalin', 'Noradrenalin', 'Dopamin']).
        groupby: Column to group by (e.g., 'ANSD').
        output_dir: Directory to save results.
    
    Returns:
        DataFrame with detailed summary statistics.
    """
    logger.info(f"Generating summary table for {columns} by {groupby} with Day 1, Day 5, and overall stats...")
    
    # Split data into Day 1 and Day 5
    day1_data = df[df['DayLabel'] == 'Day1'].copy()
    day5_data = df[df['DayLabel'] == 'Day5'].copy()
    
    # Generate TableOne summaries for Day 1 and Day 5
    table_day1 = TableOne(
        day1_data,
        columns=columns,
        groupby=groupby,
        pval=True,
        missing=True,
        decimals=2,
        htest_name=True
    )
    table_day5 = TableOne(
        day5_data,
        columns=columns,
        groupby=groupby,
        pval=True,
        missing=True,
        decimals=2,
        htest_name=True
    )
    
    # Overall summary
    table_overall = TableOne(
        df,
        columns=columns,
        groupby=groupby,
        pval=True,
        missing=True,
        decimals=2,
        htest_name=True
    )
    
    # Convert to DataFrames
    df_day1 = table_day1.tableone.reset_index().rename(columns={'level_0': 'Feature', 'level_1': 'Statistic'})
    df_day5 = table_day5.tableone.reset_index().rename(columns={'level_0': 'Feature', 'level_1': 'Statistic'})
    df_overall = table_overall.tableone.reset_index().rename(columns={'level_0': 'Feature', 'level_1': 'Statistic'})
    
    # Add Day identifier
    df_day1['Day'] = 'Day1'
    df_day5['Day'] = 'Day5'
    df_overall['Day'] = 'Overall'
    
    # Calculate change (Day 5 - Day 1) for mean and median where applicable
    change_data = []
    for feature in columns:
        for group in df[groupby].unique():
            day1_mean = day1_data[day1_data[groupby] == group][feature].mean()
            day5_mean = day5_data[day5_data[groupby] == group][feature].mean()
            day1_median = day1_data[day1_data[groupby] == group][feature].median()
            day5_median = day5_data[day5_data[groupby] == group][feature].median()
            change_data.append({
                'Feature': feature,
                'Statistic': 'Mean Change (Day5 - Day1)',
                group: f"{(day5_mean - day1_mean):.2f}" if not np.isnan(day5_mean - day1_mean) else 'NA',
                'Day': 'Change'
            })
            change_data.append({
                'Feature': feature,
                'Statistic': 'Median Change (Day5 - Day1)',
                group: f"{(day5_median - day1_median):.2f}" if not np.isnan(day5_median - day1_median) else 'NA',
                'Day': 'Change'
            })
    
    df_change = pd.DataFrame(change_data)
    
    # Combine all summaries
    summary_df = pd.concat([df_day1, df_day5, df_change, df_overall], ignore_index=True)
    
    # Reorder columns to have 'Day' first
    cols = ['Day', 'Feature', 'Statistic'] + [col for col in summary_df.columns if col not in ['Day', 'Feature', 'Statistic']]
    summary_df = summary_df[cols]
    
    # Save to CSV
    summary_path = output_dir / "catecholamine_summary.csv"
    summary_df.to_csv(summary_path, index=False)
    logger.info(f"Saved detailed catecholamine summary to {summary_path}")
    
    return summary_df

def merge_with_features(clinical: pd.DataFrame, features_file: str) -> pd.DataFrame:
    """
    Merge clinical data with features data on patient_id, ensuring patients have exactly two rows in features data.
    
    Args:
        clinical: Preprocessed clinical DataFrame.
        features_file: Path to features CSV file.
    
    Returns:
        Merged DataFrame with only patients having exactly two rows in features data.
    
    Raises:
        ValueError: If merge results in an empty DataFrame.
    """
    # Load features data
    features = load_data(features_file, file_type='csv')
    
    # Filter patients with exactly 2 rows in features data
    logger.info("Filtering patients with exactly 2 rows in features data...")
    patient_counts = features.groupby('patient_id').size()
    valid_patients = patient_counts[patient_counts == 2].index
    features_filtered = features[features['patient_id'].isin(valid_patients)]
    
    logger.debug(f"Total patients in features data: {len(patient_counts)}")
    logger.debug(f"Patients with exactly 2 rows: {len(valid_patients)}")
    logger.debug(f"Features data shape after filtering: {features_filtered.shape}")
    
    if features_filtered.empty:
        logger.error("No patients with exactly 2 rows found in features data.")
        raise ValueError("No patients with exactly 2 rows found in features data.")
    
    # Merge with clinical data
    logger.info("Merging clinical and filtered features data...")
    merged = pd.merge(
        clinical,
        features_filtered,
        left_on='patient_id',
        right_on='patient_id',
        how='inner'
    )
    logger.debug(f"After merging, shape: {merged.shape}")
    logger.info(f"Unique patients after merge: {merged['patient_id'].nunique()}")
    
    if merged.empty:
        logger.error("Merge resulted in an empty DataFrame. Check patient_id values.")
        raise ValueError("Merge resulted in an empty DataFrame.")
    
    return merged

def process_hrv_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process HRV data: filter, select columns, assign Day1/Day5 labels, and pivot.
    
    Args:
        df: Merged DataFrame.
    
    Returns:
        Pivoted DataFrame with Day1 and Day5 columns.
    """
    logger.info("Processing HRV data...")
    
    # Filter patients with exactly 2 records
    hrv = df.groupby('patient_id').filter(lambda x: len(x) == 2)
    logger.debug(f"After filtering 2 records, shape: {hrv.shape}")
    
    # Select HRV columns
    available_hrv_columns = [col for col in HRV_COLUMNS if col in hrv.columns]
    if len(available_hrv_columns) < len(HRV_COLUMNS):
        logger.warning(f"Missing HRV columns: {[col for col in HRV_COLUMNS if col not in hrv.columns]}")
    hrv = hrv[available_hrv_columns].copy()
    logger.debug(f"HRV columns selected, shape: {hrv.shape}")
    
    # Convert date to datetime
    if 'date' not in hrv.columns:
        logger.error("Column 'date' not found.")
        raise ValueError("Column 'date' not found.")
    hrv['Date'] = pd.to_datetime(hrv['date'], errors='coerce')
    if hrv['Date'].isna().all():
        logger.error("All Date values are invalid or missing.")
        raise ValueError("All Date values are invalid or missing.")
    logger.debug(f"Date NAs: {hrv['Date'].isna().sum()}")
    
    # Assign Day1 and Day5 labels
    hrv = hrv.sort_values(['patient_id', 'Date'])
    hrv['DayLabel'] = hrv.groupby('patient_id')['Date'].transform(
        lambda x: np.where(x == x.min(), 'Day1', np.where(x == x.max(), 'Day5', np.nan))
    )
    hrv = hrv.dropna(subset=['DayLabel']).reset_index(drop=True)
    logger.debug(f"After labeling, shape: {hrv.shape}")
    
    # Pivot to wide format
    pivot_columns = [col for col in hrv.columns if col not in ['patient_id', 'Date', 'DayLabel', 'date']]
    hrv_wide = hrv.pivot(
        index='patient_id',
        columns='DayLabel',
        values=pivot_columns
    )
    hrv_wide.columns = [f"{col[0]}_{col[1]}" for col in hrv_wide.columns]
    hrv_wide = hrv_wide.reset_index()
    logger.debug(f"Pivoted shape: {hrv_wide.shape}")
    
    return hrv_wide

def aggregate_medians(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate medians for Day1 and Day5 columns.
    
    Args:
        df: Pivoted HRV DataFrame.
    
    Returns:
        Aggregated DataFrame with median columns.
    """
    logger.info("Aggregating medians for Day1 and Day5...")
    aggregated = df.copy()
    
    # Calculate medians only for numeric Day1 and Day5 columns
    for col in df.columns:
        if col.endswith('_Day1') or col.endswith('_Day5'):
            if pd.api.types.is_numeric_dtype(df[col]):
                aggregated[f"{col}_median"] = df[col].median()
            else:
                logger.warning(f"Skipping median for non-numeric column: {col}")
    
    # Clean column names, avoiding duplicates
    new_columns = []
    for col in aggregated.columns:
        if '_median' in col:
            new_columns.append(col.replace('_median', ''))
        else:
            new_columns.append(col)
    aggregated.columns = new_columns
    
    # Ensure no duplicate columns
    if aggregated.columns.duplicated().any():
        logger.warning(f"Duplicate columns detected: {aggregated.columns[aggregated.columns.duplicated()].tolist()}")
        aggregated = aggregated.loc[:, ~aggregated.columns.duplicated()]
    
    logger.debug(f"Cleaned columns: {aggregated.columns.tolist()}")
    return aggregated

def summarize_features(df: pd.DataFrame, merged_df: pd.DataFrame, output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Summarize features with medians, IQRs, and multiple statistical tests for Day1 vs Day5, including overall stats.
    
    Args:
        df: Aggregated DataFrame (pivoted with Day1 and Day5 columns).
        merged_df: Merged DataFrame with DayLabel for overall stats.
        output_dir: Directory to save results.
    
    Returns:
        Summary DataFrame with detailed statistics.
    """
    logger.info("Summarizing features with Day 1, Day 5, change, and overall stats...")
    output_dir.mkdir(parents=True, exist_ok=True)
    features = [col for col in df.columns if col != 'patient_id' and not col.lower().startswith('date')]
    base_features = list(set([col.replace('_Day1', '').replace('_Day5', '') for col in features]))
    
    def summarize_single_feature(feature: str) -> pd.Series:
        logger.info(f"Summarizing feature: {feature}")
        day1_col = f"{feature}_Day1"
        day5_col = f"{feature}_Day5"
        
        # Ensure paired data
        paired = df[['patient_id', day1_col, day5_col]].dropna()
        logger.debug(f"Paired DataFrame shape for {feature}: {paired.shape}")
        
        # Extract as Series
        day1 = paired[day1_col]
        day5 = paired[day5_col]
        
        # Overall data from merged_df
        overall_data = merged_df[feature].dropna()
        
        # Validate sample size and data
        n_samples = len(paired)
        logger.debug(f"Paired samples for {feature}: {n_samples}")
        if n_samples < 2 or not (pd.api.types.is_numeric_dtype(day1) and pd.api.types.is_numeric_dtype(day5)):
            logger.warning(f"Insufficient or non-numeric data ({n_samples} samples) for {feature}. Skipping tests.")
            return pd.Series({
                'Feature': feature,
                'Day1_Median_IQR': 'NA',
                'Day1_Mean_SD': 'NA',
                'Day5_Median_IQR': 'NA',
                'Day5_Mean_SD': 'NA',
                'Median_Change_Pct': 'NA',
                'Mean_Change_Pct': 'NA',
                'Overall_Median_IQR': 'NA',
                'Overall_Mean_SD': 'NA',
                'Wilcoxon_P': 'NA',
                'TTest_P': 'NA',
                'SignTest_P': 'NA',
                'Cohens_d': 'NA'
            })
        
        # Calculate medians, IQRs, means, and SDs
        med1 = np.median(day1)
        q1_1, q3_1 = np.percentile(day1, [25, 75])
        mean1 = np.mean(day1)
        sd1 = np.std(day1)
        
        med5 = np.median(day5)
        q1_5, q3_5 = np.percentile(day5, [25, 75])
        mean5 = np.mean(day5)
        sd5 = np.std(day5)
        
        # Overall stats
        med_overall = np.median(overall_data)
        q1_overall, q3_overall = np.percentile(overall_data, [25, 75])
        mean_overall = np.mean(overall_data)
        sd_overall = np.std(overall_data)
        
        # Calculate changes
        median_change_pct = ((med5 - med1) / med1 * 100) if med1 != 0 else np.nan
        mean_change_pct = ((mean5 - mean1) / mean1 * 100) if mean1 != 0 else np.nan
        
        # Statistical tests
        wilcoxon_p = np.nan
        ttest_p = np.nan
        sign_p = np.nan
        cohens_d = np.nan
        
        # Wilcoxon test
        try:
            wilcoxon_result = pg.wilcoxon(day1, day5)
            wilcoxon_p = wilcoxon_result['p-val'].iloc[0]
        except Exception as e:
            logger.warning(f"Wilcoxon test failed for {feature}: {str(e)}")
        
        # Paired t-test
        try:
            ttest_result = ttest_rel(day1, day5)
            ttest_p = ttest_result.pvalue
            if not np.isscalar(ttest_p):
                logger.warning(f"Paired t-test returned multiple p-values for {feature}. Skipping.")
                ttest_p = np.nan
        except Exception as e:
            logger.warning(f"Paired t-test failed for {feature}: {str(e)}")
        
        # Sign test
        try:
            differences = day1 - day5
            positive = np.sum(differences > 0)
            n = np.sum(differences != 0)
            if n > 0:
                sign_p = binomtest(positive, n, p=0.5).pvalue
            else:
                logger.warning(f"No non-zero differences for {feature} in sign test.")
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

#--------------------------------------
def detect_outliers(df: pd.DataFrame, y_col: str, day: str, x_col: str = 'Adrenalin', clinical_cols: List[str] = ['ANSD', 'OUTCOME']) -> pd.DataFrame:
    """
    Detect outliers using IQR method for a PPG feature on a specific day with detailed explanation.
    
    Args:
        df: DataFrame with data for a specific day.
        y_col: PPG feature column name.
        day: 'Day1' or 'Day5'.
        clinical_cols: Clinical columns to include for context.
    
    Returns:
        DataFrame of outliers with explanations.
    """
    clinical_cols = [x_col] + clinical_cols
    logger.info(f"Detecting outliers for {y_col} on {day}...")
    cols = [y_col, 'patient_id'] + [col for col in clinical_cols if col in df.columns]
    if 'Adrenalin' not in cols:
        logger.warning(f"'Adrenalin' not in columns for {y_col}. Available columns: {df.columns.tolist()}")
        cols.append('Adrenalin') if 'Adrenalin' in df.columns else logger.error("'Adrenalin' missing from DataFrame.")
    
    df_clean = df[cols].dropna(subset=[y_col])
    
    # Validate data size
    if len(df_clean) < 4:
        logger.warning(f"Too few data points ({len(df_clean)}) for {y_col} on {day}. Skipping outlier detection.")
        return pd.DataFrame(columns=cols + ['Day', 'Plot', 'Deviation', 'Explanation'])
    
    logger.debug(f"Valid data points for {y_col} on {day}: {len(df_clean)}, values: {df_clean[y_col].tolist()}")
    
    def get_outlier_indices(series):
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return (series < lower) | (series > upper)
    
    # Apply IQR to the entire Series
    outlier_mask = get_outlier_indices(df_clean[y_col])
    outliers = df_clean[outlier_mask].copy()
    
    if not outliers.empty:
        outliers['Day'] = day
        outliers['Plot'] = y_col
        median = df_clean[y_col].median()
        std = df_clean[y_col].std()
        outliers['Deviation'] = outliers[y_col].apply(
            lambda x: (x - median) / std if std != 0 else np.nan
        )
        outliers['Explanation'] = outliers.apply(
            lambda row: (
                f"Value {row[y_col]:.2f} on {day} is {row['Deviation']:.2f} SD from median "
                f"(median={median:.2f}, IQR=[{df_clean[y_col].quantile(0.25):.2f}, "
                f"{df_clean[y_col].quantile(0.75):.2f}]). "
                f"Adrenalin={row.get('Adrenalin', 'NA'):.2f}, "
                f"Patient ANSD={row.get('ANSD', 'NA')}, OUTCOME={row.get('OUTCOME', 'NA')}."
            ),
            axis=1
        )
    
    logger.debug(f"Found {len(outliers)} outliers for {y_col} on {day}.")
    return outliers

def analyze_noradrenalin_with_features(df: pd.DataFrame, features: List[str], output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Analyze the relationship between Noradrenalin and PPG features through correlations, statistical tests, and visualizations.
    Include Day 1, Day 5, change, and overall stats.
    
    Args:
        df: Merged DataFrame with Noradrenalin and PPG features.
        features: List of PPG feature names.
        output_dir: Directory to save results and plots.
    
    Returns:
        DataFrame with detailed correlation and statistical test results.
    """
    logger.info("Analyzing Noradrenalin with PPG features, including Day 1, Day 5, and overall stats...")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if 'Noradrenalin' not in df.columns:
        logger.error(f"'Noradrenalin' column missing from DataFrame. Available columns: {df.columns.tolist()}")
        raise KeyError("'Noradrenalin' column missing from DataFrame.")
    
    day1_data = df[df['DayLabel'] == 'Day1'].copy()
    day5_data = df[df['DayLabel'] == 'Day5'].copy()
    
    results = []
    
    for feature in features:
        if feature not in df.columns:
            logger.warning(f"Skipping {feature}: column missing from DataFrame.")
            continue
        
        logger.debug(f"Analyzing {feature} vs Noradrenalin...")
        
        # Day 1 correlation
        valid_day1 = day1_data[['Noradrenalin', feature]].dropna()
        corr_day1_r = corr_day1_p = n_day1 = np.nan
        if len(valid_day1) >= 2:
            corr_day1 = pg.corr(valid_day1['Noradrenalin'], valid_day1[feature], method='spearman')
            corr_day1_r = corr_day1['r'].iloc[0]
            corr_day1_p = corr_day1['p-val'].iloc[0]
            n_day1 = len(valid_day1)
        
        # Day 5 correlation
        valid_day5 = day5_data[['Noradrenalin', feature]].dropna()
        corr_day5_r = corr_day5_p = n_day5 = np.nan
        if len(valid_day5) >= 2:
            corr_day5 = pg.corr(valid_day5['Noradrenalin'], valid_day5[feature], method='spearman')
            corr_day5_r = corr_day5['r'].iloc[0]
            corr_day5_p = corr_day5['p-val'].iloc[0]
            n_day5 = len(valid_day5)
        
        # Overall correlation
        valid_data = df[['Noradrenalin', feature]].dropna()
        corr_overall_r = corr_overall_p = n_samples = np.nan
        if len(valid_data) >= 2:
            corr_overall = pg.corr(valid_data['Noradrenalin'], valid_data[feature], method='spearman')
            corr_overall_r = corr_overall['r'].iloc[0]
            corr_overall_p = corr_overall['p-val'].iloc[0]
            n_samples = len(valid_data)
        
        # Statistical comparison: Mann-Whitney U test for overall data
        mw_p = effect_size = high_n = low_n = np.nan
        if feature in valid_data.columns:
            median_feature = valid_data[feature].median()
            high_group = valid_data[valid_data[feature] > median_feature]['Noradrenalin'].dropna()
            low_group = valid_data[valid_data[feature] <= median_feature]['Noradrenalin'].dropna()
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
            x='Noradrenalin',
            y=feature,
            scatter_kws={'color': 'blue', 's': 50},
            line_kws={'color': 'red'}
        )
        plt.title(f"Noradrenalin vs {feature.upper()}")
        plt.xlabel("Noradrenaline/Urine (µg/24h)")
        plt.ylabel(feature.upper())
        scatter_path = output_dir / f"noradrenalin_vs_{feature}.png"
        plt.savefig(scatter_path, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved scatter plot to {scatter_path}")
        
        # Boxplot
        try:
            df[f"{feature}_quartile"] = pd.qcut(df[feature], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=f"{feature}_quartile", y='Noradrenalin', data=df)
            plt.title(f"Noradrenalin Distribution by {feature.upper()} Quartiles")
            plt.xlabel(f"{feature.upper()} Quartile")
            plt.ylabel("Noradrenaline/Urine (µg/24h)")
            boxplot_path = output_dir / f"noradrenalin_by_{feature}_quartile.png"
            plt.savefig(boxplot_path, dpi=300, bbox_inches='tight')
            plt.close()
            logger.debug(f"Saved boxplot to {boxplot_path}")
        except Exception as e:
            logger.warning(f"Boxplot failed for {feature}: {str(e)}")
    
    # Save results
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_path = output_dir / "noradrenalin_feature_analysis.csv"
        results_df.to_csv(results_path, index=False)
        logger.info(f"Saved detailed Noradrenalin analysis results to {results_path}")
        
        # Correlation heatmap
        corr_series = results_df.set_index('Feature')['Overall_Spearman_R']
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_series.to_frame(), annot=True, cmap='coolwarm', center=0, cbar_kws={'label': 'Spearman R'})
        plt.title("Spearman Correlations: Noradrenalin vs PPG Features")
        heatmap_path = output_dir / "noradrenalin_feature_correlations.png"
        plt.savefig(heatmap_path, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved correlation heatmap to {heatmap_path}")
    
    return results_df

def plot_ppg_features(df: pd.DataFrame, features: List[str], x_col: str = 'Adrenalin', output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Plot PPG features vs Adrenalin for Day 1 and Day 5 separately, with dots colored by ANSD status.
    Detect outliers, annotate them with patient_id, and save plots. Enhance outliers_summary.csv.
    
    Args:
        df: DataFrame with data (must include 'DayLabel', 'ANSD d1', 'ANSD d5').
        features: List of PPG feature column names.
        x_col: X-axis column name (default: 'Adrenalin').
        output_dir: Directory to save plots.
    
    Returns:
        DataFrame of all outliers across plots with enhanced details.
    """
    logger.info("Creating PPG feature plots and detecting outliers for Day 1 and Day 5...")
    output_dir.mkdir(parents=True, exist_ok=True)
    all_outliers = []
    
    # Validate required columns
    required_cols = [x_col, 'DayLabel', 'ANSD d1', 'ANSD d5', 'patient_id']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        logger.error(f"Missing required columns in df: {missing_cols}. Available columns: {df.columns.tolist()}")
        raise KeyError(f"Missing required columns in df: {missing_cols}")
    
    # Split data into Day 1 and Day 5
    day1_data = df[df['DayLabel'] == 'Day1'].copy()
    day5_data = df[df['DayLabel'] == 'Day5'].copy()
    
    logger.debug(f"Day 1 data shape: {day1_data.shape}, columns: {day1_data.columns.tolist()}")
    logger.debug(f"Day 5 data shape: {day5_data.shape}, columns: {day5_data.columns.tolist()}")
    
    if day1_data.empty or day5_data.empty:
        logger.error("No data available for Day 1 or Day 5 after splitting.")
        raise ValueError("No data available for Day 1 or Day 5 after splitting.")
    
    # Map ANSD status to the respective day
    day1_data['ANSD_status'] = day1_data['ANSD d1']
    day5_data['ANSD_status'] = day5_data['ANSD d5']
    
    # For outlier enhancement: create feature_changes with explicit patient_id column
    logger.info("Creating feature_changes DataFrame...")
    feature_changes = df.pivot(index='patient_id', columns='DayLabel', values=features)
    feature_changes.columns = [f"{col[0]}_{col[1]}" for col in feature_changes.columns]
    # Reset index and ensure patient_id is a column
    feature_changes = feature_changes.reset_index()
    logger.debug(f"feature_changes columns after pivot and reset: {feature_changes.columns.tolist()}")
    if 'patient_id' not in feature_changes.columns:
        logger.error("patient_id column missing in feature_changes after reset_index.")
        raise KeyError("patient_id column missing in feature_changes after reset_index.")
    
    # Ensure patient_id is a string and check for invalid values
    feature_changes['patient_id'] = feature_changes['patient_id'].astype(str)
    if feature_changes['patient_id'].isna().any() or (feature_changes['patient_id'] == '').any():
        logger.error("Invalid values (NaN or empty) found in feature_changes['patient_id'].")
        raise ValueError("Invalid values (NaN or empty) found in feature_changes['patient_id'].")
    logger.debug(f"feature_changes patient_id dtype: {feature_changes['patient_id'].dtype}")
    logger.debug(f"feature_changes patient_id sample: {feature_changes['patient_id'].head().tolist()}")
    
    sns.set_style("whitegrid")
    
    for feature in features:
        if feature not in df.columns:
            logger.warning(f"Skipping plot for {feature} vs {x_col}: {feature} column missing.")
            continue
        
        # Detect outliers for each day
        outliers_day1 = detect_outliers(day1_data, feature, 'Day1', x_col=x_col)
        outliers_day5 = detect_outliers(day5_data, feature, 'Day5', x_col=x_col)
        
        # Enhance outliers with Day 1, Day 5 values, and change
        if not outliers_day1.empty:
            logger.debug(f"Before merge for {feature} Day 1 - outliers_day1 columns: {outliers_day1.columns.tolist()}")
            logger.debug(f"Before merge for {feature} Day 1 - feature_changes columns: {feature_changes.columns.tolist()}")
            logger.debug(f"Before merge for {feature} Day 1 - outliers_day1 patient_id dtype: {outliers_day1['patient_id'].dtype}")
            logger.debug(f"Before merge for {feature} Day 1 - feature_changes patient_id dtype: {feature_changes['patient_id'].dtype}")
            logger.debug(f"Before merge for {feature} Day 1 - outliers_day1 patient_id sample: {outliers_day1['patient_id'].head().tolist()}")
            logger.debug(f"Before merge for {feature} Day 1 - feature_changes patient_id sample: {feature_changes['patient_id'].head().tolist()}")
            logger.debug(f"Merging columns: {f'{feature}_Day1'}, {f'{feature}_Day5'}")
            
            if 'patient_id' not in outliers_day1.columns:
                logger.error(f"patient_id column missing in outliers_day1 for feature {feature}.")
                raise KeyError(f"patient_id column missing in outliers_day1 for feature {feature}.")
            if 'patient_id' not in feature_changes.columns:
                logger.error(f"patient_id column missing in feature_changes for feature {feature}.")
                raise KeyError(f"patient_id column missing in feature_changes for feature {feature}.")
            
            # Ensure patient_id is a string in outliers_day1
            outliers_day1['patient_id'] = outliers_day1['patient_id'].astype(str)
            
            # Check for invalid patient_id values
            if outliers_day1['patient_id'].isna().any() or (outliers_day1['patient_id'] == '').any():
                logger.error(f"Invalid values (NaN or empty) found in outliers_day1['patient_id'] for feature {feature}.")
                raise ValueError(f"Invalid values (NaN or empty) found in outliers_day1['patient_id'] for feature {feature}.")
            
            # Ensure merge columns exist in feature_changes
            merge_cols = [f"{feature}_Day1", f"{feature}_Day5"]
            missing_merge_cols = [col for col in merge_cols if col not in feature_changes.columns]
            if missing_merge_cols:
                logger.error(f"Missing merge columns in feature_changes: {missing_merge_cols}")
                raise KeyError(f"Missing merge columns in feature_changes: {missing_merge_cols}")
            
            # Attempt merge, with fallback if it fails
            try:
                outliers_day1 = outliers_day1.merge(
                    feature_changes[merge_cols],
                    on='patient_id',
                    how='left'
                )
            except KeyError as e:
                logger.error(f"Merge failed for {feature} Day 1: {str(e)}. Attempting fallback merge strategy...")
                # Fallback: Set patient_id as index and join
                try:
                    outliers_day1 = outliers_day1.set_index('patient_id')
                    feature_subset = feature_changes.set_index('patient_id')[merge_cols]
                    outliers_day1 = outliers_day1.join(feature_subset, how='left')
                    outliers_day1 = outliers_day1.reset_index()
                    logger.info(f"Fallback merge succeeded for {feature} Day 1.")
                except Exception as e2:
                    logger.error(f"Fallback merge also failed for {feature} Day 1: {str(e2)}")
                    # Save DataFrames for manual inspection
                    outliers_day1.to_csv(output_dir / f"outliers_{x_col}_day1_{feature}_failed.csv", index=True)
                    feature_changes.to_csv(output_dir / f"feature_changes_{feature}_failed.csv", index=False)
                    raise
            
            outliers_day1[f"{feature}_Change_Pct"] = (
                (outliers_day1[f"{feature}_Day5"] - outliers_day1[f"{feature}_Day1"]) / 
                outliers_day1[f"{feature}_Day1"].replace(0, np.nan) * 100
            )
            all_outliers.append(outliers_day1)
        
        if not outliers_day5.empty:
            logger.debug(f"Before merge for {feature} Day 5 - outliers_day5 columns: {outliers_day5.columns.tolist()}")
            logger.debug(f"Before merge for {feature} Day 5 - feature_changes columns: {feature_changes.columns.tolist()}")
            logger.debug(f"Before merge for {feature} Day 5 - outliers_day5 patient_id dtype: {outliers_day5['patient_id'].dtype}")
            logger.debug(f"Before merge for {feature} Day 5 - feature_changes patient_id dtype: {feature_changes['patient_id'].dtype}")
            logger.debug(f"Before merge for {feature} Day 5 - outliers_day5 patient_id sample: {outliers_day5['patient_id'].head().tolist()}")
            
            if 'patient_id' not in outliers_day5.columns:
                logger.error(f"patient_id column missing in outliers_day5 for feature {feature}.")
                raise KeyError(f"patient_id column missing in outliers_day5 for feature {feature}.")
            if 'patient_id' not in feature_changes.columns:
                logger.error(f"patient_id column missing in feature_changes for feature {feature}.")
                raise KeyError(f"patient_id column missing in feature_changes for feature {feature}.")
            
            outliers_day5['patient_id'] = outliers_day5['patient_id'].astype(str)
            
            try:
                outliers_day5 = outliers_day5.merge(
                    feature_changes[[f"{feature}_Day1", f"{feature}_Day5"]],
                    on='patient_id',
                    how='left'
                )
            except KeyError as e:
                logger.error(f"Merge failed for {feature} Day 5: {str(e)}. Attempting fallback merge strategy...")
                try:
                    outliers_day5 = outliers_day5.set_index('patient_id')
                    feature_subset = feature_changes.set_index('patient_id')[[f"{feature}_Day1", f"{feature}_Day5"]]
                    outliers_day5 = outliers_day5.join(feature_subset, how='left')
                    outliers_day5 = outliers_day5.reset_index()
                    logger.info(f"Fallback merge succeeded for {feature} Day 5.")
                except Exception as e2:
                    logger.error(f"Fallback merge also failed for {feature} Day 5: {str(e2)}")
                    raise
            
            outliers_day5[f"{feature}_Change_Pct"] = (
                (outliers_day5[f"{feature}_Day5"] - outliers_day5[f"{feature}_Day1"]) / 
                outliers_day5[f"{feature}_Day1"].replace(0, np.nan) * 100
            )
            all_outliers.append(outliers_day5)
        
        # Define color palette for ANSD status
        ansd_palette = {'Yes_ANSD': 'red', 'No_ANSD': 'blue'}
        
        # Plot for Day 1
        logger.info(f"Plotting {feature} vs {x_col} for Day 1...")
        plt.figure(figsize=(8, 6))
        ax = sns.scatterplot(
            data=day1_data,
            x=x_col,
            y=feature,
            hue='ANSD_status',
            palette=ansd_palette,
            s=50
        )
        sns.regplot(
            data=day1_data,
            x=x_col,
            y=feature,
            scatter=False,
            color='black',
            ax=ax
        )
        
        if not outliers_day1.empty:
            for _, row in outliers_day1.iterrows():
                if x_col in row:
                    ax.scatter(row[x_col], row[feature], color='orange', s=100, label='Outlier' if _ == 0 else None)
                    ax.text(
                        row[x_col] + 0.5, row[feature] + 0.5,
                        row['patient_id'],
                        fontsize=8, color='black', ha='left', va='bottom'
                    )
        
        plt.title(f"Day 1: {feature.upper()} vs {x_col}/Urine (µg/24h)")
        plt.xlabel(f"{x_col}/Urine (µg/24h)")
        plt.ylabel(feature.upper())
        plt.legend(title="ANSD Status")
        plot_path_day1 = output_dir / f"{feature}_vs_{x_col}_day1.png"
        plt.savefig(plot_path_day1, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved Day 1 scatter plot to {plot_path_day1}")
        
        # Plot for Day 5
        logger.info(f"Plotting {feature} vs {x_col} for Day 5...")
        plt.figure(figsize=(8, 6))
        ax = sns.scatterplot(
            data=day5_data,
            x=x_col,
            y=feature,
            hue='ANSD_status',
            palette=ansd_palette,
            s=50
        )
        sns.regplot(
            data=day5_data,
            x=x_col,
            y=feature,
            scatter=False,
            color='black',
            ax=ax
        )
        
        if not outliers_day5.empty:
            for _, row in outliers_day5.iterrows():
                if x_col in row:
                    ax.scatter(row[x_col], row[feature], color='orange', s=100, label='Outlier' if _ == 0 else None)
                    ax.text(
                        row[x_col] + 0.5, row[feature] + 0.5,
                        row['patient_id'],
                        fontsize=8, color='black', ha='left', va='bottom'
                    )
        
        plt.title(f"Day 5: {feature.upper()} vs {x_col}/Urine (µg/24h)")
        plt.xlabel(f"{x_col}/Urine (µg/24h)")
        plt.ylabel(feature.upper())
        plt.legend(title="ANSD Status")
        plot_path_day5 = output_dir / f"{feature}_vs_{x_col}_day5.png"
        plt.savefig(plot_path_day5, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved Day 5 scatter plot to {plot_path_day5}")
        
        # Boxplot for PPG feature
        plt.figure(figsize=(6, 4))
        sns.boxplot(x='DayLabel', y=feature, data=df)
        plt.title(f"Boxplot of {feature.upper()} (Day 1 vs Day 5)")
        plt.xlabel("Day")
        plt.ylabel(feature.upper())
        boxplot_path = output_dir / f"{feature}_{x_col}_boxplot.png"
        plt.savefig(boxplot_path, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved boxplot to {boxplot_path}")
    
    # Combine outliers and reorder columns
    outliers_df = pd.concat(all_outliers, ignore_index=True) if all_outliers else pd.DataFrame()
    if not outliers_df.empty:
        feature_cols = [f"{feature}_Day1" for feature in features] + [f"{feature}_Day5" for feature in features] + [f"{feature}_Change_Pct" for feature in features]
        cols = ['Day', 'patient_id'] + [col for col in df.columns if col in features] + feature_cols + [x_col] + ['ANSD', 'OUTCOME', 'Plot', 'Deviation', 'Explanation']
        cols = [col for col in cols if col in outliers_df.columns]
        outliers_df = outliers_df[cols]
        outliers_path = output_dir / "outliers_summary.csv"
        outliers_df.to_csv(outliers_path, index=False)
        logger.info(f"Saved detailed outliers summary to {outliers_path}")
    
    return outliers_df

def analyze_feature_changes(df: pd.DataFrame, merged_df: pd.DataFrame, features: List[str], output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Calculate and visualize percentage changes in PPG features from Day1 to Day5, including Day 1, Day 5, and overall stats.
    
    Args:
        df: Pivoted DataFrame with Day1 and Day5 columns.
        merged_df: Merged DataFrame for overall stats.
        features: List of PPG feature names.
        output_dir: Directory to save plots.
    
    Returns:
        DataFrame with detailed feature chapnges.
    """
    logger.info("Analyzing feature changes with Day 1, Day 5, and overall stats...")
    output_dir.mkdir(parents=True, exist_ok=True)
    changes = df[['patient_id']].copy()
    
    # Add Day 1 and Day 5 values
    for feature in features:
        day1_col = f"{feature}_Day1"
        day5_col = f"{feature}_Day5"
        if day1_col in df.columns and day5_col in df.columns:
            changes[day1_col] = df[day1_col]
            changes[day5_col] = df[day5_col]
    
    # Compute percentage changes
    for feature in features:
        day1_col = f"{feature}_Day1"
        day5_col = f"{feature}_Day5"
        if day1_col not in df.columns or day5_col not in df.columns:
            logger.warning(f"Skipping {feature}: {day1_col} or {day5_col} not in DataFrame.")
            continue
        
        try:
            pct_change = (
                (df[day5_col] - df[day1_col]) / df[day1_col].replace(0, np.nan) * 100
            )
            changes[f"{feature}_pct_change"] = pct_change
        except Exception as e:
            logger.warning(f"Failed to compute percentage change for {feature}: {str(e)}")
            continue
    
    # Add overall summary statistics as a new row
    summary_row = {'patient_id': 'Overall_Summary'}
    for feature in features:
        if feature in merged_df.columns:
            overall_data = merged_df[feature].dropna()
            if len(overall_data) == 0:
                logger.warning(f"Skipping overall stats for {feature}: No valid data after dropping NaN values.")
                summary_row[f"{feature}_Overall_Median_IQR"] = 'NA'
                summary_row[f"{feature}_Overall_Mean_SD"] = 'NA'
                continue
            try:
                med = np.median(overall_data)
                q1, q3 = np.percentile(overall_data, [25, 75])
                mean = np.mean(overall_data)
                sd = np.std(overall_data)
                summary_row[f"{feature}_Day1"] = np.nan
                summary_row[f"{feature}_Day5"] = np.nan
                summary_row[f"{feature}_pct_change"] = np.nan
                summary_row[f"{feature}_Overall_Median_IQR"] = f"{med:.1f} ({q1:.1f}–{q3:.1f})"
                summary_row[f"{feature}_Overall_Mean_SD"] = f"{mean:.1f} ± {sd:.1f}"
            except Exception as e:
                logger.warning(f"Failed to compute overall stats for {feature}: {str(e)}")
                summary_row[f"{feature}_Overall_Median_IQR"] = 'NA'
                summary_row[f"{feature}_Overall_Mean_SD"] = 'NA'
    
    # Append summary row
    summary_df = pd.DataFrame([summary_row])
    changes = pd.concat([changes, summary_df], ignore_index=True)
    
    # Plot histograms
    for feature in features:
        if f"{feature}_pct_change" in changes.columns:
            plt.figure(figsize=(6, 4))
            sns.histplot(changes[f"{feature}_pct_change"].dropna(), kde=True)
            plt.title(f"Percentage Change in {feature.upper()} (Day5 - Day1)")
            plt.xlabel("Percentage Change (%)")
            plt.ylabel("Count")
            hist_path = output_dir / f"{feature}_pct_change_hist.png"
            plt.savefig(hist_path, dpi=300, bbox_inches='tight')
            plt.close()
            logger.debug(f"Saved histogram to {hist_path}")
    
    changes_path = output_dir / "feature_changes.csv"
    changes.to_csv(changes_path, index=False)
    logger.info(f"Saved detailed feature changes to {changes_path}")
    return changes

def correlate_with_clinical(df: pd.DataFrame, feature_changes: pd.DataFrame, clinical_cols: List[str] = ['ANSD', 'OUTCOME', 'Adrenalin'], output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Correlate feature changes with clinical outcomes, including Day 1, Day 5, and overall correlations.
    
    Args:
        df: Merged DataFrame with clinical data.
        feature_changes: DataFrame with percentage changes.
        clinical_cols: Clinical columns to correlate with.
        output_dir: Directory to save plots.
    
    Returns:
        DataFrame with detailed correlation coefficients.
    """
    logger.info("Correlating feature changes with clinical outcomes, including Day 1 and Day 5...")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    merged = df.merge(feature_changes, on='patient_id')
    day1_data = merged[merged['DayLabel'] == 'Day1'].copy()
    day5_data = merged[merged['DayLabel'] == 'Day5'].copy()
    
    correlations = []
    
    for feature in feature_changes.columns:
        if feature.endswith('_pct_change'):
            base_feature = feature.replace('_pct_change', '')
            for col in clinical_cols:
                if col in merged.columns:
                    # Day 1 correlation
                    if base_feature in day1_data.columns:
                        corr_day1 = pg.corr(day1_data[base_feature], day1_data[col].rank(), method='spearman')
                        corr_day1_r = corr_day1['r'].iloc[0]
                        corr_day1_p = corr_day1['p-val'].iloc[0]
                    else:
                        corr_day1_r = corr_day1_p = np.nan
                    
                    # Day 5 correlation
                    if base_feature in day5_data.columns:
                        corr_day5 = pg.corr(day5_data[base_feature], day5_data[col].rank(), method='spearman')
                        corr_day5_r = corr_day5['r'].iloc[0]
                        corr_day5_p = corr_day5['p-val'].iloc[0]
                    else:
                        corr_day5_r = corr_day5_p = np.nan
                    
                    # Change correlation
                    corr_change = pg.corr(merged[feature], merged[col].rank(), method='spearman')
                    corr_change_r = corr_change['r'].iloc[0]
                    corr_change_p = corr_change['p-val'].iloc[0]
                    
                    # Overall correlation
                    if base_feature in merged.columns:
                        corr_overall = pg.corr(merged[base_feature], merged[col].rank(), method='spearman')
                        corr_overall_r = corr_overall['r'].iloc[0]
                        corr_overall_p = corr_overall['p-val'].iloc[0]
                    else:
                        corr_overall_r = corr_overall_p = np.nan
                    
                    correlations.append({
                        'Feature': base_feature,
                        'Clinical_Var': col,
                        'Day1_Spearman_R': corr_day1_r,
                        'Day1_P_value': corr_day1_p,
                        'Day5_Spearman_R': corr_day5_r,
                        'Day5_P_value': corr_day5_p,
                        'Change_Spearman_R': corr_change_r,
                        'Change_P_value': corr_change_p,
                        'Overall_Spearman_R': corr_overall_r,
                        'Overall_P_value': corr_overall_p
                    })
    
    corr_df = pd.DataFrame(correlations)
    if not corr_df.empty:
        corr_path = output_dir / "clinical_correlations.csv"
        corr_df.to_csv(corr_path, index=False)
        logger.info(f"Saved detailed correlations to {corr_path}")
        
        # Heatmap of change correlations
        pivot = corr_df.pivot(index='Feature', columns='Clinical_Var', values='Change_Spearman_R')
        plt.figure(figsize=(8, 6))
        sns.heatmap(pivot, annot=True, cmap='coolwarm', center=0)
        plt.title("Spearman Correlations: Feature Changes vs Clinical Outcomes")
        heatmap_path = output_dir / "clinical_correlations_heatmap.png"
        plt.savefig(heatmap_path, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved correlation heatmap to {heatmap_path}")
    
    return corr_df

def cluster_patients(df: pd.DataFrame, features: List[str], merged_df: pd.DataFrame, n_clusters: int = 3, output_dir: Path = PLOTS_DIR) -> pd.DataFrame:
    """
    Cluster patients based on PPG feature changes, including Day 1, Day 5, and overall stats.
    
    Args:
        df: DataFrame with feature changes.
        features: List of feature change columns.
        merged_df: Merged DataFrame for overall stats.
        n_clusters: Number of clusters.
        output_dir: Directory to save plots.
    
    Returns:
        DataFrame with detailed cluster assignments.
    """
    logger.info(f"Clustering patients into {n_clusters} clusters with detailed stats...")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    feature_cols = [f"{f}_pct_change" for f in features if f"{f}_pct_change" in df.columns]
    if len(feature_cols) < 2:
        logger.warning("Too few features for clustering.")
        return pd.DataFrame()
    
    X = df[feature_cols].dropna()
    if len(X) < n_clusters:
        logger.warning(f"Too few samples ({len(X)}) for {n_clusters} clusters.")
        return pd.DataFrame()
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df.loc[X.index, 'Cluster'] = kmeans.fit_predict(X)
    
    # Add Day 1 and Day 5 values
    for feature in features:
        day1_col = f"{feature}_Day1"
        day5_col = f"{feature}_Day5"
        if day1_col in df.columns and day5_col in df.columns:
            df[day1_col] = df[day1_col]
            df[day5_col] = df[day5_col]
    
    # Add overall summary statistics per cluster
    cluster_stats = []
    for cluster in df['Cluster'].dropna().unique():
        cluster_data = df[df['Cluster'] == cluster]
        stats = {'Cluster': cluster}
        for feature in features:
            if feature in merged_df.columns:
                cluster_feature_data = merged_df[merged_df['patient_id'].isin(cluster_data['patient_id'])][feature].dropna()
                med = np.median(cluster_feature_data)
                q1, q3 = np.percentile(cluster_feature_data, [25, 75])
                mean = np.mean(cluster_feature_data)
                sd = np.std(cluster_feature_data)
                stats[f"{feature}_Overall_Median_IQR"] = f"{med:.1f} ({q1:.1f}–{q3:.1f})"
                stats[f"{feature}_Overall_Mean_SD"] = f"{mean:.1f} ± {sd:.1f}"
        cluster_stats.append(stats)
    
    cluster_stats_df = pd.DataFrame(cluster_stats)
    cluster_stats_df['patient_id'] = 'Cluster_Summary'
    
    # Combine with original data
    cluster_summary = pd.concat([df, cluster_stats_df], ignore_index=True)
    
    # Scatter plot
    if len(feature_cols) >= 2:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            data=df,
            x=feature_cols[0],
            y=feature_cols[1],
            hue='Cluster',
            palette='deep'
        )
        plt.title(f"Patient Clusters: {feature_cols[0]} vs {feature_cols[1]}")
        plt.xlabel(feature_cols[0])
        plt.ylabel(feature_cols[1])
        cluster_path = output_dir / "patient_clusters.png"
        plt.savefig(cluster_path, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved cluster plot to {cluster_path}")
    
    cluster_path = output_dir / "cluster_assignments.csv"
    cluster_summary.to_csv(cluster_path, index=False)
    logger.info(f"Saved detailed cluster assignments to {cluster_path}")
    return cluster_summary

def plot_time_series_trends(df: pd.DataFrame, features: List[str], output_dir: Path = PLOTS_DIR) -> None:
    """
    Plot median and IQR trends for PPG features across Day1 and Day5.
    
    Args:
        df: Pivoted DataFrame with Day1 and Day5 columns.
        features: List of PPG feature names.
        output_dir: Directory to save plots.
    """
    logger.info("Plotting time-series trends...")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for feature in features:
        day1_col = f"{feature}_Day1"
        day5_col = f"{feature}_Day5"
        if day1_col in df.columns and day5_col in df.columns:
            data = {
                'Day1': df[day1_col].dropna(),
                'Day5': df[day5_col].dropna()
            }
            medians = [np.median(data['Day1']), np.median(data['Day5'])]
            q1 = [np.percentile(data['Day1'], 25), np.percentile(data['Day5'], 25)]
            q3 = [np.percentile(data['Day1'], 75), np.percentile(data['Day5'], 75)]
            
            plt.figure(figsize=(6, 4))
            plt.plot(['Day1', 'Day5'], medians, marker='o', label='Median')
            plt.fill_between(['Day1', 'Day5'], q1, q3, alpha=0.2, label='IQR')
            plt.title(f"Trend in {feature.upper()} (Day1 to Day5)")
            plt.ylabel(feature.upper())
            plt.legend()
            trend_path = output_dir / f"{feature}_trend.png"
            plt.savefig(trend_path, dpi=300, bbox_inches='tight')
            plt.close()
            logger.debug(f"Saved trend plot to {trend_path}")

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
        
        # Boxplot
        try:
            df[f"{feature}_quartile"] = pd.qcut(df[feature], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=f"{feature}_quartile", y='Adrenalin', data=df)
            plt.title(f"Adrenalin Distribution by {feature.upper()} Quartiles")
            plt.xlabel(f"{feature.upper()} Quartile")
            plt.ylabel("Adrenaline/Urine (µg/24h)")
            boxplot_path = output_dir / f"adrenalin_by_{feature}_quartile.png"
            plt.savefig(boxplot_path, dpi=300, bbox_inches='tight')
            plt.close()
            logger.debug(f"Saved boxplot to {boxplot_path}")
        except Exception as e:
            logger.warning(f"Boxplot failed for {feature}: {str(e)}")
    
    # Save results
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_path = output_dir / "adrenalin_feature_analysis.csv"
        results_df.to_csv(results_path, index=False)
        logger.info(f"Saved detailed Adrenalin analysis results to {results_path}")
        
        # Correlation heatmap
        corr_series = results_df.set_index('Feature')['Overall_Spearman_R']
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_series.to_frame(), annot=True, cmap='coolwarm', center=0, cbar_kws={'label': 'Spearman R'})
        plt.title("Spearman Correlations: Adrenalin vs PPG Features")
        heatmap_path = output_dir / "adrenalin_feature_correlations.png"
        plt.savefig(heatmap_path, dpi=300, bbox_inches='tight')
        plt.close()
        logger.debug(f"Saved correlation heatmap to {heatmap_path}")
    
    return results_df

# Modified main()
def main():
    """Main function to orchestrate the data processing pipeline."""
    logger = setup_logging()
    
    # Load and preprocess clinical data
    # clinical_raw = load_data(RAW_MERGE_FILE, file_type='excel')
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
    merged_2records['DayLabel'] = merged_2records.groupby('patient_id')['Date'].transform(
        lambda x: np.where(x == x.min(), 'Day1', np.where(x == x.max(), 'Day5', np.nan))
    )
    merged_2records = merged_2records.dropna(subset=['DayLabel']).reset_index(drop=True)
    logger.debug(f"merged_2records shape: {merged_2records.shape}, columns: {merged_2records.columns.tolist()}")
    
    # Plot PPG features and detect outliers
    outliers_adrenalin = plot_ppg_features(merged_2records, PPG_FEATURES, x_col='Adrenalin')
    if not outliers_adrenalin.empty:
        logger.info("Detailed outliers saved to plots/outliers_adrenalin_summary.csv")
    
    outliers_noradrenalin = plot_ppg_features(merged_2records, PPG_FEATURES, x_col='Noradrenalin')
    if not outliers_noradrenalin.empty:
        logger.info("Detailed outliers saved to plots/outliers_noradrenalin_summary.csv")
    
    # Analyze feature changes
    feature_changes = analyze_feature_changes(aggregated, merged, PPG_FEATURES)
    logger.info("Detailed feature changes saved to plots/feature_changes.csv")
    
    # Correlate with clinical outcomes
    corr_df = correlate_with_clinical(merged, feature_changes)
    logger.info("Detailed clinical correlations saved to plots/clinical_correlations.csv")
    
    # Analyze Adrenalin with features
    adrenalin_results = analyze_adrenalin_with_features(merged, PPG_FEATURES)
    logger.info("Detailed Adrenalin vs features analysis saved to plots/adrenalin_feature_analysis.csv")
    
    # Analyze Noradrenalin with features
    noradrenalin_results = analyze_noradrenalin_with_features(merged, PPG_FEATURES)
    logger.info("Detailed Noradrenalin vs features analysis saved to plots/noradrenalin_feature_analysis.csv")
    
    # Cluster patients
    cluster_summary = cluster_patients(feature_changes, PPG_FEATURES, merged)
    logger.info("Detailed cluster assignments saved to plots/cluster_assignments.csv")
    
    # Plot time-series trends
    plot_time_series_trends(aggregated, PPG_FEATURES)

if __name__ == "__main__":
    main()