"""Duplicate Feature Validation.

Identifies duplicate column names and identical feature value series across matrices.
Strictly non-signal and research-only.
"""

from collections import Counter
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_duplicate_feature_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of duplicate feature validation rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "check_name": "no_duplicate_column_names",
            "description": "Verifies that all column names in the feature matrix are globally unique.",
            "severity": "validation_high",
            "enforced": True,
        },
        {
            "check_name": "no_identical_feature_values",
            "description": "Flags feature columns that contain identical numerical series (collinear duplicates).",
            "severity": "validation_medium",
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_checks": len(records),
        "auto_deletion_allowed": False,
        "non_signal": True,
    }
    return df, summary


def validate_duplicate_feature_names(feature_columns: List[str]) -> Dict[str, Any]:
    """Check for duplicate column names in a list of column names."""
    counts = Counter(feature_columns)
    duplicates = [name for name, cnt in counts.items() if cnt > 1]
    passed = len(duplicates) == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_columns": len(feature_columns),
        "unique_columns": len(counts),
        "duplicate_count": len(duplicates),
        "duplicate_names": duplicates,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def validate_duplicate_feature_values(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Scan for pairs of feature columns with identical numerical values."""
    valid_cols = [c for c in feature_columns if c in df.columns]
    identical_pairs = []

    # Compare pairs
    for i in range(len(valid_cols)):
        for j in range(i + 1, len(valid_cols)):
            col1 = valid_cols[i]
            col2 = valid_cols[j]
            s1 = df[col1]
            s2 = df[col2]

            # Check if both are numeric and equal
            if pd.api.types.is_numeric_dtype(s1) and pd.api.types.is_numeric_dtype(s2):
                if s1.equals(s2):
                    identical_pairs.append({
                        "column_1": col1,
                        "column_2": col2,
                        "severity": "validation_medium",
                    })

    passed = len(identical_pairs) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_pass_with_warnings",
        "total_pairs_compared": len(valid_cols) * (len(valid_cols) - 1) // 2 if len(valid_cols) > 1 else 0,
        "identical_pair_count": len(identical_pairs),
        "identical_pairs": identical_pairs,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def summarize_duplicate_feature_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary of duplicate validation for a DataFrame."""
    res_names = validate_duplicate_feature_names(list(df.columns))
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    res_vals = validate_duplicate_feature_values(df, feat_cols)

    passed = res_names["passed"] and res_vals["passed"]
    return {
        "passed": passed,
        "status": "validation_pass" if passed else "validation_manual_review_required",
        "duplicate_name_count": res_names["duplicate_count"],
        "identical_value_pair_count": res_vals["identical_pair_count"],
        "manual_review_required": not passed,
    }


def validate_duplicate_feature_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate duplicate feature column names without destructive actions."""
    cols = list(df.columns)
    counts = Counter(cols)
    dup_cols = [col for col, count in counts.items() if count > 1]
    duplicate_count = len(cols) - len(set(cols))
    is_valid = duplicate_count == 0

    return {
        "is_valid": is_valid,
        "duplicate_columns_count": duplicate_count,
        "duplicate_columns": dup_cols,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

