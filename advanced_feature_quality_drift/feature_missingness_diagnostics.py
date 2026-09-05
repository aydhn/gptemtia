"""Phase 123 Feature Missingness Diagnostics.

Calculates missingness ratios across feature columns, detects threshold breaches,
and logs findings into manual review queue without performing automated deletion or imputation.
"""

from typing import Any, Dict, List, Tuple
import numpy as np
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)
from advanced_feature_quality_drift.feature_quality_thresholds import DEFAULT_QUALITY_THRESHOLDS


def calculate_missingness(
    df: pd.DataFrame,
    feature_columns: List[str] | None = None,
    warning_threshold: float | None = None,
    critical_threshold: float | None = None,
) -> pd.DataFrame:
    """Calculate missingness metrics for feature columns without mutating input DataFrame."""
    warn_t = warning_threshold if warning_threshold is not None else DEFAULT_QUALITY_THRESHOLDS["missingness_ratio"]["warning"]
    crit_t = critical_threshold if critical_threshold is not None else DEFAULT_QUALITY_THRESHOLDS["missingness_ratio"]["critical"]

    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "total_rows": 0,
            "missing_count": 0,
            "missing_ratio": 0.0,
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
            missing_count = int(df[col].isna().sum())
            missing_ratio = float(missing_count / total_rows) if total_rows > 0 else 0.0

            if missing_ratio >= crit_t:
                status = "diagnostic_fail"
                sev = "quality_critical"
                review = True
            elif missing_ratio >= warn_t:
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
                "missing_count": missing_count,
                "missing_ratio": round(missing_ratio, 4),
                "status": status,
                "severity": sev,
                "manual_review_required": review,
            })
        else:
            records.append({
                "column": col,
                "total_rows": total_rows,
                "missing_count": total_rows,
                "missing_ratio": 1.0,
                "status": "diagnostic_fail",
                "severity": "quality_critical",
                "manual_review_required": True,
            })

    return pd.DataFrame(records)


def summarize_feature_missingness(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from missingness diagnostics DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "critical_missingness_count": 0,
            "warning_missingness_count": 0,
            "clean_features_count": 0,
            "max_missingness_ratio": 0.0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_features = len(df)
    crit_count = int((df["severity"] == "quality_critical").sum())
    warn_count = int((df["severity"] == "quality_medium").sum())
    clean_count = total_features - crit_count - warn_count
    max_ratio = float(df["missing_ratio"].max()) if "missing_ratio" in df.columns else 0.0

    if crit_count > 0:
        overall_status = "diagnostic_fail"
    elif warn_count > 0:
        overall_status = "diagnostic_pass_with_warnings"
    else:
        overall_status = "diagnostic_pass"

    return {
        "total_features": total_features,
        "critical_missingness_count": crit_count,
        "warning_missingness_count": warn_count,
        "clean_features_count": clean_count,
        "max_missingness_ratio": round(max_ratio, 4),
        "status": overall_status,
        "manual_review_required": (crit_count + warn_count) > 0,
    }


def build_feature_missingness_diagnostics_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build missingness diagnostics DataFrame and metadata summary."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    if df is None:
        # Generate representative reference dataset for offline dry run diagnostics
        np.random.seed(42)
        n_rows = 100
        cols = feature_columns or [
            "feat_rsi_14", "feat_macd_line", "feat_bb_upper_20",
            "feat_atr_14", "feat_volatility_parkinson_20", "feat_macro_cpi_surprise"
        ]
        synth_data = {}
        for c in cols:
            arr = np.random.randn(n_rows)
            # Introduce controlled missingness for diagnostics demonstration
            if c == "feat_macro_cpi_surprise":
                arr[:10] = np.nan
            synth_data[c] = arr
        eval_df = pd.DataFrame(synth_data)
        eval_cols = cols
    else:
        eval_df = df
        eval_cols = feature_columns

    res_df = calculate_missingness(eval_df, eval_cols)
    summary = summarize_feature_missingness(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
