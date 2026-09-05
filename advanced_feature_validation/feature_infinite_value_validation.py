"""Feature Infinite Value and Degeneracy Validation.

Detects positive/negative infinite values and all-NaN degenerated feature columns.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import numpy as np
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_feature_infinite_value_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of infinite value rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "check_name": "no_infinite_values",
            "description": "Verifies that feature columns do not contain +inf or -inf.",
            "severity": "validation_high",
            "enforced": True,
        },
        {
            "check_name": "no_all_nan_features",
            "description": "Flags feature columns where 100% of values are NaN (degenerated features).",
            "severity": "validation_high",
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_checks": len(records),
        "auto_replacement_allowed": False,
        "non_signal": True,
    }
    return df, summary


def validate_no_infinite_values(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Detect infinite values across specified feature columns."""
    inf_anomalies = []

    for col in feature_columns:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            s = df[col]
            inf_count = int(np.isinf(s).sum())
            if inf_count > 0:
                inf_anomalies.append({
                    "column": col,
                    "infinite_count": inf_count,
                    "severity": "validation_high",
                })

    passed = len(inf_anomalies) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_columns_checked": len(feature_columns),
        "columns_with_infinite_values": len(inf_anomalies),
        "anomalies": inf_anomalies,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def validate_no_all_nan_features(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Detect completely unpopulated (all-NaN) feature columns."""
    all_nan_cols = []
    total_rows = len(df)

    if total_rows > 0:
        for col in feature_columns:
            if col in df.columns:
                if df[col].isna().sum() == total_rows:
                    all_nan_cols.append({
                        "column": col,
                        "total_rows": total_rows,
                        "severity": "validation_high",
                    })

    passed = len(all_nan_cols) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_columns_checked": len(feature_columns),
        "all_nan_column_count": len(all_nan_cols),
        "anomalies": all_nan_cols,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def summarize_feature_infinite_value_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary of infinite and degenerate feature checks."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    res_inf = validate_no_infinite_values(df, feat_cols)
    res_nan = validate_no_all_nan_features(df, feat_cols)

    passed = res_inf["passed"] and res_nan["passed"]
    return {
        "passed": passed,
        "status": "validation_pass" if passed else "validation_fail",
        "infinite_anomaly_count": res_inf["columns_with_infinite_values"],
        "all_nan_column_count": res_nan["all_nan_column_count"],
        "manual_review_required": not passed,
    }


def validate_feature_infinite_values(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate infinite values across all numeric columns in DataFrame."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    total_inf = 0
    columns_with_inf = []

    for col in feat_cols:
        s = df[col]
        if pd.api.types.is_numeric_dtype(s):
            count = int(np.isinf(s).sum())
            if count > 0:
                total_inf += count
                columns_with_inf.append(col)

    is_valid = total_inf == 0
    return {
        "is_valid": is_valid,
        "infinite_count": total_inf,
        "columns_with_infinite_values": columns_with_inf,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

