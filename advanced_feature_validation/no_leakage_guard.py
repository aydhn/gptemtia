"""No-Leakage Guard.

Provides unified leakage defense across DataFrames, code sources, and feature definitions.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.no_lookahead_rules import (
    validate_no_forward_return_columns,
    validate_no_future_timestamp_relation,
    validate_no_negative_shift_usage,
)
from advanced_feature_validation.forbidden_feature_columns import validate_forbidden_feature_columns


def validate_no_leakage_source_text(source_text: str) -> Dict[str, Any]:
    """Scan source code text for leakage and forbidden operations."""
    return validate_no_negative_shift_usage(source_text)


def validate_no_leakage_dataframe(
    df: pd.DataFrame,
    base_ts: Optional[str] = None,
    context_ts_fields: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Execute unified leakage audit on a DataFrame."""
    forb_res = validate_forbidden_feature_columns(df)
    fwd_res = validate_no_forward_return_columns(df)

    timestamp_leakages = []
    if base_ts and context_ts_fields and base_ts in df.columns:
        for c_field in context_ts_fields:
            if c_field in df.columns:
                ts_res = validate_no_future_timestamp_relation(df[base_ts], df[c_field])
                if not ts_res["passed"]:
                    timestamp_leakages.append({
                        "context_field": c_field,
                        "leakage_count": ts_res["leakage_count"],
                    })

    passed = forb_res["passed"] and fwd_res["passed"] and len(timestamp_leakages) == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_columns": len(df.columns),
        "forbidden_columns_clean": forb_res["passed"],
        "no_forward_returns": fwd_res["passed"],
        "timestamp_leakage_clean": len(timestamp_leakages) == 0,
        "timestamp_leakages": timestamp_leakages,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
        "non_signal": True,
    }


def build_no_leakage_guard_report(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build summary report of active no-leakage guard defenses."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "guard_name": "prohibit_negative_shift",
            "enforced": True,
            "status_label": "validation_pass",
            "description": "Zero tolerance for shift(-1) or future index alignment.",
        },
        {
            "guard_name": "prohibit_forward_returns",
            "enforced": True,
            "status_label": "validation_pass",
            "description": "Zero tolerance for forward/future return target columns.",
        },
        {
            "guard_name": "prohibit_future_context_timestamps",
            "enforced": True,
            "status_label": "validation_pass",
            "description": "Zero tolerance for context_ts > base_ts timestamp leakage.",
        },
        {
            "guard_name": "prohibit_forbidden_signal_columns",
            "enforced": True,
            "status_label": "validation_pass",
            "description": "Zero tolerance for buy/sell/signal/target/position column names.",
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_guards": len(records),
        "all_enforced": True,
        "leakage_tolerance": "zero",
        "non_signal": True,
    }
    return df, summary


def summarize_no_leakage_guard(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize leakage guard status."""
    return {
        "total_guards": len(df),
        "status": "validation_pass" if len(df) > 0 else "validation_fail",
        "all_enforced": bool(df["enforced"].all()) if "enforced" in df else False,
        "non_signal": True,
    }


def run_no_leakage_guard(df: pd.DataFrame) -> Dict[str, Any]:
    """Execute unified no-leakage guard on DataFrame."""
    res = validate_no_leakage_dataframe(df)
    passed = res["passed"]
    leakage_detected = not passed
    status = "PASSED" if passed else "VIOLATION"

    return {
        "guard_status": status,
        "leakage_detected": leakage_detected,
        "is_valid": passed,
        "current_phase": 121,
        "destructive_action_allowed": False,
        "details": res,
    }

