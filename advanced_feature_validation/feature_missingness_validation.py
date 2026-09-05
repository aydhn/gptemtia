"""Feature Missingness Validation.

Calculates missingness ratios across feature columns and validates against configurable thresholds.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_feature_missingness_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of missingness validation policies."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "policy_rule": "missingness_threshold_check",
            "default_threshold": 0.50,
            "description": "Flags feature columns where NaN ratio exceeds threshold for review.",
            "severity": "validation_medium",
            "enforced": True,
        },
        {
            "policy_rule": "no_auto_drop_missing",
            "description": "Never automatically drop rows or columns with high missingness; queue for review.",
            "severity": "validation_medium",
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_rules": len(records),
        "default_threshold": 0.50,
        "auto_drop_allowed": False,
        "non_signal": True,
    }
    return df, summary


def calculate_feature_missingness(
    df: pd.DataFrame, feature_columns: List[str]
) -> pd.DataFrame:
    """Calculate total rows, missing count, and missing ratio for each feature column."""
    records = []
    total_rows = len(df)

    for col in feature_columns:
        if col in df.columns:
            missing_count = int(df[col].isna().sum())
            missing_ratio = float(missing_count / total_rows) if total_rows > 0 else 0.0
            records.append({
                "column": col,
                "total_rows": total_rows,
                "missing_count": missing_count,
                "missing_ratio": round(missing_ratio, 4),
            })

    return pd.DataFrame(records)


def validate_feature_missingness_threshold(
    df: pd.DataFrame, feature_columns: List[str], threshold: float = 0.5
) -> Dict[str, Any]:
    """Flag columns where missingness exceeds threshold."""
    missingness_df = calculate_feature_missingness(df, feature_columns)
    violations = []

    if not missingness_df.empty:
        excessive = missingness_df[missingness_df["missing_ratio"] > threshold]
        for _, row in excessive.iterrows():
            violations.append({
                "column": row["column"],
                "missing_ratio": row["missing_ratio"],
                "threshold": threshold,
                "severity": "validation_medium",
            })

    passed = len(violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_pass_with_warnings",
        "threshold": threshold,
        "total_features_checked": len(feature_columns),
        "columns_exceeding_threshold": len(violations),
        "violations": violations,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def summarize_feature_missingness_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary of missingness compliance."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    res = validate_feature_missingness_threshold(df, feat_cols)

    return {
        "passed": res["passed"],
        "status": res["status_label"],
        "columns_exceeding_threshold": res["columns_exceeding_threshold"],
        "manual_review_required": res["manual_review_required"],
    }


def validate_feature_missingness(
    df: pd.DataFrame, max_missingness_ratio: float = 0.35
) -> Dict[str, Any]:
    """Validate missingness ratios across feature columns."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    excessive_missing_columns = []
    total_rows = len(df)

    if total_rows > 0:
        for col in feat_cols:
            missing_ratio = float(df[col].isna().sum() / total_rows)
            if missing_ratio > max_missingness_ratio:
                excessive_missing_columns.append(col)

    is_valid = len(excessive_missing_columns) == 0
    return {
        "is_valid": is_valid,
        "max_missingness_ratio": max_missingness_ratio,
        "excessive_missing_columns": excessive_missing_columns,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

