"""Phase 123 Feature Duplicate Value Diagnostics.

Detects feature columns with overwhelmingly repetitive values (excessive duplicate ratio),
indicating potential discrete clipping or degenerate calculation, without performing automated removal.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)
from advanced_feature_quality_drift.feature_quality_thresholds import DEFAULT_QUALITY_THRESHOLDS


def detect_duplicate_value_features(
    df: pd.DataFrame,
    feature_columns: List[str] | None = None,
    warning_threshold: float | None = None,
    critical_threshold: float | None = None,
) -> pd.DataFrame:
    """Detect columns dominated by duplicate/repeated values without mutating input DataFrame."""
    warn_t = warning_threshold if warning_threshold is not None else DEFAULT_QUALITY_THRESHOLDS["duplicate_value_ratio"]["warning"]
    crit_t = critical_threshold if critical_threshold is not None else DEFAULT_QUALITY_THRESHOLDS["duplicate_value_ratio"]["critical"]

    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "total_rows": 0,
            "unique_values_count": 0,
            "modal_duplicate_count": 0,
            "duplicate_ratio": 0.0,
            "status": "diagnostic_pass",
            "severity": "quality_info",
            "manual_review_required": False,
        } for c in cols])

    cols = feature_columns if feature_columns is not None else [
        c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")
    ]
    total_rows = len(df)
    records = []

    for col in cols:
        if col in df.columns:
            valid_vals = df[col].dropna()
            n_valid = len(valid_vals)
            if n_valid > 0:
                val_counts = valid_vals.value_counts()
                modal_count = int(val_counts.iloc[0])
                n_unique = len(val_counts)
                dup_ratio = float(modal_count / n_valid)
            else:
                modal_count = 0
                n_unique = 0
                dup_ratio = 0.0

            if dup_ratio >= crit_t:
                status = "diagnostic_fail"
                sev = "quality_critical"
                review = True
            elif dup_ratio >= warn_t:
                status = "diagnostic_pass_with_warnings"
                sev = "quality_medium"
                review = True
            else:
                status = "diagnostic_pass"
                sev = "quality_info"
                review = False

            records.append({
                "column": col,
                "total_rows": total_rows,
                "unique_values_count": n_unique,
                "modal_duplicate_count": modal_count,
                "duplicate_ratio": round(dup_ratio, 4),
                "status": status,
                "severity": sev,
                "manual_review_required": review,
            })
        else:
            records.append({
                "column": col,
                "total_rows": total_rows,
                "unique_values_count": 0,
                "modal_duplicate_count": 0,
                "duplicate_ratio": 0.0,
                "status": "diagnostic_pass",
                "severity": "quality_info",
                "manual_review_required": False,
            })

    return pd.DataFrame(records)


def summarize_feature_duplicate_value(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from duplicate value diagnostics DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "critical_duplicates_count": 0,
            "warning_duplicates_count": 0,
            "clean_features_count": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_features = len(df)
    crit_count = int((df["severity"] == "quality_critical").sum())
    warn_count = int((df["severity"] == "quality_medium").sum())
    clean_count = total_features - crit_count - warn_count

    if crit_count > 0:
        overall_status = "diagnostic_fail"
    elif warn_count > 0:
        overall_status = "diagnostic_pass_with_warnings"
    else:
        overall_status = "diagnostic_pass"

    return {
        "total_features": total_features,
        "critical_duplicates_count": crit_count,
        "warning_duplicates_count": warn_count,
        "clean_features_count": clean_count,
        "status": overall_status,
        "manual_review_required": (crit_count + warn_count) > 0,
    }


def build_feature_duplicate_value_diagnostics_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build duplicate value diagnostics report and summary."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    if df is None:
        import numpy as np
        np.random.seed(42)
        n_rows = 100
        cols = feature_columns or [
            "feat_rsi_14", "feat_macd_line", "feat_bb_upper_20",
            "feat_atr_14", "feat_volatility_parkinson_20"
        ]
        synth_data = {c: np.random.randn(n_rows) for c in cols}
        eval_df = pd.DataFrame(synth_data)
        eval_cols = cols
    else:
        eval_df = df
        eval_cols = feature_columns

    res_df = detect_duplicate_value_features(eval_df, eval_cols)
    summary = summarize_feature_duplicate_value(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
