# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model No-Lookahead Input Guards.

Provides validation rules preventing forward-looking columns, shifts,
future return calculations, and prospective joins in baseline model inputs.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

LOOKAHEAD_TRIGGER_PATTERNS = [
    "future_", "forward_", "next_", "shift(-1)", "shift(-",
    "lead_", "t+1", "t+2", "ahead_", "future_return",
]

NO_LOOKAHEAD_GUARDS = [
    {"guard_id": "guard_timestamp_order_ascending", "scope": "temporal_order", "enforced": True, "description": "Ensures timestamps are monotonic ascending"},
    {"guard_id": "guard_no_future_columns", "scope": "column_inspection", "enforced": True, "description": "Blocks column names with forward/future return semantics"},
    {"guard_id": "guard_backward_asof_only", "scope": "merge_policy", "enforced": True, "description": "Requires as-of joins to use backward direction only"},
    {"guard_id": "guard_no_shift_negative", "scope": "feature_computation", "enforced": True, "description": "Rejects any shift(-k) lookahead calculations"},
]


def build_baseline_model_no_lookahead_input_guard_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-lookahead guards registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for g in NO_LOOKAHEAD_GUARDS:
        rows.append({
            "guard_id": g["guard_id"],
            "scope": g["scope"],
            "enforced": g["enforced"],
            "description": g["description"],
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_no_lookahead_guards(df)
    return df, summary


def validate_baseline_model_no_lookahead_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect column names for any forward-looking / lookahead tokens."""
    violations = []
    for col in column_names:
        c_lower = col.lower()
        for pattern in LOOKAHEAD_TRIGGER_PATTERNS:
            if pattern in c_lower:
                violations.append(f"Column '{col}' matches forbidden lookahead pattern '{pattern}'")

    valid = len(violations) == 0
    return {
        "valid": valid,
        "violations": violations,
        "total_columns_checked": len(column_names),
        "status": "VALID_NO_LOOKAHEAD" if valid else "LOOKAHEAD_VIOLATION_DETECTED",
        "non_signal": True,
    }


def validate_no_future_baseline_model_join(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_ts: str,
    right_ts: str,
) -> Dict[str, Any]:
    """Validate that right_df does not have timestamps in the future of left_df when joining."""
    if left_df.empty or right_df.empty:
        return {"valid": True, "violations": [], "status": "EMPTY_DATAFRAMES_VALID", "non_signal": True}

    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {"valid": False, "violations": ["Missing timestamp columns"], "status": "INVALID_TS_COLUMN", "non_signal": True}

    max_left = pd.to_datetime(left_df[left_ts]).max()
    max_right = pd.to_datetime(right_df[right_ts]).max()

    violations = []
    if max_right > max_left:
        violations.append(f"Right dataframe contains future timestamps: {max_right} > {max_left}")

    valid = len(violations) == 0
    return {
        "valid": valid,
        "violations": violations,
        "status": "VALID_NO_FUTURE_JOIN" if valid else "FUTURE_TIMESTAMP_JOIN_BLOCKED",
        "non_signal": True,
    }


def summarize_baseline_model_no_lookahead_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no-lookahead guards."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
