"""Phase 123 Feature Infinite Value Diagnostics.

Detects positive and negative infinite values (+/-inf) across numeric feature columns,
flagging critical findings without performing automated substitution or deletion.
"""

from typing import Any, Dict, List, Tuple
import numpy as np
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def detect_infinite_values(
    df: pd.DataFrame,
    feature_columns: List[str] | None = None,
) -> pd.DataFrame:
    """Detect infinite values in feature columns without mutating input DataFrame."""
    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "total_rows": 0,
            "pos_inf_count": 0,
            "neg_inf_count": 0,
            "total_inf_count": 0,
            "inf_ratio": 0.0,
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
            pos_inf = int(np.isposinf(df[col]).sum())
            neg_inf = int(np.isneginf(df[col]).sum())
            tot_inf = pos_inf + neg_inf
            inf_ratio = float(tot_inf / total_rows) if total_rows > 0 else 0.0

            if tot_inf > 0:
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
                "pos_inf_count": pos_inf,
                "neg_inf_count": neg_inf,
                "total_inf_count": tot_inf,
                "inf_ratio": round(inf_ratio, 6),
                "status": status,
                "severity": sev,
                "manual_review_required": review,
            })
        else:
            records.append({
                "column": col,
                "total_rows": total_rows,
                "pos_inf_count": 0,
                "neg_inf_count": 0,
                "total_inf_count": 0,
                "inf_ratio": 0.0,
                "status": "diagnostic_pass",
                "severity": "quality_info",
                "manual_review_required": False,
            })

    return pd.DataFrame(records)


def summarize_feature_infinite_value(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from infinite value diagnostics DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "features_with_inf": 0,
            "total_inf_values": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_features = len(df)
    inf_features = int((df["total_inf_count"] > 0).sum())
    total_inf = int(df["total_inf_count"].sum())

    status = "diagnostic_fail" if inf_features > 0 else "diagnostic_pass"

    return {
        "total_features": total_features,
        "features_with_inf": inf_features,
        "total_inf_values": total_inf,
        "status": status,
        "manual_review_required": inf_features > 0,
    }


def build_feature_infinite_value_diagnostics_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build infinite value diagnostics report and summary."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    if df is None:
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

    res_df = detect_infinite_values(eval_df, eval_cols)
    summary = summarize_feature_infinite_value(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
