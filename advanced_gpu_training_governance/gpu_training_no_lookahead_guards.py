# -*- coding: utf-8 -*-
"""Phase 139 GPU Training No-Lookahead Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

LOOKAHEAD_SUSPICIOUS_TERMS: List[str] = [
    "future",
    "forward",
    "next_",
    "lead_",
    "t_plus",
    "shift(-",
    "shift(-1)",
    "target_next",
    "label_lead",
]


def build_gpu_training_no_lookahead_guard_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-lookahead guards registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    guards = [
        {
            "guard_id": "NLA_GRD_001",
            "guard_name": "column_naming_lookahead_guard",
            "check_type": "column_inspection",
            "enforced": True,
            "non_signal": True,
            "description": "Scans column headers for future/forward/next/lead prefixes or suffixes.",
            "status": "gpu_governance_ready",
        },
        {
            "guard_id": "NLA_GRD_002",
            "guard_name": "timestamp_order_integrity_guard",
            "check_type": "temporal_validation",
            "enforced": True,
            "non_signal": True,
            "description": "Ensures all training inputs respect strictly ascending chronological order.",
            "status": "gpu_governance_ready",
        },
        {
            "guard_id": "NLA_GRD_003",
            "guard_name": "backward_asof_join_guard",
            "check_type": "join_validation",
            "enforced": True,
            "non_signal": True,
            "description": "Validates that joins only match past or current timestamps (no future right-hand keys).",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(guards)
    summary = summarize_gpu_training_no_lookahead_guards(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_gpu_training_no_lookahead_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that column names contain no lookahead or future references."""
    violating_columns = []
    for col in column_names:
        c_lower = col.lower()
        for term in LOOKAHEAD_SUSPICIOUS_TERMS:
            if term in c_lower:
                violating_columns.append(col)
                break

    is_clean = len(violating_columns) == 0
    return {
        "is_clean": is_clean,
        "violating_columns": violating_columns,
        "total_columns_checked": len(column_names),
        "non_signal": True,
        "status": "PASS" if is_clean else "FAIL_LOOKAHEAD",
    }


def validate_no_future_gpu_training_join(
    left_df: pd.DataFrame, right_df: pd.DataFrame, left_ts: str, right_ts: str
) -> Dict[str, Any]:
    """Validate that joining left_df with right_df does not incorporate future timestamps."""
    if left_df.empty or right_df.empty:
        return {"is_valid": True, "violations_count": 0, "non_signal": True, "status": "EMPTY_PASS"}

    # Convert timestamps to datetime if present
    l_series = pd.to_datetime(left_df[left_ts], errors="coerce")
    r_series = pd.to_datetime(right_df[right_ts], errors="coerce")

    # In a backward asof join, max right timestamp used should never exceed max left timestamp
    max_left = l_series.max()
    max_right = r_series.max()
    has_future_leakage = bool(max_right > max_left) if pd.notna(max_left) and pd.notna(max_right) else False

    return {
        "is_valid": not has_future_leakage,
        "max_left_timestamp": str(max_left),
        "max_right_timestamp": str(max_right),
        "has_future_leakage": has_future_leakage,
        "non_signal": True,
        "status": "PASS" if not has_future_leakage else "FAIL_TEMPORAL_LEAKAGE",
    }


def summarize_gpu_training_no_lookahead_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no-lookahead guards DataFrame."""
    if df.empty:
        return {"total_guards": 0, "non_signal": True}
    return {
        "total_guards": len(df),
        "all_enforced": bool((df["enforced"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
