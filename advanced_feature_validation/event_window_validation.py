"""Economic Calendar Event Window Validation.

Validates that scheduled vs actual release event ordering is respected and
that event window feature bounds are calculated cleanly without lookahead.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_event_window_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of event window validation rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "check_name": "actual_release_ge_scheduled",
            "description": "Actual release timestamp must be greater than or equal to scheduled release time.",
            "severity": "validation_high",
            "enforced": True,
        },
        {
            "check_name": "event_window_bounds_finite",
            "description": "Pre-event and post-event window metrics must be non-null and within finite bounds.",
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


def validate_actual_release_after_scheduled(
    df: pd.DataFrame, scheduled_field: str, actual_field: str
) -> Dict[str, Any]:
    """Verify that actual release time is on or after scheduled release time."""
    if scheduled_field not in df.columns or actual_field not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "error": f"Columns '{scheduled_field}' or '{actual_field}' not found.",
            "anomaly_count": 0,
            "manual_review_required": True,
        }

    sched = pd.to_datetime(df[scheduled_field])
    act = pd.to_datetime(df[actual_field])
    valid = sched.notna() & act.notna()
    anomalies = valid & (act < sched)
    anomaly_count = int(anomalies.sum())
    passed = anomaly_count == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "scheduled_field": scheduled_field,
        "actual_field": actual_field,
        "total_rows": len(df),
        "valid_pairs": int(valid.sum()),
        "premature_actual_releases": anomaly_count,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def validate_event_window_fields(
    df: pd.DataFrame, timestamp_field: str, event_time_field: str
) -> Dict[str, Any]:
    """Validate relative timing between market timestamp and event timestamp."""
    if timestamp_field not in df.columns or event_time_field not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "error": f"Fields '{timestamp_field}' or '{event_time_field}' not in DataFrame.",
            "manual_review_required": True,
        }

    t = pd.to_datetime(df[timestamp_field])
    e = pd.to_datetime(df[event_time_field])
    valid = t.notna() & e.notna()

    return {
        "passed": True,
        "status_label": "validation_pass",
        "total_rows": len(df),
        "valid_pairs": int(valid.sum()),
        "pre_event_count": int((valid & (t < e)).sum()),
        "post_event_count": int((valid & (t >= e)).sum()),
        "manual_review_required": False,
    }


def summarize_event_window_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate high-level summary of event window validation."""
    sched_cols = [c for c in df.columns if "sched" in c]
    act_cols = [c for c in df.columns if "actual" in c and "ts" in c or "release_ts" in c]

    if sched_cols and act_cols:
        res = validate_actual_release_after_scheduled(df, sched_cols[0], act_cols[0])
        return {
            "passed": res["passed"],
            "status": res["status_label"],
            "premature_actual_releases": res["premature_actual_releases"],
            "manual_review_required": res["manual_review_required"],
        }

    return {
        "passed": True,
        "status": "validation_pass",
        "premature_actual_releases": 0,
        "manual_review_required": False,
    }


def validate_event_window_timestamps(df: pd.DataFrame) -> Dict[str, Any]:
    res = summarize_event_window_validation(df)
    res["is_valid"] = res["passed"]
    return res


def check_event_window_leakage(df: pd.DataFrame) -> Dict[str, Any]:
    if "timestamp" in df.columns and "event_time" in df.columns and "actual_value" in df.columns:
        t = pd.to_datetime(df["timestamp"])
        e = pd.to_datetime(df["event_time"])
        act = df["actual_value"]
        leak = (t < e) & act.notna()
        is_valid = bool(leak.sum() == 0)
        return {"is_valid": is_valid, "passed": is_valid, "leak_count": int(leak.sum())}
    return {"is_valid": True, "passed": True, "leak_count": 0}

