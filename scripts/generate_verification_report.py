#!/usr/bin/env python3
"""Generate a markdown data-verification report with Seaborn plots.

Usage:
    python scripts/generate_verification_report.py [--output-dir OUTPUT] [--config CONFIG]

Walks the output tree produced by the processing pipeline and produces a
comprehensive markdown report with embedded visualisations covering
completeness, errors, SQI distributions, RR statistics, and per-file detail.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import warnings
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import seaborn as sns

warnings.filterwarnings("ignore", category=FutureWarning)
sns.set_theme(style="whitegrid", palette="muted", font_scale=0.95)

EXPECTED_SUBDIRS = {"segments", "features", "rr_intervals", "sqi"}
PLOTS_SUBDIR = "plots"
_PATIENTS_PER_PAGE = 25


# ── helpers ──────────────────────────────────────────────────────────────────

def _sizeof_fmt(num: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if abs(num) < 1024:
            return f"{num:.1f} {unit}"
        num /= 1024
    return f"{num:.1f} TB"


def _load_json(path: Path) -> Optional[Any]:
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def _count_files(directory: Path, pattern: str = "*") -> int:
    if not directory.is_dir():
        return 0
    return sum(1 for _ in directory.glob(pattern))


def _dir_size(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    return sum(f.stat().st_size for f in directory.rglob("*") if f.is_file())


def _save_fig(fig: plt.Figure, plots_dir: Path, name: str) -> str:
    path = plots_dir / f"{name}.png"
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return f"{PLOTS_SUBDIR}/{name}.png"


def _extract_patient_id(path_str: str) -> str:
    return path_str.split("/")[0] if "/" in path_str else path_str


def _embed_plots(w, value, alt_text: str):
    """Embed one or more plot images into the markdown report."""
    if not value:
        return
    if isinstance(value, list):
        for p in value:
            w(f"![{alt_text}]({p})")
            w("")
    else:
        w(f"![{alt_text}]({value})")
        w("")


def _filter_by_signal(file_infos: List[Dict], signal: Optional[str]) -> List[Dict]:
    """Return file_infos filtered to a specific signal type, or all if None."""
    if signal is None:
        return file_infos
    return [f for f in file_infos if f.get("signal_type", "").upper() == signal.upper()]


def _signal_groups(file_infos: List[Dict]) -> List[Tuple[Optional[str], str, str]]:
    """Return (filter_value, label, suffix) tuples for total + each signal type present."""
    types = set(f.get("signal_type", "N/A").upper() for f in file_infos)
    groups: List[Tuple[Optional[str], str, str]] = [(None, "All Signals", "all")]
    for t in sorted(types):
        if t in ("PPG", "ECG"):
            groups.append((t, t, t.lower()))
    return groups


def _split_sqi_by_quality(file_infos: List[Dict]) -> Tuple[
    Dict[str, List[float]], Dict[str, List[float]]
]:
    """Split per-window SQI values into normal and abnormal groups
    using the composite quality label for each window."""
    normal_vals: Dict[str, List[float]] = defaultdict(list)
    abnormal_vals: Dict[str, List[float]] = defaultdict(list)
    for f in file_infos:
        quality = f.get("composite_quality", [])
        if not quality:
            continue
        for metric, vals in f.get("sqi_values", {}).items():
            n = min(len(vals), len(quality))
            for j in range(n):
                if quality[j] == "normal":
                    normal_vals[metric].append(vals[j])
                else:
                    abnormal_vals[metric].append(vals[j])
    return dict(normal_vals), dict(abnormal_vals)


def _split_rr_by_quality(file_infos: List[Dict]) -> Tuple[
    List[float], List[float], List[float], List[float]
]:
    """Split RR means/stds into normal and abnormal groups.

    Uses the per-file majority quality label (>50% normal windows → normal file).
    """
    norm_means, norm_stds = [], []
    abn_means, abn_stds = [], []
    for f in file_infos:
        means = f.get("rr_means", [])
        stds = f.get("rr_stds", [])
        if not means:
            continue
        n_norm = f.get("normal_segments", 0)
        n_abn = f.get("abnormal_segments", 0)
        if n_norm >= n_abn:
            norm_means.extend(means)
            norm_stds.extend(stds)
        else:
            abn_means.extend(means)
            abn_stds.extend(stds)
    return norm_means, norm_stds, abn_means, abn_stds


# ── scanning ─────────────────────────────────────────────────────────────────

def find_file_output_dirs(output_base: Path) -> List[Path]:
    results = []
    for sqi_dir in sorted(output_base.rglob("sqi")):
        if sqi_dir.is_dir():
            parent = sqi_dir.parent
            if parent not in results:
                results.append(parent)
    for rr_dir in sorted(output_base.rglob("rr_intervals")):
        if rr_dir.is_dir():
            parent = rr_dir.parent
            if parent not in results:
                results.append(parent)
    return sorted(results)


def analyse_file_output(file_dir: Path, output_base: Path) -> Dict[str, Any]:
    rel = file_dir.relative_to(output_base)
    info: Dict[str, Any] = {"path": str(rel), "abs_path": str(file_dir)}

    present_subdirs = {d.name for d in file_dir.iterdir() if d.is_dir()}
    info["subdirs_present"] = sorted(present_subdirs & EXPECTED_SUBDIRS)
    info["subdirs_missing"] = sorted(EXPECTED_SUBDIRS - present_subdirs)

    seg_dir = file_dir / "segments"
    info["segment_csvs"] = _count_files(seg_dir, "*.csv")
    info["segments_size"] = _dir_size(seg_dir)

    rr_dir = file_dir / "rr_intervals"
    info["rr_txts"] = _count_files(rr_dir, "*.txt")
    info["rr_json_exists"] = (rr_dir / "rr.json").is_file()
    info["rr_size"] = _dir_size(rr_dir)

    rr_json = _load_json(rr_dir / "rr.json")
    if rr_json and isinstance(rr_json, dict):
        info["rr_json_segments"] = len(rr_json)
        rr_entries = [v for v in rr_json.values() if isinstance(v, dict)]
        info["rr_total_intervals"] = sum(v.get("count", 0) for v in rr_entries)
        means = [v["mean_ms"] for v in rr_entries if "mean_ms" in v]
        stds = [v["std_ms"] for v in rr_entries if "std_ms" in v]
        info["rr_means"] = means
        info["rr_stds"] = stds
        info["rr_mean_ms_range"] = (round(min(means), 1), round(max(means), 1)) if means else None
    else:
        info["rr_json_segments"] = 0
        info["rr_total_intervals"] = 0
        info["rr_means"] = []
        info["rr_stds"] = []

    feat_dir = file_dir / "features"
    info["feature_csvs"] = _count_files(feat_dir, "*.csv")
    info["features_size"] = _dir_size(feat_dir)

    sqi_dir = file_dir / "sqi"
    info["sqi_json_exists"] = (sqi_dir / "sqi.json").is_file()
    info["sqi_size"] = _dir_size(sqi_dir)

    sqi_json = _load_json(sqi_dir / "sqi.json")
    if sqi_json and isinstance(sqi_json, dict):
        info["signal_type"] = sqi_json.get("signal_type", "N/A")
        info["signal_column"] = sqi_json.get("signal_column", "N/A")
        info["total_samples"] = sqi_json.get("total_samples", 0)
        info["total_duration_s"] = sqi_json.get("total_duration_seconds", 0)
        info["sampling_rate"] = sqi_json.get("sampling_rate", 0)
        info["normal_segments"] = sqi_json.get("normal_segment_count", 0)
        info["abnormal_segments"] = sqi_json.get("abnormal_segment_count", 0)
        info["total_segments"] = info["normal_segments"] + info["abnormal_segments"]
        info["sqi_metrics"] = list(sqi_json.get("sqi_metrics", {}).keys())
        info["sqi_error"] = None

        sqi_values: Dict[str, List[float]] = {}
        sqi_qualities: Dict[str, List[str]] = {}
        for mname, mdata in sqi_json.get("sqi_metrics", {}).items():
            if isinstance(mdata, dict) and "values" in mdata:
                sqi_values[mname] = mdata["values"]
                sqi_qualities[mname] = mdata.get("quality", [])
        info["sqi_values"] = sqi_values
        info["sqi_qualities"] = sqi_qualities

        info["threshold_method"] = sqi_json.get("threshold_method", "value")
        comp = sqi_json.get("composite", {})
        info["composite_scores"] = comp.get("scores", [])
        info["composite_quality"] = comp.get("quality", [])
        info["composite_threshold"] = comp.get("score_threshold", None)
        info["composite_details"] = comp.get("details", {})
    else:
        info["sqi_error"] = "sqi.json missing or unreadable"
        info["sqi_values"] = {}
        info["sqi_qualities"] = {}
        info["composite_scores"] = []
        info["composite_quality"] = []
        info["composite_details"] = {}

    return info


def analyse_summary(output_base: Path) -> Dict[str, Any]:
    path = output_base / "sqi_summary.json"
    if not path.is_file():
        return {"exists": False}
    data = _load_json(path)
    if not isinstance(data, list):
        return {"exists": True, "readable": False}

    ok = [e for e in data if "error" not in e]
    errors = [e for e in data if "error" in e]
    error_counts = Counter(e.get("error", "")[:120] for e in errors)
    return {
        "exists": True, "readable": True,
        "total": len(data), "ok": len(ok), "errors": len(errors),
        "error_counts": error_counts,
    }


# ── plotting ─────────────────────────────────────────────────────────────────

def _draw_patient_stacked_bars(ax, patients, data_by_patient, all_types, colors_map,
                               ylabel: str, title: str):
    """Draw a stacked bar chart for a list of patients (reusable helper)."""
    x = np.arange(len(patients))
    bottom = np.zeros(len(patients))
    for sig_t in all_types:
        vals = [data_by_patient[p].get(sig_t, 0) for p in patients]
        ax.bar(x, vals, bottom=bottom, label=sig_t,
               color=colors_map.get(sig_t, "#7f8c8d"), edgecolor="white")
        bottom += np.array(vals)
    ax.set_xticks(x)
    ax.set_xticklabels(patients, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(fontsize=8)


def plot_processing_overview(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    valid = [f for f in file_infos if f.get("sqi_error") is None]
    if not valid:
        return []

    colors_map = {"PPG": "#3498db", "ECG": "#e74c3c", "N/A": "#95a5a6"}
    types = Counter(f.get("signal_type", "N/A") for f in valid)
    labels_t = sorted(types.keys())
    vals_t = [types[l] for l in labels_t]
    cols_t = [colors_map.get(l, "#7f8c8d") for l in labels_t]

    patient_type: Dict[str, Counter] = defaultdict(Counter)
    patient_dur: Dict[str, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for f in valid:
        pid = _extract_patient_id(f["path"])
        sig = f.get("signal_type", "N/A")
        patient_type[pid][sig] += 1
        patient_dur[pid][sig] += f.get("total_duration_s", 0) / 3600
    patients_sorted = sorted(patient_type.keys())
    all_types = sorted({t for c in patient_type.values() for t in c})

    # Summary figure (signal type totals only)
    fig, ax = plt.subplots(figsize=(5, 4))
    bars = ax.bar(labels_t, vals_t, color=cols_t, edgecolor="white", width=0.5)
    for bar, v in zip(bars, vals_t):
        ax.text(bar.get_x() + bar.get_width() / 2, v + max(vals_t) * 0.02,
                str(v), ha="center", fontweight="bold")
    ax.set_ylabel("Number of files")
    ax.set_title("Files by Signal Type")
    fig.tight_layout()
    paths = [_save_fig(fig, plots_dir, "01a_overview_summary")]

    # Paginated per-patient detail plots
    pages = [patients_sorted[i:i + _PATIENTS_PER_PAGE]
             for i in range(0, len(patients_sorted), _PATIENTS_PER_PAGE)]
    for page_idx, page_patients in enumerate(pages):
        n_pages = len(pages)
        suffix = f" (page {page_idx + 1}/{n_pages})" if n_pages > 1 else ""
        fig, axes = plt.subplots(1, 2, figsize=(max(10, len(page_patients) * 0.55), 5))
        _draw_patient_stacked_bars(axes[0], page_patients, patient_type, all_types,
                                   colors_map, "Number of files",
                                   f"Files per Patient{suffix}")
        _draw_patient_stacked_bars(axes[1], page_patients, patient_dur, all_types,
                                   colors_map, "Hours",
                                   f"Recording Hours per Patient{suffix}")
        fig.tight_layout()
        paths.append(_save_fig(fig, plots_dir, f"01b_overview_patients_p{page_idx + 1}"))

    return paths


def plot_signal_type_and_duration(file_infos: List[Dict], plots_dir: Path) -> Optional[str]:
    valid = [f for f in file_infos if f.get("sqi_error") is None]
    if not valid:
        return None

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    types = [f.get("signal_type", "N/A") for f in valid]
    tc = Counter(types)
    colors_map = {"PPG": "#3498db", "ECG": "#e74c3c", "N/A": "#95a5a6"}
    labels_t = list(tc.keys())
    vals_t = [tc[l] for l in labels_t]
    cols_t = [colors_map.get(l, "#7f8c8d") for l in labels_t]
    axes[0].pie(vals_t, labels=labels_t, colors=cols_t, autopct="%1.0f%%", startangle=90)
    axes[0].set_title("Signal Type Distribution")

    durations = [f["total_duration_s"] / 60 for f in valid if f.get("total_duration_s", 0) > 0]
    if durations:
        sns.histplot(durations, bins=30, kde=True, ax=axes[1], color="#3498db", edgecolor="white")
        axes[1].set_xlabel("Duration (minutes)")
        axes[1].set_ylabel("Count")
        axes[1].set_title("Recording Duration Distribution")

    fig.tight_layout()
    return _save_fig(fig, plots_dir, "02_signal_type_duration")


def plot_segment_quality(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    valid = [f for f in file_infos if f.get("sqi_error") is None and f.get("total_segments", 0) > 0]
    if not valid:
        return []

    normal = [f["normal_segments"] for f in valid]
    abnormal = [f["abnormal_segments"] for f in valid]
    ratios = [f["normal_segments"] / f["total_segments"] * 100 for f in valid]

    # Summary figure
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    total_n = sum(normal)
    total_a = sum(abnormal)
    axes[0].pie([total_n, total_a], labels=["Normal", "Abnormal"],
                colors=["#2ecc71", "#e74c3c"], autopct="%1.1f%%", startangle=90)
    axes[0].set_title("Overall Segment Quality")

    sns.histplot(ratios, bins=20, kde=True, ax=axes[1], color="#2ecc71", edgecolor="white")
    axes[1].set_xlabel("Normal segment ratio (%)")
    axes[1].set_ylabel("Number of files")
    axes[1].set_title("Per-File Normal Ratio")
    axes[1].axvline(np.median(ratios), color="#e67e22", ls="--", label=f"Median: {np.median(ratios):.0f}%")
    axes[1].legend()

    fig.tight_layout()
    paths = [_save_fig(fig, plots_dir, "03a_segment_quality_summary")]

    # Paginated per-patient segment quality
    patient_segs: Dict[str, Dict[str, int]] = defaultdict(lambda: {"normal": 0, "abnormal": 0})
    for f in valid:
        pid = _extract_patient_id(f["path"])
        patient_segs[pid]["normal"] += f.get("normal_segments", 0)
        patient_segs[pid]["abnormal"] += f.get("abnormal_segments", 0)
    patients_sorted = sorted(patient_segs.keys())

    pages = [patients_sorted[i:i + _PATIENTS_PER_PAGE]
             for i in range(0, len(patients_sorted), _PATIENTS_PER_PAGE)]
    for page_idx, page_patients in enumerate(pages):
        n_pages = len(pages)
        suffix = f" (page {page_idx + 1}/{n_pages})" if n_pages > 1 else ""
        fig, ax = plt.subplots(figsize=(max(8, len(page_patients) * 0.5), 5))
        x = np.arange(len(page_patients))
        n_vals = [patient_segs[p]["normal"] for p in page_patients]
        a_vals = [patient_segs[p]["abnormal"] for p in page_patients]
        ax.bar(x, n_vals, label="Normal", color="#2ecc71", edgecolor="white")
        ax.bar(x, a_vals, bottom=n_vals, label="Abnormal", color="#e74c3c", edgecolor="white")
        ax.set_xticks(x)
        ax.set_xticklabels(page_patients, rotation=45, ha="right", fontsize=8)
        ax.set_ylabel("Segments")
        ax.set_title(f"Segments per Patient{suffix}")
        ax.legend(fontsize=8)
        fig.tight_layout()
        paths.append(_save_fig(fig, plots_dir, f"03b_segment_quality_patients_p{page_idx + 1}"))

    return paths


def _plot_sqi_effect_group(
    infos: List[Dict], plots_dir: Path, prefix: str, label: str,
) -> List[str]:
    """Violin, effect-size, and median dot plots for one signal group."""
    import pandas as pd
    norm_vals, abn_vals = _split_sqi_by_quality(infos)
    all_metrics = sorted(set(list(norm_vals.keys()) + list(abn_vals.keys())))
    if not all_metrics:
        return []

    short_map = {m: m.replace("_sqi", "").replace("_", " ").title() for m in all_metrics}
    paths: List[str] = []

    # --- 1. Split violin plot ---
    rows_list = []
    for m in all_metrics:
        short = short_map[m]
        nv = np.array([v for v in norm_vals.get(m, []) if np.isfinite(v)])
        av = np.array([v for v in abn_vals.get(m, []) if np.isfinite(v)])
        if len(nv) < 10 and len(av) < 10:
            continue
        combined = np.concatenate([nv, av]) if len(nv) + len(av) > 0 else np.array([0])
        lo, hi = _robust_xlim(combined)
        for v in nv:
            if lo <= v <= hi:
                rows_list.append({"Metric": short, "Group": "Normal", "Value": v})
        for v in av:
            if lo <= v <= hi:
                rows_list.append({"Metric": short, "Group": "Abnormal", "Value": v})

    if rows_list:
        df = pd.DataFrame(rows_list)
        fig, ax = plt.subplots(figsize=(14, 5.5))
        sns.violinplot(data=df, x="Metric", y="Value", hue="Group",
                       split=True, inner="quart", linewidth=0.8,
                       palette={"Normal": "#2ecc71", "Abnormal": "#e74c3c"},
                       ax=ax, density_norm="width")
        ax.set_title(f"Split Violin (Normal vs Abnormal) — {label}", fontsize=12)
        ax.tick_params(axis="x", labelsize=7, rotation=25)
        ax.set_xlabel("")
        ax.axhline(0, color="grey", ls="--", lw=0.5, alpha=0.5)
        ax.legend(fontsize=8, loc="upper right")
        fig.tight_layout()
        paths.append(_save_fig(fig, plots_dir, f"{prefix}_violin"))

    # --- 2. Effect-size bar chart ---
    effect_sizes = []
    for m in all_metrics:
        short = short_map[m]
        nv = np.array([v for v in norm_vals.get(m, []) if np.isfinite(v)])
        av = np.array([v for v in abn_vals.get(m, []) if np.isfinite(v)])
        if len(nv) < 10 or len(av) < 10:
            continue
        med_n = np.median(nv)
        med_a = np.median(av)
        mad_n = np.median(np.abs(nv - med_n)) * 1.4826
        mad_a = np.median(np.abs(av - med_a)) * 1.4826
        pooled_mad = np.sqrt((mad_n**2 + mad_a**2) / 2)
        d = (med_a - med_n) / pooled_mad if pooled_mad > 1e-12 else 0
        effect_sizes.append({"Metric": short, "Cohen_d": d, "abs_d": abs(d)})

    if effect_sizes:
        df_es = pd.DataFrame(effect_sizes).sort_values("abs_d", ascending=True)

        fig2, ax2 = plt.subplots(figsize=(8, max(4, len(df_es) * 0.4)))
        colors = ["#e74c3c" if d > 0 else "#3498db" for d in df_es["Cohen_d"]]
        ax2.barh(df_es["Metric"], df_es["Cohen_d"], color=colors, edgecolor="white", height=0.6)
        ax2.axvline(0, color="black", lw=0.8)
        for thresh, _ in [(0.2, "small"), (0.5, "medium"), (0.8, "large")]:
            ax2.axvline(thresh, color="#95a5a6", ls=":", lw=0.8, alpha=0.6)
            ax2.axvline(-thresh, color="#95a5a6", ls=":", lw=0.8, alpha=0.6)
        ax2.set_xlabel("Cohen's d  (red = abnormal higher, blue = abnormal lower)")
        ax2.set_title(f"Effect Size — {label}", fontsize=12)
        ax2.tick_params(axis="y", labelsize=8)
        fig2.tight_layout()
        paths.append(_save_fig(fig2, plots_dir, f"{prefix}_effect"))

        # --- 3. Median dot plot ---
        med_rows = []
        for m in all_metrics:
            short = short_map[m]
            nv = np.array([v for v in norm_vals.get(m, []) if np.isfinite(v)])
            av = np.array([v for v in abn_vals.get(m, []) if np.isfinite(v)])
            if len(nv) < 10 or len(av) < 10:
                continue
            med_rows.append({
                "Metric": short,
                "median_normal": float(np.median(nv)),
                "median_abnormal": float(np.median(av)),
            })
        if med_rows:
            df_med = pd.DataFrame(med_rows)
            df_med["abs_diff"] = (df_med["median_abnormal"] - df_med["median_normal"]).abs()
            df_med = df_med.sort_values("abs_diff", ascending=True)

            all_medians = np.concatenate([
                df_med["median_normal"].values, df_med["median_abnormal"].values])
            lo, hi = _robust_xlim(all_medians)

            fig3, ax3 = plt.subplots(figsize=(10, max(4, len(df_med) * 0.4)))
            y_pos = np.arange(len(df_med))
            for i, (_, row) in enumerate(df_med.iterrows()):
                x0 = np.clip(row["median_normal"], lo, hi)
                x1 = np.clip(row["median_abnormal"], lo, hi)
                ax3.plot([x0, x1], [i, i], color="#bdc3c7", lw=1.5, zorder=1)
            norm_clipped = np.clip(df_med["median_normal"].values, lo, hi)
            abn_clipped = np.clip(df_med["median_abnormal"].values, lo, hi)
            ax3.scatter(norm_clipped, y_pos, color="#2ecc71", s=60,
                        zorder=2, label="Normal", edgecolors="white", linewidth=0.5)
            ax3.scatter(abn_clipped, y_pos, color="#e74c3c", s=60,
                        zorder=2, label="Abnormal", marker="D", edgecolors="white", linewidth=0.5)
            for i, (_, row) in enumerate(df_med.iterrows()):
                for val, clr in [(row["median_normal"], "#2ecc71"),
                                 (row["median_abnormal"], "#e74c3c")]:
                    if val > hi or val < lo:
                        ax3.annotate(f"{val:.1f}", xy=(np.clip(val, lo, hi), i),
                                     fontsize=6, color=clr, ha="left", va="bottom")
            ax3.set_yticks(y_pos)
            ax3.set_yticklabels(df_med["Metric"], fontsize=8)
            ax3.set_xlabel("Median SQI value")
            ax3.set_title(f"Median SQI: Normal vs Abnormal — {label}", fontsize=11)
            ax3.legend(fontsize=8, loc="lower right")
            ax3.set_xlim(lo, hi)
            ax3.grid(axis="x", alpha=0.3)
            fig3.tight_layout()
            paths.append(_save_fig(fig3, plots_dir, f"{prefix}_median"))

    return paths


def plot_sqi_effect_size(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    paths: List[str] = []
    for sig_filter, label, suffix in _signal_groups(file_infos):
        infos = _filter_by_signal(file_infos, sig_filter)
        paths += _plot_sqi_effect_group(infos, plots_dir, f"06_{suffix}", label)
    return paths


def _robust_xlim(vals: np.ndarray, margin: float = 3.0) -> Tuple[float, float]:
    """Return (lo, hi) x-limits that exclude extreme outliers.

    Uses Q25 - margin*IQR .. Q75 + margin*IQR (standard boxplot rule with
    adjustable margin), then snaps to the actual data range.
    """
    q1, q3 = np.percentile(vals, [25, 75])
    iqr = q3 - q1
    if iqr == 0:
        iqr = max(abs(q1), 1.0) * 0.5
    lo = q1 - margin * iqr
    hi = q3 + margin * iqr
    return max(lo, vals.min()), min(hi, vals.max())


def _plot_sqi_dist_group(
    infos: List[Dict], plots_dir: Path, prefix: str, label: str,
) -> List[str]:
    """Plot SQI distributions (overall + normal/abnormal) for one signal group."""
    all_vals: Dict[str, List[float]] = defaultdict(list)
    for f in infos:
        for metric, vals in f.get("sqi_values", {}).items():
            all_vals[metric].extend(vals)

    metrics = [m for m in all_vals if len(all_vals[m]) > 10]
    if not metrics:
        return []

    short_names = [m.replace("_sqi", "").replace("_", " ").title() for m in metrics]
    n = len(metrics)
    cols = min(3, n)
    rows = (n + cols - 1) // cols
    paths: List[str] = []

    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 3.5 * rows))
    if rows * cols == 1:
        axes = np.array([axes])
    axes_flat = axes.flatten()

    for i, (metric, short) in enumerate(zip(metrics, short_names)):
        ax = axes_flat[i]
        vals = np.array(all_vals[metric])
        vals_clean = vals[np.isfinite(vals)]
        if len(vals_clean) == 0:
            continue
        lo, hi = _robust_xlim(vals_clean)
        vals_clipped = vals_clean[(vals_clean >= lo) & (vals_clean <= hi)]
        n_outliers = len(vals_clean) - len(vals_clipped)
        sns.histplot(vals_clipped, bins=40, kde=True, ax=ax,
                     color=sns.color_palette("husl", n)[i], edgecolor="white")
        q25, q50, q75 = np.percentile(vals_clean, [25, 50, 75])
        ax.axvline(q50, color="#e74c3c", ls="--", lw=1.5, label=f"Median: {q50:.2f}")
        ax.axvline(q25, color="#f39c12", ls=":", lw=1, label=f"Q25: {q25:.2f}")
        ax.axvline(q75, color="#f39c12", ls=":", lw=1, label=f"Q75: {q75:.2f}")
        title = short
        if n_outliers:
            pct = n_outliers / len(vals_clean) * 100
            title += f"  ({n_outliers:,} outliers clipped, {pct:.1f}%)"
        ax.set_title(title, fontsize=9)
        ax.set_xlabel("")
        ax.legend(fontsize=7)

    for j in range(i + 1, len(axes_flat)):
        axes_flat[j].set_visible(False)

    fig.suptitle(f"SQI Distributions — {label}", fontsize=13, y=1.01)
    fig.tight_layout()
    paths.append(_save_fig(fig, plots_dir, f"{prefix}_distributions"))

    norm_vals, abn_vals = _split_sqi_by_quality(infos)
    if norm_vals or abn_vals:
        fig2, axes2 = plt.subplots(rows, cols, figsize=(5 * cols, 3.5 * rows))
        if rows * cols == 1:
            axes2 = np.array([axes2])
        axes2_flat = axes2.flatten()
        for i, (metric, short) in enumerate(zip(metrics, short_names)):
            ax = axes2_flat[i]
            nv = np.array(norm_vals.get(metric, []), dtype=float)
            av = np.array(abn_vals.get(metric, []), dtype=float)
            nv = nv[np.isfinite(nv)]
            av = av[np.isfinite(av)]
            all_clean = np.concatenate([nv, av]) if len(nv) + len(av) > 0 else np.array([0])
            lo, hi = _robust_xlim(all_clean)
            if len(nv) > 5:
                nv_c = nv[(nv >= lo) & (nv <= hi)]
                sns.kdeplot(nv_c, ax=ax, color="#2ecc71", fill=True, alpha=0.35,
                            label=f"Normal (n={len(nv):,})", linewidth=1.5)
            if len(av) > 5:
                av_c = av[(av >= lo) & (av <= hi)]
                sns.kdeplot(av_c, ax=ax, color="#e74c3c", fill=True, alpha=0.35,
                            label=f"Abnormal (n={len(av):,})", linewidth=1.5)
            ax.set_title(short, fontsize=9)
            ax.set_xlabel("")
            ax.legend(fontsize=7)
        for j in range(i + 1, len(axes2_flat)):
            axes2_flat[j].set_visible(False)
        fig2.suptitle(f"SQI Normal vs Abnormal — {label}", fontsize=13, y=1.01)
        fig2.tight_layout()
        paths.append(_save_fig(fig2, plots_dir, f"{prefix}_norm_abn"))

    return paths


def plot_sqi_distributions(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    paths: List[str] = []
    for sig_filter, label, suffix in _signal_groups(file_infos):
        infos = _filter_by_signal(file_infos, sig_filter)
        paths += _plot_sqi_dist_group(infos, plots_dir, f"04_{suffix}", label)
    return paths


def _plot_sqi_box_group(
    infos: List[Dict], plots_dir: Path, prefix: str, label: str,
) -> List[str]:
    """Plot SQI boxplots (overall + normal/abnormal) for one signal group."""
    import pandas as pd

    all_vals: Dict[str, List[float]] = defaultdict(list)
    for f in infos:
        for metric, vals in f.get("sqi_values", {}).items():
            all_vals[metric].extend(vals)
    metrics = [m for m in all_vals if len(all_vals[m]) > 10]
    if not metrics:
        return []

    fig, ax = plt.subplots(figsize=(12, 5))
    data_for_box = []
    labels_for_box = []
    for m in metrics:
        arr = np.array([v for v in all_vals[m] if np.isfinite(v)])
        lo, hi = _robust_xlim(arr)
        data_for_box.append(arr[(arr >= lo) & (arr <= hi)])
        labels_for_box.append(m.replace("_sqi", "").replace("_", "\n"))

    bp = ax.boxplot(data_for_box, patch_artist=True, labels=labels_for_box,
                    showfliers=True, flierprops=dict(marker=".", markersize=2, alpha=0.3))
    palette = sns.color_palette("husl", len(metrics))
    for patch, color in zip(bp["boxes"], palette):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax.set_ylabel("SQI Value")
    ax.set_title(f"SQI Metric Comparison — {label}")
    ax.tick_params(axis="x", labelsize=8)
    ax.axhline(0, color="grey", ls="--", lw=0.5, alpha=0.5)
    fig.tight_layout()
    paths = [_save_fig(fig, plots_dir, f"{prefix}_boxplots")]

    norm_vals, abn_vals = _split_sqi_by_quality(infos)
    if norm_vals or abn_vals:
        rows_list = []
        for m in metrics:
            short = m.replace("_sqi", "").replace("_", " ")
            nv = [v for v in norm_vals.get(m, []) if np.isfinite(v)]
            av = [v for v in abn_vals.get(m, []) if np.isfinite(v)]
            combined = np.array(nv + av)
            if len(combined) < 10:
                continue
            lo, hi = _robust_xlim(combined)
            for v in nv:
                if lo <= v <= hi:
                    rows_list.append({"Metric": short, "Group": "Normal", "Value": v})
            for v in av:
                if lo <= v <= hi:
                    rows_list.append({"Metric": short, "Group": "Abnormal", "Value": v})

        if rows_list:
            df = pd.DataFrame(rows_list)
            fig2, ax2 = plt.subplots(figsize=(14, 5))
            sns.boxplot(data=df, x="Metric", y="Value", hue="Group",
                        palette={"Normal": "#2ecc71", "Abnormal": "#e74c3c"},
                        showfliers=False, ax=ax2, linewidth=0.8)
            ax2.set_title(f"SQI Normal vs Abnormal — {label}")
            ax2.tick_params(axis="x", labelsize=7, rotation=20)
            ax2.set_xlabel("")
            ax2.axhline(0, color="grey", ls="--", lw=0.5, alpha=0.5)
            ax2.legend(fontsize=8)
            fig2.tight_layout()
            paths.append(_save_fig(fig2, plots_dir, f"{prefix}_boxplots_norm_abn"))

    return paths


def plot_sqi_boxplots(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    paths: List[str] = []
    for sig_filter, label, suffix in _signal_groups(file_infos):
        infos = _filter_by_signal(file_infos, sig_filter)
        paths += _plot_sqi_box_group(infos, plots_dir, f"05_{suffix}", label)
    return paths


def _plot_rr_group(
    infos: List[Dict], plots_dir: Path, prefix: str, label: str,
) -> List[str]:
    """RR interval statistics (overall + normal/abnormal) for one signal group."""
    all_means = []
    all_stds = []
    for f in infos:
        all_means.extend(f.get("rr_means", []))
        all_stds.extend(f.get("rr_stds", []))

    all_means = np.array([m for m in all_means if np.isfinite(m)])
    all_stds = np.array([s for s in all_stds if np.isfinite(s)])
    if len(all_means) == 0:
        return []

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    m_lo, m_hi = _robust_xlim(all_means)
    means_clipped = all_means[(all_means >= m_lo) & (all_means <= m_hi)]
    n_clip_m = len(all_means) - len(means_clipped)

    sns.histplot(means_clipped, bins=50, kde=True, ax=axes[0], color="#9b59b6", edgecolor="white")
    med = np.median(all_means)
    axes[0].axvline(med, color="#e74c3c", ls="--", label=f"Median: {med:.0f} ms")
    axes[0].set_xlabel("Mean RR interval (ms)")
    axes[0].set_ylabel("Number of segments")
    title_m = "Mean RR Distribution"
    if n_clip_m:
        title_m += f"  ({n_clip_m:,} outliers clipped)"
    axes[0].set_title(title_m, fontsize=10)
    axes[0].legend()

    s_lo, s_hi = 0, 1
    if len(all_stds) > 0:
        s_lo, s_hi = _robust_xlim(all_stds)
        stds_clipped = all_stds[(all_stds >= s_lo) & (all_stds <= s_hi)]
        n_clip_s = len(all_stds) - len(stds_clipped)
        sns.histplot(stds_clipped, bins=50, kde=True, ax=axes[1], color="#e67e22", edgecolor="white")
        axes[1].set_xlabel("Std RR interval (ms)")
        axes[1].set_ylabel("Number of segments")
        title_s = "RR Variability (Std)"
        if n_clip_s:
            title_s += f"  ({n_clip_s:,} outliers clipped)"
        axes[1].set_title(title_s, fontsize=10)

    if len(all_means) > 0 and len(all_stds) > 0 and len(all_means) == len(all_stds):
        mask = ((all_means >= m_lo) & (all_means <= m_hi) &
                (all_stds >= s_lo) & (all_stds <= s_hi))
        axes[2].scatter(all_means[mask], all_stds[mask], alpha=0.3, s=10, c="#3498db")
        axes[2].set_xlabel("Mean RR (ms)")
        axes[2].set_ylabel("Std RR (ms)")
        axes[2].set_title("Mean vs Std RR (outliers excluded)")
    else:
        axes[2].text(0.5, 0.5, "Lengths differ", ha="center", va="center",
                     transform=axes[2].transAxes)

    fig.suptitle(f"RR Interval Statistics — {label}", fontsize=13, y=1.02)
    fig.tight_layout()
    paths = [_save_fig(fig, plots_dir, f"{prefix}_rr_all")]

    nm, ns, am, a_s = _split_rr_by_quality(infos)
    nm = np.array([v for v in nm if np.isfinite(v)])
    ns = np.array([v for v in ns if np.isfinite(v)])
    am = np.array([v for v in am if np.isfinite(v)])
    a_s = np.array([v for v in a_s if np.isfinite(v)])

    if len(nm) > 10 or len(am) > 10:
        fig2, axes2 = plt.subplots(1, 3, figsize=(14, 4.5))

        combined_m = np.concatenate([nm, am]) if len(nm) + len(am) > 0 else all_means
        cm_lo, cm_hi = _robust_xlim(combined_m)
        combined_s = np.concatenate([ns, a_s]) if len(ns) + len(a_s) > 0 else all_stds
        cs_lo, cs_hi = _robust_xlim(combined_s) if len(combined_s) > 0 else (0, 1)

        if len(nm) > 5:
            nc = nm[(nm >= cm_lo) & (nm <= cm_hi)]
            sns.kdeplot(nc, ax=axes2[0], color="#2ecc71", fill=True, alpha=0.3,
                        label=f"Normal (n={len(nm):,})", linewidth=1.5)
        if len(am) > 5:
            ac = am[(am >= cm_lo) & (am <= cm_hi)]
            sns.kdeplot(ac, ax=axes2[0], color="#e74c3c", fill=True, alpha=0.3,
                        label=f"Abnormal (n={len(am):,})", linewidth=1.5)
        axes2[0].set_xlabel("Mean RR (ms)")
        axes2[0].set_title("Mean RR — Normal vs Abnormal")
        axes2[0].legend(fontsize=8)

        if len(ns) > 5:
            nc = ns[(ns >= cs_lo) & (ns <= cs_hi)]
            sns.kdeplot(nc, ax=axes2[1], color="#2ecc71", fill=True, alpha=0.3,
                        label=f"Normal (n={len(ns):,})", linewidth=1.5)
        if len(a_s) > 5:
            ac = a_s[(a_s >= cs_lo) & (a_s <= cs_hi)]
            sns.kdeplot(ac, ax=axes2[1], color="#e74c3c", fill=True, alpha=0.3,
                        label=f"Abnormal (n={len(a_s):,})", linewidth=1.5)
        axes2[1].set_xlabel("Std RR (ms)")
        axes2[1].set_title("RR Variability — Normal vs Abnormal")
        axes2[1].legend(fontsize=8)

        if len(nm) > 0 and len(nm) == len(ns):
            m_mask = (nm >= cm_lo) & (nm <= cm_hi) & (ns >= cs_lo) & (ns <= cs_hi)
            axes2[2].scatter(nm[m_mask], ns[m_mask], alpha=0.25, s=10, c="#2ecc71",
                             label="Normal")
        if len(am) > 0 and len(am) == len(a_s):
            m_mask = (am >= cm_lo) & (am <= cm_hi) & (a_s >= cs_lo) & (a_s <= cs_hi)
            axes2[2].scatter(am[m_mask], a_s[m_mask], alpha=0.4, s=15, c="#e74c3c",
                             label="Abnormal", marker="x")
        axes2[2].set_xlabel("Mean RR (ms)")
        axes2[2].set_ylabel("Std RR (ms)")
        axes2[2].set_title("Mean vs Std — Normal vs Abnormal")
        axes2[2].legend(fontsize=8)

        fig2.suptitle(f"RR Normal vs Abnormal — {label}", fontsize=13, y=1.02)
        fig2.tight_layout()
        paths.append(_save_fig(fig2, plots_dir, f"{prefix}_rr_norm_abn"))

    return paths


def plot_rr_statistics(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    paths: List[str] = []
    for sig_filter, label, suffix in _signal_groups(file_infos):
        infos = _filter_by_signal(file_infos, sig_filter)
        paths += _plot_rr_group(infos, plots_dir, f"07_{suffix}", label)
    return paths


def plot_disk_usage(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    cat_sizes = defaultdict(int)
    for f in file_infos:
        cat_sizes["segments"] += f.get("segments_size", 0)
        cat_sizes["rr_intervals"] += f.get("rr_size", 0)
        cat_sizes["features"] += f.get("features_size", 0)
        cat_sizes["sqi"] += f.get("sqi_size", 0)

    labels = [k for k, v in cat_sizes.items() if v > 0]
    sizes = [cat_sizes[k] for k in labels]
    if not sizes:
        return []

    # Summary pie chart
    fig, ax = plt.subplots(figsize=(5, 4))
    colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12"]
    ax.pie(sizes, labels=labels, colors=colors[:len(labels)], autopct="%1.1f%%", startangle=90)
    ax.set_title("Disk Usage by Category")
    fig.tight_layout()
    paths = [_save_fig(fig, plots_dir, "07a_disk_usage_summary")]

    # Paginated per-patient disk usage
    per_patient: Dict[str, int] = defaultdict(int)
    for f in file_infos:
        pid = _extract_patient_id(f["path"])
        per_patient[pid] += (f.get("segments_size", 0) + f.get("rr_size", 0)
                             + f.get("features_size", 0) + f.get("sqi_size", 0))
    pids = sorted(per_patient.keys())

    pages = [pids[i:i + _PATIENTS_PER_PAGE] for i in range(0, len(pids), _PATIENTS_PER_PAGE)]
    for page_idx, page_pids in enumerate(pages):
        n_pages = len(pages)
        suffix = f" (page {page_idx + 1}/{n_pages})" if n_pages > 1 else ""
        fig, ax = plt.subplots(figsize=(max(8, len(page_pids) * 0.5), 5))
        p_sizes = [per_patient[p] / (1024 ** 2) for p in page_pids]
        palette = sns.color_palette("Set2", len(page_pids))
        ax.bar(range(len(page_pids)), p_sizes, color=palette, edgecolor="white")
        ax.set_xticks(range(len(page_pids)))
        ax.set_xticklabels(page_pids, rotation=45, ha="right", fontsize=8)
        ax.set_ylabel("Size (MB)")
        ax.set_title(f"Disk Usage per Patient{suffix}")
        fig.tight_layout()
        paths.append(_save_fig(fig, plots_dir, f"07b_disk_usage_patients_p{page_idx + 1}"))

    return paths


def _build_patient_metric_matrix(
    file_infos: List[Dict], metrics: List[str], patients: List[str],
    quality_filter: Optional[str] = None,
) -> np.ndarray:
    """Build a (patients x metrics) matrix of median SQI values.

    If quality_filter is 'normal' or 'abnormal', only include windows with
    that composite quality label.
    """
    accum: Dict[str, Dict[str, List[float]]] = {p: {m: [] for m in metrics} for p in patients}
    for f in file_infos:
        pid = _extract_patient_id(f["path"])
        if pid not in accum:
            continue
        quality = f.get("composite_quality", [])
        for m in metrics:
            vals = f.get("sqi_values", {}).get(m, [])
            n = min(len(vals), len(quality)) if quality else len(vals)
            for j in range(n):
                if quality_filter and quality:
                    if quality[j] != quality_filter:
                        continue
                v = vals[j]
                if np.isfinite(v):
                    accum[pid][m].append(v)
            if not quality and quality_filter is None:
                accum[pid][m].extend(v for v in vals if np.isfinite(v))

    matrix = []
    for p in patients:
        row = []
        for m in metrics:
            vs = accum[p][m]
            row.append(float(np.median(vs)) if vs else np.nan)
        matrix.append(row)
    return np.array(matrix)


def _render_heatmap_pages(
    matrix_arr: np.ndarray, patients: List[str], short_metrics: List[str],
    plots_dir: Path, filename_prefix: str, title_prefix: str,
    cmap: str = "RdYlGn", center: Optional[float] = 0,
    cbar_label: str = "Median SQI",
) -> List[str]:
    """Render paginated heatmap pages for a given matrix."""
    finite_vals = matrix_arr[np.isfinite(matrix_arr)]
    if len(finite_vals) == 0:
        return []
    q05, q95 = np.nanpercentile(finite_vals, [5, 95])
    vmin, vmax = q05, q95
    display_arr = np.clip(matrix_arr, vmin, vmax)

    pages = [patients[i:i + _PATIENTS_PER_PAGE]
             for i in range(0, len(patients), _PATIENTS_PER_PAGE)]
    paths: List[str] = []
    for page_idx, page_patients in enumerate(pages):
        n_pages = len(pages)
        suffix = f" (page {page_idx + 1}/{n_pages})" if n_pages > 1 else ""
        start = page_idx * _PATIENTS_PER_PAGE
        end = start + len(page_patients)
        sub_display = display_arr[start:end]
        sub_raw = matrix_arr[start:end]
        annot_strs = np.array([[f"{v:.2f}" if np.isfinite(v) else ""
                                for v in row] for row in sub_raw])
        fig, ax = plt.subplots(
            figsize=(max(10, len(short_metrics) * 0.9), max(4, len(page_patients) * 0.45)))
        sns.heatmap(sub_display, xticklabels=short_metrics, yticklabels=page_patients,
                    annot=annot_strs, fmt="", cmap=cmap, center=center, ax=ax,
                    linewidths=0.5, linecolor="white", cbar_kws={"label": cbar_label},
                    vmin=vmin, vmax=vmax)
        ax.set_title(f"{title_prefix}{suffix}")
        ax.tick_params(axis="x", labelsize=8, rotation=45)
        ax.tick_params(axis="y", labelsize=9)
        fig.tight_layout()
        paths.append(_save_fig(fig, plots_dir, f"{filename_prefix}_p{page_idx + 1}"))
    return paths


def _plot_heatmap_group(
    infos: List[Dict], plots_dir: Path, prefix: str, label: str,
) -> List[str]:
    """Heatmap set (all + normal + difference) for one signal group."""
    valid = [f for f in infos if f.get("sqi_error") is None and f.get("total_segments", 0) > 0]
    if len(valid) < 2:
        return []

    all_metrics = set()
    for f in valid:
        all_metrics.update(f.get("sqi_values", {}).keys())
    metrics = sorted(all_metrics)
    if not metrics:
        return []

    patients = sorted(set(_extract_patient_id(f["path"]) for f in valid))
    short_metrics = [m.replace("_sqi", "").replace("_", " ") for m in metrics]

    mat_all = _build_patient_metric_matrix(valid, metrics, patients)
    paths = _render_heatmap_pages(mat_all, patients, short_metrics, plots_dir,
                                  f"{prefix}_all", f"Median SQI (all) — {label}")

    mat_norm = _build_patient_metric_matrix(valid, metrics, patients, quality_filter="normal")
    paths += _render_heatmap_pages(mat_norm, patients, short_metrics, plots_dir,
                                   f"{prefix}_normal", f"Median SQI (normal) — {label}")

    mat_abn = _build_patient_metric_matrix(valid, metrics, patients, quality_filter="abnormal")
    if np.any(np.isfinite(mat_abn)):
        mat_diff = mat_abn - mat_norm
        paths += _render_heatmap_pages(
            mat_diff, patients, short_metrics, plots_dir,
            f"{prefix}_diff", f"SQI Δ (abn − norm) — {label}",
            cmap="coolwarm", center=0, cbar_label="Δ Median SQI",
        )

    return paths


def plot_per_patient_quality_heatmap(file_infos: List[Dict], plots_dir: Path) -> List[str]:
    paths: List[str] = []
    for sig_filter, label, suffix in _signal_groups(file_infos):
        infos = _filter_by_signal(file_infos, sig_filter)
        paths += _plot_heatmap_group(infos, plots_dir, f"09_{suffix}", label)
    return paths


def plot_composite_scores(file_infos: List[Dict], plots_dir: Path) -> Optional[str]:
    all_scores = []
    all_quality = []
    for f in file_infos:
        all_scores.extend(f.get("composite_scores", []))
        all_quality.extend(f.get("composite_quality", []))
    if not all_scores:
        return None

    scores = np.array(all_scores)
    scores = scores[np.isfinite(scores)]
    if len(scores) == 0:
        return None

    threshold = None
    for f in file_infos:
        t = f.get("composite_threshold")
        if t is not None:
            threshold = t
            break

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    sns.histplot(scores, bins=50, kde=True, ax=axes[0], color="#8e44ad", edgecolor="white")
    if threshold is not None:
        axes[0].axvline(threshold, color="#e74c3c", ls="--", lw=2, label=f"Threshold: {threshold}")
    med = np.median(scores)
    axes[0].axvline(med, color="#f39c12", ls=":", lw=1.5, label=f"Median: {med:.3f}")
    axes[0].set_xlabel("Composite Score")
    axes[0].set_ylabel("Number of windows")
    axes[0].set_title("Composite Score Distribution")
    axes[0].legend(fontsize=8)

    qc = Counter(all_quality)
    labels_q = ["normal", "abnormal"]
    vals_q = [qc.get(l, 0) for l in labels_q]
    colors_q = ["#2ecc71", "#e74c3c"]
    axes[1].bar(labels_q, vals_q, color=colors_q, edgecolor="white", width=0.5)
    for i, v in enumerate(vals_q):
        axes[1].text(i, v + max(vals_q) * 0.02, str(v), ha="center", fontweight="bold")
    axes[1].set_ylabel("Number of windows")
    axes[1].set_title("Composite Quality Classification")

    per_file_means = []
    for f in file_infos:
        cs = f.get("composite_scores", [])
        if cs:
            per_file_means.append(np.mean(cs))
    if per_file_means:
        sns.histplot(per_file_means, bins=30, kde=True, ax=axes[2], color="#3498db", edgecolor="white")
        axes[2].set_xlabel("Mean Composite Score per File")
        axes[2].set_ylabel("Number of files")
        axes[2].set_title("Per-File Mean Composite Score")
        if threshold is not None:
            axes[2].axvline(threshold, color="#e74c3c", ls="--", lw=1.5, label=f"Threshold: {threshold}")
            axes[2].legend(fontsize=8)

    fig.tight_layout()
    return _save_fig(fig, plots_dir, "09_composite_scores")


def plot_composite_components(file_infos: List[Dict], plots_dir: Path) -> Optional[str]:
    component_names = ["quantile_rank", "tail_probability", "modified_z_score", "rolling_variance"]
    all_trapz: List[float] = []
    component_data: Dict[str, List[float]] = {c: [] for c in component_names}

    for f in file_infos:
        details = f.get("composite_details", {})
        if not details:
            continue
        trapz = details.get("trapz_ratio", [])
        all_trapz.extend(trapz)
        for metric_name, metric_detail in details.items():
            if metric_name == "trapz_ratio":
                continue
            if not isinstance(metric_detail, dict):
                continue
            for comp in component_names:
                vals = metric_detail.get(comp, [])
                component_data[comp].extend(vals)

    has_data = any(len(v) > 0 for v in component_data.values()) or len(all_trapz) > 0
    if not has_data:
        return None

    all_components = component_names + (["trapz_ratio"] if all_trapz else [])
    n = len(all_components)
    cols = min(3, n)
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 3.8 * rows))
    if rows * cols == 1:
        axes = np.array([axes])
    axes_flat = axes.flatten()

    palette = sns.color_palette("Set2", n)
    titles = {
        "quantile_rank": "Quantile Rank",
        "tail_probability": "Tail Probability",
        "modified_z_score": "Modified Z-Score",
        "rolling_variance": "Rolling Variance",
        "trapz_ratio": "Trapz Area Ratio",
    }

    for i, comp in enumerate(all_components):
        ax = axes_flat[i]
        vals = np.array(all_trapz if comp == "trapz_ratio" else component_data.get(comp, []))
        vals = vals[np.isfinite(vals)]
        if len(vals) == 0:
            ax.set_visible(False)
            continue
        clip_hi = np.percentile(vals, 99.5) if len(vals) > 100 else vals.max()
        clip_lo = np.percentile(vals, 0.5) if len(vals) > 100 else vals.min()
        clipped = vals[(vals >= clip_lo) & (vals <= clip_hi)]
        sns.histplot(clipped, bins=40, kde=True, ax=ax, color=palette[i], edgecolor="white")
        q50 = np.median(clipped)
        ax.axvline(q50, color="#e74c3c", ls="--", lw=1.5, label=f"Median: {q50:.3f}")
        ax.set_title(titles.get(comp, comp), fontsize=10)
        ax.set_xlabel("")
        ax.legend(fontsize=7)

    for j in range(i + 1, len(axes_flat)):
        axes_flat[j].set_visible(False)

    fig.suptitle("Composite Scorer — Component Distributions", fontsize=13, y=1.01)
    fig.tight_layout()
    return _save_fig(fig, plots_dir, "10_composite_components")


# ── markdown generation ─────────────────────────────────────────────────────

def generate_report(
    output_base: Path,
    file_infos: List[Dict[str, Any]],
    summary_info: Dict[str, Any],
    plot_paths: Dict[str, Any],
    data_dir: Optional[Path] = None,
) -> str:
    lines: List[str] = []
    w = lines.append

    w("# Data Verification Report")
    w("")
    w(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    w(f"**Output directory:** `{output_base}`")
    w("")
    w("This report provides a comprehensive post-processing verification of the signal processing pipeline output. "
       "It covers data completeness, signal quality assessment, RR-interval extraction, and per-patient breakdowns "
       "to help identify issues before downstream analysis.")
    w("")

    # ── 1. Overview ──────────────────────────────────────────────────────
    w("## 1. Overview")
    w("")
    total_size = _dir_size(output_base)
    valid = [f for f in file_infos if f.get("sqi_error") is None]
    sig_counts = Counter(f.get("signal_type", "N/A") for f in valid)
    patients = sorted(set(_extract_patient_id(f["path"]) for f in valid))
    durations_all = [f["total_duration_s"] for f in valid if f.get("total_duration_s")]

    w("The table below summarises the pipeline output at a glance. Each raw recording file (PPG or ECG) "
       "produces one output folder containing SQI metrics, segmented waveforms, and RR intervals.")
    w("")

    w("| Metric | Value |")
    w("|--------|-------|")
    w(f"| Total file outputs | {len(file_infos)} |")
    w(f"| Files with valid SQI | {len(valid)} |")
    for sig_t in sorted(sig_counts):
        w(f"| &nbsp;&nbsp;{sig_t} files | {sig_counts[sig_t]} |")
    w(f"| Patients | {len(patients)} |")
    if durations_all:
        w(f"| Total recording time | {sum(durations_all) / 3600:.1f} hours |")
    w(f"| Output directory size | {_sizeof_fmt(total_size)} |")
    w("")

    if plot_paths.get("overview"):
        _embed_plots(w, plot_paths["overview"], "Processing Overview")
        w("**How to read these charts:**")
        w("")
        ecg_n = sig_counts.get("ECG", 0)
        ppg_n = sig_counts.get("PPG", 0)
        w(f"- **Files by Signal Type (summary):** The dataset contains **{ecg_n} ECG** and **{ppg_n} PPG** recordings. "
           "ECG files come from the chest-lead sensor and PPG files from the pulse-oximeter (SmartCare).")
        w(f"- **Files per Patient (detail pages):** Stacked bars show how many ECG (red) and PPG (blue) files "
           "each patient contributed. Uneven bar heights indicate variation in monitoring duration across patients.")
        w(f"- **Recording Hours per Patient (detail pages):** Total recording hours stacked by signal type. "
           "This helps spot patients with unusually short or long monitoring periods that may need investigation.")
        w("")

    # ── 1b. Missing patients ──────────────────────────────────────────────
    if data_dir and data_dir.is_dir():
        import re
        expected_pids = sorted([
            d.name for d in data_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".")
        ])
        # Per-patient signal type counts from output
        patient_signals: Dict[str, Counter] = defaultdict(Counter)
        for f in valid:
            pid = _extract_patient_id(f["path"])
            sig = f.get("signal_type", "N/A")
            patient_signals[pid][sig] += 1

        output_pids = set(patient_signals.keys())
        missing_pids = [p for p in expected_pids if p not in output_pids]

        w(f"### Patient Coverage ({len(output_pids)} of {len(expected_pids)} patients)")
        w("")
        if missing_pids:
            w(f"**{len(missing_pids)} patients** in `data_dir` have no processed output yet:")
            w("")
            # Show as comma list for compactness
            w(", ".join(f"`{p}`" for p in missing_pids))
            w("")
        else:
            w("All patients in `data_dir` have processed output.")
            w("")

        # Per-patient PPG/ECG breakdown table
        w("<details>")
        w("<summary>Per-patient file counts (PPG / ECG)</summary>")
        w("")
        w("| Patient | ECG files | PPG files | Total |")
        w("|---------|----------:|----------:|------:|")
        for pid in expected_pids:
            ecg_c = patient_signals[pid].get("ECG", 0)
            ppg_c = patient_signals[pid].get("PPG", 0)
            total = ecg_c + ppg_c
            marker = " ⚠️" if total == 0 else ""
            w(f"| `{pid}` | {ecg_c} | {ppg_c} | {total}{marker} |")
        w("")
        w("</details>")
        w("")

    # ── 2. Signal & Duration ─────────────────────────────────────────────
    w("## 2. Signal Types & Recording Duration")
    w("")
    w("This section visualises the distribution of signal types (PPG vs ECG) and the per-file recording "
       "durations. Longer recordings yield more segments and more reliable feature extraction; very short "
       "recordings (under 60 seconds) typically produce zero usable segments because they are shorter than "
       "the configured window size.")
    w("")
    if plot_paths.get("signal_duration"):
        _embed_plots(w, plot_paths["signal_duration"], "Signal Types & Duration")
        w("**Interpretation:** The left panel shows the proportional split of PPG vs ECG files. The right panel "
           "is a histogram of recording durations — a cluster near zero indicates many brief connection attempts "
           "or sensor restarts. The bulk of useful recordings typically falls in the multi-hour range.")
        w("")

    # ── 3. Completeness ──────────────────────────────────────────────────
    w("## 3. Completeness Check")
    w("")
    complete = [f for f in file_infos if not f["subdirs_missing"]]
    incomplete = [f for f in file_infos if f["subdirs_missing"]]
    w("Every processed file should produce a folder with four sub-directories: "
       "`segments/` (windowed waveform CSVs), `features/` (extracted HRV features), "
       "`rr_intervals/` (beat-to-beat interval files), and `sqi/` (quality metrics JSON). "
       "Missing sub-directories indicate a processing failure or an incomplete run.")
    w("")
    w(f"- **Complete** (all 4 subdirs present): {len(complete)}")
    w(f"- **Incomplete**: {len(incomplete)}")
    w("")
    if incomplete:
        w("The table below lists files with missing sub-directories. These may need re-processing.")
        w("")
        w("| Path | Missing subdirs |")
        w("|------|----------------|")
        for f in incomplete[:30]:
            w(f"| `{f['path']}` | {', '.join(f['subdirs_missing'])} |")
        if len(incomplete) > 30:
            w(f"| ... | ({len(incomplete) - 30} more) |")
        w("")

    # ── 4. Aggregate Statistics ──────────────────────────────────────────
    w("## 4. Aggregate Statistics")
    w("")
    valid = [f for f in file_infos if f.get("sqi_error") is None]
    total_segments = sum(f.get("total_segments", 0) for f in valid)
    total_normal = sum(f.get("normal_segments", 0) for f in valid)
    total_abnormal = sum(f.get("abnormal_segments", 0) for f in valid)
    total_seg_csvs = sum(f.get("segment_csvs", 0) for f in file_infos)
    total_rr_txts = sum(f.get("rr_txts", 0) for f in file_infos)
    total_rr_intervals = sum(f.get("rr_total_intervals", 0) for f in file_infos)
    total_feat_csvs = sum(f.get("feature_csvs", 0) for f in file_infos)
    durations = [f["total_duration_s"] for f in valid if f.get("total_duration_s")]

    w("A high-level summary of everything produced by the pipeline. "
       "\"Normal\" segments passed the signal quality threshold and are suitable for downstream analysis "
       "(e.g., HRV feature extraction), while \"abnormal\" segments were flagged as noisy or artefact-corrupted.")
    w("")

    w("| Metric | Value |")
    w("|--------|-------|")
    w(f"| Files with valid SQI | {len(valid)} |")
    sig_types = Counter(f.get("signal_type", "N/A") for f in valid)
    w(f"| Signal types | {', '.join(f'{t}: {c}' for t, c in sig_types.most_common())} |")
    w(f"| Total segments (from SQI) | {total_segments:,} |")
    if total_segments:
        w(f"| Normal segments | {total_normal:,} ({total_normal / total_segments * 100:.1f}%) |")
        w(f"| Abnormal segments | {total_abnormal:,} ({total_abnormal / total_segments * 100:.1f}%) |")
    w(f"| Segment CSV files on disk | {total_seg_csvs:,} |")
    w(f"| RR interval .txt files | {total_rr_txts:,} |")
    w(f"| Total RR intervals extracted | {total_rr_intervals:,} |")
    w(f"| Feature CSV files | {total_feat_csvs:,} |")
    if durations:
        w(f"| Recording duration range | {min(durations):.0f}s – {max(durations):.0f}s |")
        w(f"| Total recording time | {sum(durations) / 3600:.1f} hours |")
    w("")
    if total_segments:
        norm_pct = total_normal / total_segments * 100
        if norm_pct >= 90:
            w(f"> **Good:** {norm_pct:.1f}% of segments are classified as normal — the majority of data is usable.")
        elif norm_pct >= 70:
            w(f"> **Acceptable:** {norm_pct:.1f}% of segments are normal. Consider reviewing files with high abnormal rates.")
        else:
            w(f"> **Warning:** Only {norm_pct:.1f}% of segments are normal. Signal quality may need investigation.")
        w("")

    # ── 5. Segment Quality ───────────────────────────────────────────────
    w("## 5. Segment Quality")
    w("")
    w("Each recording is split into fixed-length windows (segments). The signal quality index (SQI) "
       "classifier labels each window as *normal* or *abnormal*. This section shows the distribution "
       "of normal vs abnormal segments across the dataset.")
    w("")
    if plot_paths.get("segment_quality"):
        _embed_plots(w, plot_paths["segment_quality"], "Segment Quality")
        w("**Interpretation:** The summary shows the overall normal vs abnormal split and the per-file normal "
           "ratio distribution. The detail pages break this down per patient, revealing whether quality issues "
           "are concentrated in specific patients (e.g., due to poor sensor contact or excessive motion artefact) "
           "or distributed broadly.")
        w("")

    # ── 6. SQI Distributions ─────────────────────────────────────────────
    w("## 6. SQI Metric Distributions")
    w("")
    w("The pipeline computes multiple Signal Quality Index (SQI) metrics for each window. "
       "These metrics capture different aspects of signal fidelity:")
    w("")
    w("| Metric | What it measures |")
    w("|--------|-----------------|")
    w("| Signal Entropy | Randomness/complexity of the waveform (higher = more noise) |")
    w("| SNR | Signal-to-noise ratio (higher = cleaner signal) |")
    w("| Kurtosis | Peakedness of the amplitude distribution (extreme values = artefacts) |")
    w("| Skewness | Asymmetry of the signal distribution |")
    w("| Zero Crossing | Rate of signal polarity changes (sensitive to baseline wander) |")
    w("| Energy | Total power in the window |")
    w("| Amplitude Variability | Variation in peak-to-trough amplitudes |")
    w("| Baseline Wander | Low-frequency drift in the signal baseline |")
    w("| Peak-to-Peak Amplitude | Maximum excursion within each window |")
    w("| PPG/Respiratory Signal Quality | Domain-specific composite quality scores |")
    w("")
    w("All metrics are z-score normalised. Values near 0 indicate typical quality; extreme positive or "
       "negative values indicate outlier windows. Plots below clip extreme outliers "
       "(beyond Q25 − 3×IQR or Q75 + 3×IQR) to keep the main distribution visible.")
    w("")
    w("> **Signal-type grouping:** Every plot in sections 6.1–6.4 is generated three times: "
       "once for **all signals combined**, once for **PPG only**, and once for **ECG only**. "
       "This lets you compare whether quality patterns differ between signal types.")
    w("")
    if plot_paths.get("sqi_dist"):
        w("### 6.1 Histograms with KDE")
        w("")
        _embed_plots(w, plot_paths["sqi_dist"], "SQI Distributions")
        w("**How to read:** For each signal group, the first figure shows overall distributions. "
           "The second overlays **normal** (green) and **abnormal** (red) windows, making it easy "
           "to spot which metrics separate good from bad segments.")
        w("")
    if plot_paths.get("sqi_box"):
        w("### 6.2 Box Plot Comparison")
        w("")
        _embed_plots(w, plot_paths["sqi_box"], "SQI Box Plots")
        w("**How to read:** The overall box plot shows spread per metric. The side-by-side plot "
           "compares normal (green) vs abnormal (red). Compare PPG and ECG to see whether "
           "the same metrics are discriminative for both signal types.")
        w("")
    if plot_paths.get("sqi_effect"):
        w("### 6.3 Normal vs Abnormal — Detailed Comparison")
        w("")
        _embed_plots(w, plot_paths["sqi_effect"], "SQI Normal vs Abnormal")
        w("**How to read these three plots (shown per signal group):**")
        w("")
        w("- **Split violin:** Green (normal) and red (abnormal) half-violins. Differences in "
           "shape or center indicate discriminative metrics.")
        w("- **Effect size (Cohen's d):** Horizontal bar chart ranking metrics by discriminative "
           "power. Dotted lines at 0.2 / 0.5 / 0.8 mark small / medium / large effects. "
           "Red = abnormal higher, blue = abnormal lower.")
        w("- **Median comparison (dot plot):** Green circles (normal) and red diamonds (abnormal) "
           "connected by lines. Longer lines = bigger difference.")
        w("")
        w("Comparing the PPG and ECG effect-size plots reveals which quality metrics matter most "
           "for each modality.")
        w("")
    if plot_paths.get("patient_heatmap"):
        w("### 6.4 Per-Patient SQI Heatmap")
        w("")
        _embed_plots(w, plot_paths["patient_heatmap"], "Patient SQI Heatmap")
        w("**How to read:** Three heatmap variants per signal group: (1) **all windows**, "
           "(2) **normal-only**, and (3) **difference** (abnormal − normal, blue-white-red scale). "
           "The difference heatmap directly highlights which metrics shift most per patient. "
           "Separate PPG/ECG heatmaps let you spot modality-specific outlier patients.")
        w("")

    # ── 7. Composite SQI Scoring ────────────────────────────────────────
    has_composite = any(f.get("composite_scores") for f in file_infos)
    if has_composite:
        w("## 7. Composite SQI Scoring")
        w("")
        w("Instead of applying simple per-metric thresholds, the **composite scoring** method combines "
           "multiple statistical features into a single quality score per window. This approach is more "
           "robust because a window must fail on several dimensions simultaneously to be flagged as abnormal. "
           "The five statistical components are:")
        w("")
        w("1. **Quantile Rank** — Where the SQI value falls in its global distribution (low percentile = poor).")
        w("2. **Modified Z-Score** — How far the value deviates from the median in MAD units (high = outlier).")
        w("3. **Tail Probability** — Fraction of the distribution more extreme than this value.")
        w("4. **Trapezoidal Integration Ratio** — Cumulative area under the sorted SQI curve (low = concentrated outlier).")
        w("5. **Rolling Variance** — Local variability around each window (high = unstable signal).")
        w("")
        w("Each component produces a pass/fail flag (1 or 0), and the final composite score is a weighted average. "
           "Windows scoring below the threshold are classified as abnormal.")
        w("")

        all_cs = []
        all_cq = []
        for f in file_infos:
            all_cs.extend(f.get("composite_scores", []))
            all_cq.extend(f.get("composite_quality", []))
        cq_counter = Counter(all_cq)
        cs_arr = [s for s in all_cs if np.isfinite(s)]
        comp_threshold = None
        for f in file_infos:
            t = f.get("composite_threshold")
            if t is not None:
                comp_threshold = t
                break

        w("| Metric | Value |")
        w("|--------|-------|")
        w(f"| Threshold method | composite |")
        w(f"| Total windows scored | {len(all_cs):,} |")
        w(f"| Normal windows | {cq_counter.get('normal', 0):,} |")
        w(f"| Abnormal windows | {cq_counter.get('abnormal', 0):,} |")
        if cs_arr:
            w(f"| Score range | {min(cs_arr):.4f} – {max(cs_arr):.4f} |")
            w(f"| Score median | {np.median(cs_arr):.4f} |")
            w(f"| Score mean ± std | {np.mean(cs_arr):.4f} ± {np.std(cs_arr):.4f} |")
        if comp_threshold is not None:
            w(f"| Score threshold | {comp_threshold} |")
        w("")

        if plot_paths.get("composite_scores"):
            w(f"![Composite Scores]({plot_paths['composite_scores']})")
            w("")
            w("**Interpretation:** The histogram shows the distribution of composite scores. "
               "The vertical dashed line marks the threshold — everything to the left is classified as abnormal. "
               "A sharp peak well above the threshold indicates most data is high quality. A long left tail "
               "or bimodal distribution suggests a distinct subset of poor-quality recordings.")
            w("")
        if plot_paths.get("composite_components"):
            w(f"![Composite Components]({plot_paths['composite_components']})")
            w("")
            w("**Interpretation:** These histograms show the raw values for each of the five statistical "
               "components that feed into the composite score. Components with distributions clustered at "
               "high values contribute positively to overall quality. Components with broad or bimodal "
               "distributions are the most discriminative for separating good from poor segments.")
            w("")
    else:
        w("## 7. Composite SQI Scoring")
        w("")
        w("*Composite scoring not available in current output (threshold_method may be `value`). "
           "To enable it, set `threshold_method: composite` in `config.yaml`.*")
        w("")

    # ── 8. RR Interval Statistics ────────────────────────────────────────
    w("## 8. RR Interval Statistics")
    w("")
    w("RR intervals are the time (in milliseconds) between consecutive heartbeat peaks. They are the "
       "foundation for Heart Rate Variability (HRV) analysis. For a healthy resting adult, typical mean "
       "RR is 600–1200 ms (corresponding to 50–100 bpm). Segments with very high or very low mean RR "
       "may indicate arrhythmia, motion artefact, or missed/extra peak detections.")
    w("")
    if plot_paths.get("rr_stats"):
        _embed_plots(w, plot_paths["rr_stats"], "RR Statistics")
        w("**How to read these plots (shown for All Signals, PPG, and ECG separately):**")
        w("")
        w("- **Overall plots:** Mean RR distribution, variability (Std), and scatter.")
        w("- **Normal vs Abnormal overlay:** Compares RR characteristics between normal (green) "
           "and abnormal (red) quality files. PPG and ECG are shown separately so you can see if "
           "abnormal-quality segments have different heart rate patterns for each modality.")
        w("- **Scatter:** Normal (green dots) vs abnormal (red crosses). Points far from the "
           "normal cluster indicate genuine quality issues.")
        w("")

    # ── 9. Disk Usage ───────────────────────────────────────────────────
    w("## 9. Disk Usage")
    w("")
    cat_sizes = defaultdict(int)
    for f in file_infos:
        cat_sizes["segments"] += f.get("segments_size", 0)
        cat_sizes["rr_intervals"] += f.get("rr_size", 0)
        cat_sizes["features"] += f.get("features_size", 0)
        cat_sizes["sqi"] += f.get("sqi_size", 0)
    w("Disk usage broken down by output category. Segments (raw waveform CSVs) typically dominate "
       "storage because they contain the full signal data for each window. RR intervals and SQI metadata "
       "are comparatively small.")
    w("")
    w("| Category | Size |")
    w("|----------|------|")
    for cat in ("segments", "rr_intervals", "sqi", "features"):
        w(f"| {cat} | {_sizeof_fmt(cat_sizes[cat])} |")
    w(f"| **Total** | **{_sizeof_fmt(sum(cat_sizes.values()))}** |")
    w("")
    if plot_paths.get("disk"):
        _embed_plots(w, plot_paths["disk"], "Disk Usage")
        w("**Interpretation:** The pie chart shows proportional storage by category. The per-patient "
           "detail pages show how disk usage is distributed across patients — patients with more or "
           "longer recordings naturally consume more space. If segments consume >95% of disk, consider "
           "whether all segment CSVs are needed for downstream work, or whether only features and "
           "RR intervals suffice.")
        w("")

    # ── 10. Data Quality Flags ───────────────────────────────────────────
    w("## 10. Data Quality Flags")
    w("")
    w("Automated quality checks that flag potential issues requiring manual review. "
       "These are heuristic warnings — not all flags necessarily indicate a real problem, "
       "but they highlight files that deviate from expected patterns.")
    w("")
    empty_sqi = [f for f in file_infos if not f.get("sqi_json_exists")]
    empty_rr = [f for f in file_infos if not f.get("rr_json_exists")]
    no_segments = [f for f in file_infos if f.get("segment_csvs", 0) == 0]
    all_abnormal = [f for f in valid if f.get("normal_segments", 0) == 0 and f.get("total_segments", 0) > 0]
    short = [f for f in valid if 0 < (f.get("total_duration_s") or 0) < 60]

    flags = [
        ("Missing sqi.json", len(empty_sqi),
         "SQI file absent — the pipeline likely crashed or was interrupted during processing"),
        ("Missing rr.json", len(empty_rr),
         "RR interval JSON absent — peak detection may have failed (no peaks found in any segment)"),
        ("Zero segment CSVs on disk", len(no_segments),
         "Output directory exists but contains no segment files — recording was too short to fill one window"),
        ("All segments abnormal", len(all_abnormal),
         "Every window in this file was classified as abnormal — may indicate persistent noise, "
         "sensor disconnection, or an overly strict quality threshold"),
        ("Very short recording (<60s)", len(short),
         "Recording shorter than the segment window size — no segments can be extracted"),
    ]
    w("| Flag | Count | Meaning |")
    w("|------|------:|---------|")
    for label, cnt, meaning in flags:
        w(f"| {label} | {'**' + str(cnt) + '**' if cnt else '0'} | {meaning} |")
    w("")
    if all_abnormal:
        w("### Files with all abnormal segments")
        w("")
        w("These files had segments extracted but every single one was flagged as abnormal. "
           "This may indicate sensor issues during the entire recording. Consider reviewing the "
           "raw signal to determine whether the data is salvageable or should be excluded:")
        w("")
        for f in all_abnormal[:20]:
            w(f"- `{f['path']}`")
        if len(all_abnormal) > 20:
            w(f"- ... ({len(all_abnormal) - 20} more)")
        w("")

    # ── 11. Per-file breakdown ───────────────────────────────────────────
    w("## 11. Per-File Breakdown")
    w("")
    w("Detailed per-file inventory of all pipeline outputs. Each row corresponds to one raw input file.")
    w("")
    w("**Column guide:**")
    w("")
    w("| Column | Description |")
    w("|--------|-------------|")
    w("| **Path** | Relative path within the output directory (patient / date / type / file) |")
    w("| **Signal** | Detected signal type — PPG (photoplethysmography) or ECG (electrocardiogram) |")
    w("| **Duration** | Total recording length in seconds |")
    w("| **Segments (N/A)** | Count of normal / abnormal segments as determined by the SQI classifier |")
    w("| **Seg CSVs** | Number of segment CSV files written to disk |")
    w("| **RR txts** | Number of RR-interval text files (one per segment) |")
    w("| **RR JSON** | Whether the consolidated `rr.json` summary exists |")
    w("| **Feat CSVs** | Number of HRV feature CSV files |")
    w("| **SQI JSON** | Whether the `sqi.json` quality report exists |")
    w("| **Issues** | Any anomalies detected for this file |")
    w("")
    w("<details>")
    w("<summary>Click to expand full table</summary>")
    w("")
    w("| # | Path | Signal | Duration (s) | Segments (N/A) | Seg CSVs | RR txts | RR JSON | Feat CSVs | SQI JSON | Issues |")
    w("|--:|------|--------|-------------:|---------------:|---------:|--------:|--------:|----------:|---------:|--------|")

    for i, f in enumerate(file_infos, 1):
        sig = f.get("signal_type", "?")
        dur = f"{f['total_duration_s']:.0f}" if f.get("total_duration_s") else ""
        seg_str = f"{f.get('normal_segments', '?')}/{f.get('abnormal_segments', '?')}" if f.get("sqi_error") is None else "err"
        rr_ok = "yes" if f.get("rr_json_exists") else "**NO**"
        sqi_ok = "yes" if f.get("sqi_json_exists") else "**NO**"

        issues = []
        if f["subdirs_missing"]:
            issues.append(f"missing: {','.join(f['subdirs_missing'])}")
        if f.get("sqi_error"):
            issues.append("sqi unreadable")
        if f.get("sqi_json_exists") and f.get("segment_csvs", 0) == 0 and f.get("normal_segments", 0) > 0:
            issues.append("segments on disk=0 but SQI says normal>0")
        if not f.get("rr_json_exists"):
            issues.append("rr.json missing")
        issue_str = "; ".join(issues) if issues else "-"

        w(f"| {i} | `{f['path']}` | {sig} | {dur} | {seg_str} | {f.get('segment_csvs', 0)} | {f.get('rr_txts', 0)} | {rr_ok} | {f.get('feature_csvs', 0)} | {sqi_ok} | {issue_str} |")

    w("")
    w("</details>")
    w("")
    w("---")
    w(f"*Report generated by `scripts/generate_verification_report.py`*")
    w("")
    return "\n".join(lines)


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate output verification report")
    parser.add_argument("--output-dir", type=str, default=None)
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("--report-path", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent

    if args.output_dir:
        output_base = Path(args.output_dir)
    else:
        config_path = Path(args.config) if args.config else project_root / "config.yaml"
        try:
            import yaml
            with open(config_path) as f:
                cfg = yaml.safe_load(f) or {}
            raw = cfg.get("output_dir", "output")
            p = Path(raw)
            output_base = p if p.is_absolute() else project_root / p
        except Exception:
            output_base = project_root / "output"

    if not output_base.is_dir():
        print(f"ERROR: Output directory does not exist: {output_base}", file=sys.stderr)
        sys.exit(1)

    # Resolve data_dir to identify expected patients
    data_dir = None
    config_path = Path(args.config) if args.config else project_root / "config.yaml"
    try:
        import yaml
        with open(config_path) as f:
            cfg_all = yaml.safe_load(f) or {}
        raw_dd = cfg_all.get("data_dir", "")
        if raw_dd:
            dd = Path(raw_dd)
            data_dir = dd if dd.is_absolute() else project_root / dd
    except Exception:
        pass

    report_path = Path(args.report_path) if args.report_path else output_base / "verification_report.md"
    plots_dir = output_base / PLOTS_SUBDIR
    plots_dir.mkdir(parents=True, exist_ok=True)

    print(f"Scanning output directory: {output_base}")
    file_dirs = find_file_output_dirs(output_base)
    print(f"Found {len(file_dirs)} per-file output directories")

    print("Analysing each file output ...")
    file_infos = [analyse_file_output(d, output_base) for d in file_dirs]

    print("Reading sqi_summary.json ...")
    summary_info = analyse_summary(output_base)

    print("Generating plots ...")
    plot_paths: Dict[str, Any] = {}
    plot_paths["overview"] = plot_processing_overview(file_infos, plots_dir)
    plot_paths["signal_duration"] = plot_signal_type_and_duration(file_infos, plots_dir)
    plot_paths["segment_quality"] = plot_segment_quality(file_infos, plots_dir)
    plot_paths["sqi_dist"] = plot_sqi_distributions(file_infos, plots_dir)
    plot_paths["sqi_box"] = plot_sqi_boxplots(file_infos, plots_dir)
    plot_paths["sqi_effect"] = plot_sqi_effect_size(file_infos, plots_dir)
    plot_paths["rr_stats"] = plot_rr_statistics(file_infos, plots_dir)
    plot_paths["disk"] = plot_disk_usage(file_infos, plots_dir)
    plot_paths["patient_heatmap"] = plot_per_patient_quality_heatmap(file_infos, plots_dir)
    plot_paths["composite_scores"] = plot_composite_scores(file_infos, plots_dir)
    plot_paths["composite_components"] = plot_composite_components(file_infos, plots_dir)
    n_plots = sum(len(v) if isinstance(v, list) else (1 if v else 0)
                  for v in plot_paths.values())
    print(f"  Saved {n_plots} plot(s) to {plots_dir}")

    print("Generating markdown report ...")
    report = generate_report(output_base, file_infos, summary_info, plot_paths,
                             data_dir=data_dir)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    print(f"Report written to: {report_path}")


if __name__ == "__main__":
    main()
