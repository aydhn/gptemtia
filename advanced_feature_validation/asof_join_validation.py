"""Asof Join Direction and Policy Validation.

Ensures all asof joins enforce backward-only direction without future lookup.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

PROHIBITED_JOIN_POLICIES = [
    "direction='forward'",
    "direction=\"forward\"",
    "direction='nearest'",
    "direction=\"nearest\"",
    "allow_exact_matches=False, direction='forward'",
]


def build_asof_join_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of asof join rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "policy_rule": "backward_only_mandatory",
            "description": "All merge_asof operations must specify direction='backward'.",
            "severity": "validation_critical",
            "prohibited_alternatives": ["forward", "nearest"],
            "enforced": True,
        },
        {
            "policy_rule": "context_timestamp_non_future",
            "description": "Output context timestamps must satisfy context_ts <= base_ts.",
            "severity": "validation_critical",
            "prohibited_alternatives": ["context_ts > base_ts"],
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_rules": len(records),
        "enforced_direction": "backward",
        "current_phase": active_profile.current_phase,
        "non_signal": True,
    }
    return df, summary


def validate_backward_asof_join_result(
    df: pd.DataFrame, base_ts: str, context_ts: str
) -> Dict[str, Any]:
    """Verify that an asof join result satisfies backward causality."""
    if base_ts not in df.columns or context_ts not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "error": f"Columns '{base_ts}' or '{context_ts}' not found.",
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
        "total_rows": len(df),
        "valid_pairs": int(valid.sum()),
        "future_leakage_count": leakage_count,
        "message": "Backward asof join verified; zero future data leakage."
        if passed
        else f"Failed: {leakage_count} records contain context timestamps later than base timestamp.",
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def validate_no_nearest_forward_join_policy(policy_text: str) -> Dict[str, Any]:
    """Scan policy string or configuration text for forward/nearest directives."""
    violations: List[str] = []
    text_lower = policy_text.lower()

    if "forward" in text_lower:
        violations.append("found_forward_direction")
    if "nearest" in text_lower:
        violations.append("found_nearest_direction")

    passed = len(violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "violations": violations,
        "manual_review_required": not passed,
    }


def summarize_asof_join_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize asof join validation status for a DataFrame."""
    base_cols = [c for c in df.columns if "base" in c or c == "timestamp"]
    ctx_cols = [c for c in df.columns if "context" in c or "release" in c or "published" in c]

    if base_cols and ctx_cols:
        res = validate_backward_asof_join_result(df, base_cols[0], ctx_cols[0])
        return {
            "passed": res["passed"],
            "status": res["status_label"],
            "future_leakage_count": res["future_leakage_count"],
            "manual_review_required": res["manual_review_required"],
        }
    return {
        "passed": True,
        "status": "validation_pass",
        "future_leakage_count": 0,
        "manual_review_required": False,
    }


def validate_asof_join_direction(direction: str) -> Dict[str, Any]:
    d_clean = str(direction).lower().strip()
    is_valid = (d_clean == "backward")
    return {
        "is_valid": is_valid,
        "passed": is_valid,
        "direction": direction,
        "status": "PASS" if is_valid else "FAIL",
    }


def validate_asof_join_timestamps(base_ts, context_ts) -> Dict[str, Any]:
    b = pd.to_datetime(base_ts)
    c = pd.to_datetime(context_ts)
    valid = b.notna() & c.notna()
    leakage = valid & (c > b)
    is_valid = bool(leakage.sum() == 0)
    return {
        "is_valid": is_valid,
        "passed": is_valid,
        "leakage_count": int(leakage.sum()),
    }

