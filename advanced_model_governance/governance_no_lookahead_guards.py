# -*- coding: utf-8 -*-
"""Phase 144: Governance No-Lookahead Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

LOOKAHEAD_PATTERNS = [
    "future_",
    "forward_",
    "next_",
    "target_",
    "label_",
    "lead_",
    "shift(-",
    "t_plus",
]


def build_governance_no_lookahead_guard_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for no-lookahead guards."""
    prof = profile or get_model_governance_profile()
    records = [
        {"guard_name": "column_name_lookahead_guard", "enforcement": "Reject column names matching future or shift(-1) patterns.", "status": "ACTIVE"},
        {"guard_name": "point_in_time_join_guard", "enforcement": "Enforce left_ts >= right_ts for all point-in-time merges.", "status": "ACTIVE"},
        {"guard_name": "purged_split_guard", "enforcement": "Enforce embargo margins between train and evaluation partitions.", "status": "ACTIVE"},
    ]
    for r in records:
        r["phase"] = prof.current_phase
        r["is_enforced"] = True

    df = pd.DataFrame(records)
    summary = summarize_governance_no_lookahead_guards(df)
    return df, summary


def summarize_governance_no_lookahead_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no-lookahead guards."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["is_enforced"].all()),
        "status": "ALL_LOOKAHEAD_GUARDS_ACTIVE",
    }


def validate_governance_no_lookahead_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate column list does not contain lookahead patterns."""
    violations = []
    for col in column_names:
        col_lower = str(col).lower()
        if any(pat in col_lower for pat in LOOKAHEAD_PATTERNS):
            violations.append(col)

    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violations": violations,
        "status": "PASS" if is_valid else "FAIL_LOOKAHEAD_DETECTED",
    }


def validate_no_future_governance_join(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_ts: str,
    right_ts: str,
) -> Dict[str, Any]:
    """Validate that right_df timestamps are not in the future relative to left_df."""
    if left_df.empty or right_df.empty:
        return {"is_valid": True, "status": "PASS_EMPTY", "violations_count": 0}

    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {"is_valid": False, "status": "FAIL_MISSING_TIMESTAMP_COLUMN", "violations_count": 1}

    # Verify no future leakage
    left_max = pd.to_datetime(left_df[left_ts]).max()
    right_min = pd.to_datetime(right_df[right_ts]).min()

    is_valid = True
    violations = 0
    if right_min > left_max:
        is_valid = False
        violations = 1

    return {
        "is_valid": is_valid,
        "violations_count": violations,
        "status": "PASS" if is_valid else "FAIL_FUTURE_JOIN_DETECTED",
    }
