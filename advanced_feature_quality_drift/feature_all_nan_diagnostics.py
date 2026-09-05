"""Phase 123 Feature All-NaN Diagnostics.

Identifies feature columns whose values are 100% NaN, flagging critical findings
for manual inspection without performing automated column deletion.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def detect_all_nan_features(
    df: pd.DataFrame,
    feature_columns: List[str] | None = None,
) -> pd.DataFrame:
    """Detect columns containing only NaN values without mutating input DataFrame."""
    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "total_rows": 0,
            "all_nan_flag": False,
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
            all_nan = bool(df[col].isna().all())
            if all_nan:
                status = "diagnostic_fail"
                sev = "quality_critical"
                review = True
            else:
                status = "diagnostic_pass"
                sev = "quality_info"
                review = False

            records.append({
                "column": col,
                "total_rows": total_rows,
                "all_nan_flag": all_nan,
                "status": status,
                "severity": sev,
                "manual_review_required": review,
            })
        else:
            records.append({
                "column": col,
                "total_rows": total_rows,
                "all_nan_flag": True,
                "status": "diagnostic_fail",
                "severity": "quality_critical",
                "manual_review_required": True,
            })

    return pd.DataFrame(records)


def summarize_feature_all_nan(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate summary from all-NaN diagnostics DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "all_nan_count": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_features = len(df)
    all_nan_count = int(df["all_nan_flag"].sum()) if "all_nan_flag" in df.columns else 0
    status = "diagnostic_fail" if all_nan_count > 0 else "diagnostic_pass"

    return {
        "total_features": total_features,
        "all_nan_count": all_nan_count,
        "status": status,
        "manual_review_required": all_nan_count > 0,
    }


def build_feature_all_nan_diagnostics_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build all-NaN diagnostics report and summary."""
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

    res_df = detect_all_nan_features(eval_df, eval_cols)
    summary = summarize_feature_all_nan(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
