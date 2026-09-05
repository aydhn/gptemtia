"""Phase 123 Feature Zero Variance Diagnostics.

Identifies constant or near-zero variance features whose lack of variation indicates
broken upstream computation or stalled values, without performing automated dropping.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def detect_zero_variance_features(
    df: pd.DataFrame,
    feature_columns: List[str] | None = None,
    variance_threshold: float = 1e-12,
) -> pd.DataFrame:
    """Detect features with zero or near-zero variance without mutating input DataFrame."""
    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "total_rows": 0,
            "variance": 0.0,
            "std_dev": 0.0,
            "zero_variance_flag": False,
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
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            valid_vals = df[col].dropna()
            if len(valid_vals) > 1:
                var = float(valid_vals.var())
                std = float(valid_vals.std())
                is_zero = bool(var <= variance_threshold)
            elif len(valid_vals) == 1:
                var = 0.0
                std = 0.0
                is_zero = True
            else:
                var = 0.0
                std = 0.0
                is_zero = True

            if is_zero:
                status = "diagnostic_fail"
                sev = "quality_high"
                review = True
            else:
                status = "diagnostic_pass"
                sev = "quality_info"
                review = False

            records.append({
                "column": col,
                "total_rows": total_rows,
                "variance": round(var, 8),
                "std_dev": round(std, 8),
                "zero_variance_flag": is_zero,
                "status": status,
                "severity": sev,
                "manual_review_required": review,
            })
        else:
            records.append({
                "column": col,
                "total_rows": total_rows,
                "variance": 0.0,
                "std_dev": 0.0,
                "zero_variance_flag": False,
                "status": "diagnostic_pass",
                "severity": "quality_info",
                "manual_review_required": False,
            })

    return pd.DataFrame(records)


def summarize_feature_zero_variance(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from zero variance diagnostics DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "zero_variance_count": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_features = len(df)
    zv_count = int(df["zero_variance_flag"].sum()) if "zero_variance_flag" in df.columns else 0
    status = "diagnostic_fail" if zv_count > 0 else "diagnostic_pass"

    return {
        "total_features": total_features,
        "zero_variance_count": zv_count,
        "status": status,
        "manual_review_required": zv_count > 0,
    }


def build_feature_zero_variance_diagnostics_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build zero variance diagnostics report and summary."""
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

    res_df = detect_zero_variance_features(eval_df, eval_cols)
    summary = summarize_feature_zero_variance(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
