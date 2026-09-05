"""Feature Numeric Sanity Validation.

Verifies that feature columns contain strictly numeric data types and finite, sane values.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import numpy as np
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_feature_numeric_sanity_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of numeric sanity rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "check_name": "numeric_dtype_compliance",
            "description": "All feature columns must have float or integer data types.",
            "severity": "validation_high",
            "enforced": True,
        },
        {
            "check_name": "numeric_range_sanity",
            "description": "Values must not exceed realistic floating-point magnitude limits (1e12).",
            "severity": "validation_medium",
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_checks": len(records),
        "enforced": True,
        "non_signal": True,
    }
    return df, summary


def validate_numeric_feature_columns(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Verify that all specified feature columns are numeric."""
    non_numeric = []

    for col in feature_columns:
        if col in df.columns:
            dtype = df[col].dtype
            if not pd.api.types.is_numeric_dtype(df[col]):
                non_numeric.append({
                    "column": col,
                    "dtype": str(dtype),
                    "severity": "validation_high",
                })

    passed = len(non_numeric) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_columns_checked": len(feature_columns),
        "non_numeric_count": len(non_numeric),
        "non_numeric_columns": non_numeric,
        "manual_review_required": not passed,
    }


def validate_numeric_range_sanity(
    df: pd.DataFrame, feature_columns: List[str], max_magnitude: float = 1e12
) -> Dict[str, Any]:
    """Check for extreme numerical outliers or corrupted floats."""
    range_violations = []

    for col in feature_columns:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            s = df[col].dropna()
            if len(s) > 0:
                abs_max = float(s.abs().max())
                if abs_max > max_magnitude or np.isnan(abs_max):
                    range_violations.append({
                        "column": col,
                        "abs_max_value": abs_max,
                        "max_allowed_magnitude": max_magnitude,
                        "severity": "validation_medium",
                    })

    passed = len(range_violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_pass_with_warnings",
        "total_columns_checked": len(feature_columns),
        "violation_count": len(range_violations),
        "range_violations": range_violations,
        "manual_review_required": not passed,
    }


def summarize_feature_numeric_sanity_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary of numeric sanity for a DataFrame."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    res_dtype = validate_numeric_feature_columns(df, feat_cols)
    res_range = validate_numeric_range_sanity(df, feat_cols)

    passed = res_dtype["passed"] and res_range["passed"]
    return {
        "passed": passed,
        "status": "validation_pass" if passed else "validation_fail",
        "non_numeric_columns_count": res_dtype["non_numeric_count"],
        "range_violations_count": res_range["violation_count"],
        "manual_review_required": not passed,
    }


def validate_feature_numeric_sanity(
    df: pd.DataFrame, abs_max_threshold: float = 1e10
) -> Dict[str, Any]:
    """Validate numeric sanity and detect extreme magnitude outliers."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    outlier_columns = []

    for col in feat_cols:
        s = df[col]
        if pd.api.types.is_numeric_dtype(s):
            val_max = s.abs().max()
            if pd.notna(val_max) and val_max > abs_max_threshold:
                outlier_columns.append(col)
        else:
            outlier_columns.append(col)

    is_valid = len(outlier_columns) == 0
    return {
        "is_valid": is_valid,
        "outlier_columns": outlier_columns,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

