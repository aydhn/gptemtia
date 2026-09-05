"""Phase 123 Feature Distribution Drift Diagnostics.

Compares empirical distributions of feature columns between a baseline reference window
and current observation window. Strictly non-signal, non-predictive, and research-only.
"""

from typing import Any, Dict, List, Tuple
import numpy as np
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)
from advanced_feature_quality_drift.feature_drift_thresholds import DEFAULT_DRIFT_THRESHOLDS


def compare_feature_distribution_baseline(
    current_df: pd.DataFrame,
    baseline_df: pd.DataFrame,
    feature_columns: List[str] | None = None,
) -> pd.DataFrame:
    """Compare distributions between baseline and current dataframes without mutating inputs."""
    mean_warn = DEFAULT_DRIFT_THRESHOLDS["distribution_mean_shift"]["warning"]
    mean_crit = DEFAULT_DRIFT_THRESHOLDS["distribution_mean_shift"]["critical"]
    std_warn = DEFAULT_DRIFT_THRESHOLDS["distribution_std_shift"]["warning"]
    std_crit = DEFAULT_DRIFT_THRESHOLDS["distribution_std_shift"]["critical"]
    min_obs = int(DEFAULT_DRIFT_THRESHOLDS["min_sample_size"]["warning"])

    if current_df.empty or baseline_df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "baseline_rows": len(baseline_df),
            "current_rows": len(current_df),
            "mean_baseline": 0.0,
            "mean_current": 0.0,
            "mean_abs_delta": 0.0,
            "std_baseline": 0.0,
            "std_current": 0.0,
            "std_abs_delta": 0.0,
            "q25_delta": 0.0,
            "q50_delta": 0.0,
            "q75_delta": 0.0,
            "drift_status": "diagnostic_manual_review_required",
            "severity": "drift_medium",
            "manual_review_required": True,
            "notes": "Insufficient sample rows in baseline or current window",
        } for c in cols])

    cols = feature_columns if feature_columns is not None else [
        c for c in current_df.columns
        if c in baseline_df.columns and c not in ("timestamp", "asset_id", "symbol")
    ]
    records = []

    for col in cols:
        b_series = baseline_df[col].dropna() if col in baseline_df.columns else pd.Series(dtype=float)
        c_series = current_df[col].dropna() if col in current_df.columns else pd.Series(dtype=float)

        b_len = len(b_series)
        c_len = len(c_series)

        if b_len < min_obs or c_len < min_obs:
            records.append({
                "column": col,
                "baseline_rows": b_len,
                "current_rows": c_len,
                "mean_baseline": float(b_series.mean()) if b_len > 0 else 0.0,
                "mean_current": float(c_series.mean()) if c_len > 0 else 0.0,
                "mean_abs_delta": 0.0,
                "std_baseline": float(b_series.std()) if b_len > 1 else 0.0,
                "std_current": float(c_series.std()) if c_len > 1 else 0.0,
                "std_abs_delta": 0.0,
                "q25_delta": 0.0,
                "q50_delta": 0.0,
                "q75_delta": 0.0,
                "drift_status": "diagnostic_manual_review_required",
                "severity": "drift_medium",
                "manual_review_required": True,
                "notes": f"Sample size below minimum threshold ({b_len}/{c_len} < {min_obs})",
            })
            continue

        b_mean = float(b_series.mean())
        c_mean = float(c_series.mean())
        b_std = float(b_series.std()) if b_len > 1 else 1e-6
        c_std = float(c_series.std()) if c_len > 1 else 1e-6

        # Standardized mean difference
        pooled_std = max(1e-6, np.sqrt((b_std ** 2 + c_std ** 2) / 2.0))
        mean_abs_delta = abs(c_mean - b_mean) / pooled_std

        # Relative standard deviation change
        std_abs_delta = abs(c_std - b_std) / max(1e-6, b_std)

        # Quantile shifts
        q25_delta = abs(float(c_series.quantile(0.25)) - float(b_series.quantile(0.25))) / pooled_std
        q50_delta = abs(float(c_series.median()) - float(b_series.median())) / pooled_std
        q75_delta = abs(float(c_series.quantile(0.75)) - float(b_series.quantile(0.75))) / pooled_std

        if mean_abs_delta >= mean_crit or std_abs_delta >= std_crit:
            drift_status = "diagnostic_fail"
            sev = "drift_critical"
            review = True
            notes = "Critical distribution shift detected"
        elif mean_abs_delta >= mean_warn or std_abs_delta >= std_warn:
            drift_status = "diagnostic_pass_with_warnings"
            sev = "drift_medium"
            review = True
            notes = "Moderate distribution drift detected"
        else:
            drift_status = "diagnostic_pass"
            sev = "drift_low"
            review = False
            notes = "Distribution aligned with baseline"

        records.append({
            "column": col,
            "baseline_rows": b_len,
            "current_rows": c_len,
            "mean_baseline": round(b_mean, 4),
            "mean_current": round(c_mean, 4),
            "mean_abs_delta": round(mean_abs_delta, 4),
            "std_baseline": round(b_std, 4),
            "std_current": round(c_std, 4),
            "std_abs_delta": round(std_abs_delta, 4),
            "q25_delta": round(q25_delta, 4),
            "q50_delta": round(q50_delta, 4),
            "q75_delta": round(q75_delta, 4),
            "drift_status": drift_status,
            "severity": sev,
            "manual_review_required": review,
            "notes": notes,
        })

    return pd.DataFrame(records)


def summarize_feature_distribution_drift(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from distribution drift DataFrame."""
    if df.empty:
        return {
            "total_features_compared": 0,
            "critical_drift_count": 0,
            "warning_drift_count": 0,
            "stable_features_count": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_compared = len(df)
    crit_count = int((df["severity"] == "drift_critical").sum())
    warn_count = int((df["severity"] == "drift_medium").sum())
    stable_count = total_compared - crit_count - warn_count

    if crit_count > 0:
        overall_status = "diagnostic_fail"
    elif warn_count > 0:
        overall_status = "diagnostic_pass_with_warnings"
    else:
        overall_status = "diagnostic_pass"

    return {
        "total_features_compared": total_compared,
        "critical_drift_count": crit_count,
        "warning_drift_count": warn_count,
        "stable_features_count": stable_count,
        "status": overall_status,
        "manual_review_required": (crit_count + warn_count) > 0,
    }


def build_feature_distribution_drift_report(
    profile: FeatureQualityDriftProfile | None = None,
    current_df: pd.DataFrame | None = None,
    baseline_df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build feature distribution drift report and summary."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    if current_df is None or baseline_df is None:
        np.random.seed(42)
        n_b = 100
        n_c = 100
        cols = feature_columns or [
            "feat_rsi_14", "feat_macd_line", "feat_bb_upper_20",
            "feat_atr_14", "feat_volatility_parkinson_20"
        ]
        b_data = {c: np.random.randn(n_b) for c in cols}
        c_data = {c: np.random.randn(n_c) + (0.1 if c == "feat_rsi_14" else 0.0) for c in cols}
        eval_base = pd.DataFrame(b_data)
        eval_curr = pd.DataFrame(c_data)
        eval_cols = cols
    else:
        eval_base = baseline_df
        eval_curr = current_df
        eval_cols = feature_columns

    res_df = compare_feature_distribution_baseline(eval_curr, eval_base, eval_cols)
    summary = summarize_feature_distribution_drift(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
