import pandas as pd
import numpy as np
from tableone import TableOne
import pingouin as pg
import seaborn as sns
import colorlog
import logging
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot
from statsmodels.stats.api import het_breuschpagan
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.stats import binomtest, mannwhitneyu
from pathlib import Path
from typing import List
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from sklearn.cluster import KMeans

# Constants
RAW_MERGE_FILE = "24EI+03TS-raw-merge.xlsx"
FEATURES_FILE = "features_24EI_compiled.csv"
PATIENT_ID_PREFIX = "24EI-"
PLOTS_DIR = Path("plots")
SUMMARY_DIR = Path("summaries")
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

def generate_markdown_report():
    """Generate a comprehensive Markdown report combining all analysis outputs."""
    md_path = Path("analysis_report.md")
    with open(md_path, 'w') as md:
        md.write("# Analysis Summary\n\n")
        
        # Feature Summary Table
        feature_summary_path = SUMMARY_DIR / "feature_summary.csv"
        if feature_summary_path.exists():
            md.write("## Feature Summary Table\n\n")
            df = pd.read_csv(feature_summary_path)
            md.write(df.to_markdown(index=False))
            md.write("\n\n")
        
        # Catecholamine Summary
        catecholamine_summary_path = SUMMARY_DIR / "catecholamine_summary.csv"
        if catecholamine_summary_path.exists():
            md.write("## Catecholamine Summary\n\n")
            df = pd.read_csv(catecholamine_summary_path)
            md.write(df.to_markdown(index=False))
            md.write("\n\n")
        
        # General Sections (e.g., pair plots, heatmaps, PCA, etc. for Adrenalin and Noradrenalin)
        for x_col in ['Adrenalin', 'Noradrenalin']:
            general_dir = PLOTS_DIR / "general" / x_col.lower()
            md.write(f"## General Analysis for {x_col}\n\n")
            
            # Pair Plot
            pair_path = general_dir / "pair_plot.png"
            desc_path = general_dir / "pair_plot_desc.txt"
            if pair_path.exists():
                md.write(f"### Pair Plot\n\n![Pair Plot]({pair_path})\n\n")
                if desc_path.exists():
                    with open(desc_path, 'r') as f:
                        md.write(f.read() + "\n\n")
            
            # Correlation Heatmap
            heatmap_path = general_dir / "correlation_heatmap.png"
            desc_path = general_dir / "correlation_heatmap_desc.txt"
            if heatmap_path.exists():
                md.write(f"### Correlation Heatmap\n\n![Correlation Heatmap]({heatmap_path})\n\n")
                if desc_path.exists():
                    with open(desc_path, 'r') as f:
                        md.write(f.read() + "\n\n")
            
            # PCA Plot
            pca_path = general_dir / "pca_plot.png"
            desc_path = general_dir / "pca_plot_desc.txt"
            if pca_path.exists():
                md.write(f"### PCA Plot\n\n![PCA Plot]({pca_path})\n\n")
                if desc_path.exists():
                    with open(desc_path, 'r') as f:
                        md.write(f.read() + "\n\n")
            
            # Feature Analysis CSV
            analysis_path = general_dir / f"{x_col.lower()}_feature_analysis.csv"
            if analysis_path.exists():
                md.write(f"### Feature Analysis Table\n\n")
                df = pd.read_csv(analysis_path)
                md.write(df.to_markdown(index=False))
                md.write("\n\n")
            
            # Correlation Heatmap for Features
            corr_heatmap_path = general_dir / f"{x_col.lower()}_feature_correlations.png"
            if corr_heatmap_path.exists():
                md.write(f"### Feature Correlations Heatmap\n\n![Feature Correlations]({corr_heatmap_path})\n\n")
            
            # Boxplots by Quartiles
            for feature in PPG_FEATURES:
                box_path = general_dir / f"{feature}_{x_col.lower()}_quartiles.png"
                desc_path = general_dir / f"{feature}_{x_col.lower()}_quartiles_desc.txt"
                if box_path.exists():
                    md.write(f"#### {feature} by {x_col} Quartiles\n\n![Boxplot]({box_path})\n\n")
                    if desc_path.exists():
                        with open(desc_path, 'r') as f:
                            md.write(f.read() + "\n\n")
            
            # Scatter Plots
            for feature in PPG_FEATURES:
                scatter_path = general_dir / f"{x_col.lower()}_vs_{feature}.png"
                if scatter_path.exists():
                    md.write(f"#### Scatter Plot: {x_col} vs {feature}\n\n![Scatter]({scatter_path})\n\n")
        
        # Per-Feature Sections
        for feature in PPG_FEATURES:
            md.write(f"# Feature: {feature.upper()}\n\n")
            
            feature_dir = PLOTS_DIR / feature
            
            # Day Comparison
            comp_path = feature_dir / f"{feature}_day_comparison.png"
            comp_desc_path = feature_dir / f"{feature}_day_comparison_desc.txt"
            if comp_path.exists():
                md.write(f"## Day Comparison\n\n![Day Comparison]({comp_path})\n\n")
                if comp_desc_path.exists():
                    with open(comp_desc_path, 'r') as f:
                        md.write(f.read() + "\n\n")
            
            # Change Stats
            stats_path = feature_dir / "change_stats.txt"
            if stats_path.exists():
                md.write("### Change Statistics\n\n")
                with open(stats_path, 'r') as f:
                    md.write("```\n" + f.read() + "\n```\n\n")
            
            # Change Histogram
            hist_path = feature_dir / "change_histogram.png"
            hist_desc_path = feature_dir / "change_histogram_desc.txt"
            if hist_path.exists():
                md.write(f"### Change Histogram\n\n![Change Histogram]({hist_path})\n\n")
                if hist_desc_path.exists():
                    with open(hist_desc_path, 'r') as f:
                        md.write(f.read() + "\n\n")
            
            # Change QQ Plot
            qq_path = feature_dir / "change_qq.png"
            qq_desc_path = feature_dir / "change_qq_desc.txt"
            if qq_path.exists():
                md.write(f"### Change QQ Plot\n\n![Change QQ]({qq_path})\n\n")
                if qq_desc_path.exists():
                    with open(qq_desc_path, 'r') as f:
                        md.write(f.read() + "\n\n")
            
            # Day KDE Comparison
            kde_path = feature_dir / "day_kde_comparison.png"
            kde_desc_path = feature_dir / "day_kde_comparison_desc.txt"
            if kde_path.exists():
                md.write(f"### Day KDE Comparison\n\n![Day KDE]({kde_path})\n\n")
                if kde_desc_path.exists():
                    with open(kde_desc_path, 'r') as f:
                        md.write(f.read() + "\n\n")
            
            # Vs Adrenalin and Noradrenalin
            for x_col in ['adrenalin', 'noradrenalin']:
                sub_dir = feature_dir / x_col
                
                md.write(f"## Vs {x_col.capitalize()}\n\n")
                
                for day in ['day1', 'day5']:
                    md.write(f"### {day.capitalize()}\n\n")
                    
                    # Linear Regression Plot
                    lin_path = sub_dir / f"{feature}_vs_{x_col}_ {day}_linear.png"
                    lin_desc_path = sub_dir / f"{feature}_vs_{x_col}_ {day}_linear_desc.txt"
                    if lin_path.exists():
                        md.write(f"#### Linear Regression Plot\n\n![Linear Regression]({lin_path})\n\n")
                        if lin_desc_path.exists():
                            with open(lin_desc_path, 'r') as f:
                                md.write(f.read() + "\n\n")
                    
                    # Model Summary
                    model_path = sub_dir / f"model_summary_{day}.txt"
                    if model_path.exists():
                        md.write(f"#### Model Summary\n\n")
                        with open(model_path, 'r') as f:
                            md.write("```\n" + f.read() + "\n```\n\n")
                    
                    # Residuals Plot
                    res_path = sub_dir / f"residuals_{day}.png"
                    res_desc_path = sub_dir / f"residuals_{day}_desc.txt"
                    if res_path.exists():
                        md.write(f"#### Residuals Plot\n\n![Residuals]({res_path})\n\n")
                        if res_desc_path.exists():
                            with open(res_desc_path, 'r') as f:
                                md.write(f.read() + "\n\n")
                    
                    # QQ Plot
                    qq_path = sub_dir / f"qq_{day}.png"
                    qq_desc_path = sub_dir / f"qq_{day}_desc.txt"
                    if qq_path.exists():
                        md.write(f"#### QQ Plot\n\n![QQ Plot]({qq_path})\n\n")
                        if qq_desc_path.exists():
                            with open(qq_desc_path, 'r') as f:
                                md.write(f.read() + "\n\n")
                    
                    # Leverage Plot
                    lev_path = sub_dir / f"leverage_{day}.png"
                    lev_desc_path = sub_dir / f"leverage_{day}_desc.txt"
                    if lev_path.exists():
                        md.write(f"#### Leverage Plot\n\n![Leverage]({lev_path})\n\n")
                        if lev_desc_path.exists():
                            with open(lev_desc_path, 'r') as f:
                                md.write(f.read() + "\n\n")
                    
                    # Residual Histogram
                    res_hist_path = sub_dir / f"residual_histogram_{day}.png"
                    res_hist_desc_path = sub_dir / f"residual_histogram_{day}_desc.txt"
                    if res_hist_path.exists():
                        md.write(f"#### Residual Histogram\n\n![Residual Histogram]({res_hist_path})\n\n")
                        if res_hist_desc_path.exists():
                            with open(res_hist_desc_path, 'r') as f:
                                md.write(f.read() + "\n\n")
                    
                    # Joint Plot
                    joint_path = sub_dir / f"joint_plot_{day}.png"
                    joint_desc_path = sub_dir / f"joint_plot_{day}_desc.txt"
                    if joint_path.exists():
                        md.write(f"#### Joint Plot\n\n![Joint Plot]({joint_path})\n\n")
                        if joint_desc_path.exists():
                            with open(joint_desc_path, 'r') as f:
                                md.write(f.read() + "\n\n")
                    
                    # Hexbin Plot
                    hex_path = sub_dir / f"hexbin_plot_{day}.png"
                    hex_desc_path = sub_dir / f"hexbin_plot_{day}_desc.txt"
                    if hex_path.exists():
                        md.write(f"#### Hexbin Plot\n\n![Hexbin Plot]({hex_path})\n\n")
                        if hex_desc_path.exists():
                            with open(hex_desc_path, 'r') as f:
                                md.write(f.read() + "\n\n")
        
        # Outliers Summary
        for x_col in ['Adrenalin', 'Noradrenalin']:
            outliers_path = PLOTS_DIR / f"outliers_summary_{x_col.lower()}.csv"
            if outliers_path.exists():
                md.write(f"## Outliers Summary for {x_col}\n\n")
                df = pd.read_csv(outliers_path)
                md.write(df.to_markdown(index=False))
                md.write("\n\n")
        
        # Feature Changes
        changes_path = PLOTS_DIR / "general" / "feature_changes.csv"
        if changes_path.exists():
            md.write("## Feature Changes\n\n")
            df = pd.read_csv(changes_path)
            md.write(df.to_markdown(index=False))
            md.write("\n\n")
        
        # Clinical Correlations
        corr_path = PLOTS_DIR / "general" / "clinical_correlations.csv"
        if corr_path.exists():
            md.write("## Clinical Correlations\n\n")
            df = pd.read_csv(corr_path)
            md.write(df.to_markdown(index=False))
            md.write("\n\n")
        
        corr_heatmap_path = PLOTS_DIR / "general" / "clinical_correlations_heatmap.png"
        if corr_heatmap_path.exists():
            md.write(f"### Clinical Correlations Heatmap\n\n![Clinical Correlations Heatmap]({corr_heatmap_path})\n\n")
        
        # Cluster Assignments
        cluster_path = PLOTS_DIR / "general" / "cluster_assignments.csv"
        if cluster_path.exists():
            md.write("## Cluster Assignments\n\n")
            df = pd.read_csv(cluster_path)
            md.write(df.to_markdown(index=False))
            md.write("\n\n")
        
        cluster_plot_path = PLOTS_DIR / "general" / "patient_clusters.png"
        if cluster_plot_path.exists():
            md.write(f"### Patient Clusters Plot\n\n![Patient Clusters]({cluster_plot_path})\n\n")
        
        # Time Series Trends
        md.write("## Time Series Trends\n\n")
        for feature in PPG_FEATURES:
            trend_path = PLOTS_DIR / "general" / f"{feature}_trend.png"
            if trend_path.exists():
                md.write(f"### Trend for {feature.upper()}\n\n![Trend]({trend_path})\n\n")
    
    logger.info(f"Generated Markdown report at {md_path}")

def main():
    generate_markdown_report()
    
if __name__ == "__main__":
    main()