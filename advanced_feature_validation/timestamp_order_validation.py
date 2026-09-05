"""Timestamp Order and Monotonicity Validation.

Validates that timestamp indices are non-null, monotonically increasing, and free of future bias.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_timestamp_order_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of timestamp order validation rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "check_name": "timestamp_not_null",
            "description": "Verifies that timestamp field has zero null or missing values.",
            "severity": "validation_critical",
            "enforced": True,
        },
        {
            "check_name": "timestamp_monotonic_increasing",
            "description": "Verifies that timestamp sequence is strictly non-decreasing.",
            "severity": "validation_high",
            "enforced": True,
        },
        {
            "check_name": "context_timestamp_not_future",
            "description": "Verifies that joined context timestamp is on or before base timestamp.",
            "severity": "validation_critical",
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


def validate_timestamp_not_null(df: pd.DataFrame, timestamp_field: str) -> Dict[str, Any]:
    """Check that timestamp field has zero nulls."""
    if timestamp_field not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "timestamp_field": timestamp_field,
            "error": f"Field '{timestamp_field}' not in DataFrame columns.",
            "null_count": 0,
            "manual_review_required": True,
        }

    s = df[timestamp_field]
    null_count = int(s.isna().sum())
    passed = null_count == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "timestamp_field": timestamp_field,
        "total_rows": len(df),
        "null_count": null_count,
        "manual_review_required": not passed,
    }


def validate_timestamp_monotonic(df: pd.DataFrame, timestamp_field: str) -> Dict[str, Any]:
    """Check that timestamp values are monotonically non-decreasing."""
    if timestamp_field not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "timestamp_field": timestamp_field,
            "error": f"Field '{timestamp_field}' not in DataFrame columns.",
            "is_monotonic": False,
            "manual_review_required": True,
        }

    s = pd.to_datetime(df[timestamp_field])
    is_monotonic = bool(s.is_monotonic_increasing)
    non_monotonic_diffs = (s.diff().dt.total_seconds() < 0).sum()

    return {
        "passed": is_monotonic,
        "status_label": "validation_pass" if is_monotonic else "validation_fail",
        "timestamp_field": timestamp_field,
        "is_monotonic": is_monotonic,
        "negative_step_count": int(non_monotonic_diffs),
        "manual_review_required": not is_monotonic,
    }


def validate_context_timestamp_not_future(
    df: pd.DataFrame, base_ts: str, context_ts: str
) -> Dict[str, Any]:
    """Check that context timestamp is on or before base timestamp for every row."""
    if base_ts not in df.columns or context_ts not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "error": f"One or both fields missing: '{base_ts}', '{context_ts}'",
            "leakage_count": 0,
            "manual_review_required": True,
        }

    b = pd.to_datetime(df[base_ts])
    c = pd.to_datetime(df[context_ts])
    valid = b.notna() & c.notna()
    leakage = valid & (c > b)
    leakage_count = int(leakage.sum())
    passed = leakage_count == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "base_ts_field": base_ts,
        "context_ts_field": context_ts,
        "total_valid_pairs": int(valid.sum()),
        "leakage_count": leakage_count,
        "manual_review_required": not passed,
    }


def summarize_timestamp_order_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary of timestamp order validation for a DataFrame."""
    ts_field = "timestamp" if "timestamp" in df.columns else (df.columns[0] if len(df.columns) > 0 else "")
    res_null = validate_timestamp_not_null(df, ts_field) if ts_field else {"passed": False}
    res_mono = validate_timestamp_monotonic(df, ts_field) if ts_field else {"passed": False}
    passed = res_null.get("passed", False) and res_mono.get("passed", False)

    return {
        "passed": passed,
        "status": "validation_pass" if passed else "validation_fail",
        "timestamp_field": ts_field,
        "null_check_passed": res_null.get("passed", False),
        "monotonic_check_passed": res_mono.get("passed", False),
        "manual_review_required": not passed,
    }


def validate_timestamp_order(df: pd.DataFrame, timestamp_field: str = "timestamp") -> Dict[str, Any]:
    res = summarize_timestamp_order_validation(df)
    res["is_valid"] = res["passed"]
    res["monotonic_increasing"] = res.get("monotonic_check_passed", False)
    return res

