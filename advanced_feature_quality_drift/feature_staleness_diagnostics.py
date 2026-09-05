"""Phase 123 Feature Staleness Diagnostics.

Identifies features that fail to update or remain frozen across consecutive observations,
revealing pipeline ingestion stalls or lagged feeds.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)
from advanced_feature_quality_drift.feature_quality_thresholds import DEFAULT_QUALITY_THRESHOLDS


def detect_stale_features(
    df: pd.DataFrame,
    timestamp_field: str = "timestamp",
    feature_columns: List[str] | None = None,
    warning_bars: int | None = None,
    critical_bars: int | None = None,
) -> pd.DataFrame:
    """Detect consecutive identical values in feature series without mutating input DataFrame."""
    warn_b = warning_bars if warning_bars is not None else int(DEFAULT_QUALITY_THRESHOLDS["staleness_max_unchanged_bars"]["warning"])
    crit_b = critical_bars if critical_bars is not None else int(DEFAULT_QUALITY_THRESHOLDS["staleness_max_unchanged_bars"]["critical"])

    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "total_rows": 0,
            "max_consecutive_unchanged": 0,
            "current_tail_unchanged": 0,
            "status": "diagnostic_pass",
            "severity": "quality_info",
            "manual_review_required": False,
        } for c in cols])

    cols = feature_columns if feature_columns is not None else [
        c for c in df.columns if c not in (timestamp_field, "asset_id", "symbol")
    ]
    total_rows = len(df)
    records = []

    for col in cols:
        if col in df.columns:
            s = df[col]
            # calculate consecutive equal runs
            diff = s.ne(s.shift())
            run_lengths = diff.cumsum()
            counts = s.groupby(run_lengths).transform("count")
            max_unchanged = int(counts.max()) if total_rows > 0 else 0

            # tail unchanged
            tail_run_id = run_lengths.iloc[-1] if total_rows > 0 else 0
            tail_unchanged = int((run_lengths == tail_run_id).sum()) if total_rows > 0 else 0

            if max_unchanged >= crit_b:
                status = "diagnostic_fail"
                sev = "quality_critical"
                review = True
            elif max_unchanged >= warn_b:
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
                "max_consecutive_unchanged": max_unchanged,
                "current_tail_unchanged": tail_unchanged,
                "status": status,
                "severity": sev,
                "manual_review_required": review,
            })
        else:
            records.append({
                "column": col,
                "total_rows": total_rows,
                "max_consecutive_unchanged": 0,
                "current_tail_unchanged": 0,
                "status": "diagnostic_pass",
                "severity": "quality_info",
                "manual_review_required": False,
            })

    return pd.DataFrame(records)


def summarize_feature_staleness(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from staleness diagnostics DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "stale_critical_count": 0,
            "stale_warning_count": 0,
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
        "stale_critical_count": crit_count,
        "stale_warning_count": warn_count,
        "clean_features_count": clean_count,
        "status": overall_status,
        "manual_review_required": (crit_count + warn_count) > 0,
    }


def build_feature_staleness_diagnostics_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    timestamp_field: str = "timestamp",
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build feature staleness diagnostics report and summary."""
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
        synth_data[timestamp_field] = pd.date_range("2026-01-01", periods=n_rows, freq="1h")
        eval_df = pd.DataFrame(synth_data)
        eval_cols = cols
    else:
        eval_df = df
        eval_cols = feature_columns

    res_df = detect_stale_features(eval_df, timestamp_field, eval_cols)
    summary = summarize_feature_staleness(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
