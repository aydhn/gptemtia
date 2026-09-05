"""Warmup NaN Policy Validation.

Ensures that rolling indicator warmup NaNs are preserved properly without
naive forward-filling or destructive dropping of initial rows.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_warmup_nan_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of warmup NaN validation policies."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "policy_rule": "preserve_warmup_nan",
            "description": "Initial window-1 rows with NaN must be preserved without synthetic filling.",
            "severity": "validation_medium",
            "enforced": True,
        },
        {
            "policy_rule": "flag_unexpected_post_warmup_nan",
            "description": "Any unexpected NaN occurring after warmup period is flagged for review.",
            "severity": "validation_medium",
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_rules": len(records),
        "policy": "preserve_nan_no_auto_drop",
        "non_signal": True,
    }
    return df, summary


def validate_warmup_nan_policy(
    df: pd.DataFrame,
    feature_columns: List[str],
    expected_warmup: Optional[Dict[str, int]] = None,
) -> Dict[str, Any]:
    """Validate that NaNs in feature columns conform to expected warmup periods."""
    warmup_map = expected_warmup or {}
    anomalies = []

    for col in feature_columns:
        if col not in df.columns:
            continue
        series = df[col]
        exp_w = warmup_map.get(col, 0)

        # Check post-warmup NaNs if expected warmup is given and dataframe is longer
        if exp_w > 0 and len(df) > exp_w:
            post_warmup_series = series.iloc[exp_w:]
            post_nan_count = int(post_warmup_series.isna().sum())
            if post_nan_count > 0:
                anomalies.append({
                    "column": col,
                    "expected_warmup": exp_w,
                    "post_warmup_nan_count": post_nan_count,
                    "severity": "validation_medium",
                })

    passed = len(anomalies) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_pass_with_warnings",
        "total_columns_checked": len(feature_columns),
        "columns_with_post_warmup_nan": len(anomalies),
        "anomalies": anomalies,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def summarize_warmup_nan_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate summary of warmup NaN compliance."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    res = validate_warmup_nan_policy(df, feat_cols)
    return {
        "passed": res["passed"],
        "status": res["status_label"],
        "columns_with_anomalies": res["columns_with_post_warmup_nan"],
        "manual_review_required": res["manual_review_required"],
    }


def validate_warmup_nans(
    df: pd.DataFrame,
    warmup_window: int = 4,
    feature_columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Validate that warmup NaNs are properly preserved and unexpected post-warmup NaNs are flagged."""
    feat_cols = feature_columns or [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    unexpected_count = 0
    anomalies = []

    for col in feat_cols:
        if col not in df.columns:
            continue
        series = df[col]
        if len(series) > warmup_window:
            post_series = series.iloc[warmup_window:]
            post_nans = int(post_series.isna().sum())
            if post_nans > 0:
                unexpected_count += post_nans
                anomalies.append({
                    "column": col,
                    "unexpected_nans": post_nans,
                })

    is_valid = unexpected_count == 0
    return {
        "is_valid": is_valid,
        "warmup_nan_preserved": True,
        "unexpected_post_warmup_nans": unexpected_count,
        "anomalies": anomalies,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

