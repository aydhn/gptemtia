"""Phase 127: Regime Matrix Asof Join Policies.

Enforces strictly backward-only temporal joins, zero forward/nearest matching,
and non-mutating transformations returning clean copied DataFrames.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

ASOF_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "asof_policy_backward_only",
        "policy_name": "Strict Backward Direction",
        "description": "pd.merge_asof must strictly use direction='backward' to prevent future observation contamination.",
        "direction": "backward",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "asof_policy_non_mutating",
        "policy_name": "Non-Mutating Input Preservation",
        "description": "Input dataframes must never be mutated in-place; copy() is created before joining.",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "asof_policy_monotonic_order",
        "policy_name": "Strict Monotonic Sort Requirement",
        "description": "Both left and right timestamp indices must be sorted in ascending order prior to join.",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "asof_policy_no_nearest_or_forward",
        "policy_name": "Prohibit Nearest or Forward Joins",
        "description": "direction='nearest' and direction='forward' are strictly disallowed in all asof operations.",
        "direction": "backward",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "asof_policy_entity_partition_alignment",
        "policy_name": "Entity Partition Alignment",
        "description": "Multi-asset joins must partition strictly by canonical entity ID (by parameter).",
        "is_enforced": True,
        "non_signal": True,
    },
]


def build_regime_matrix_asof_join_policy_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the asof join policy registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for pol in ASOF_POLICIES:
        p_copy = pol.copy()
        p_copy["current_phase"] = p.current_phase
        p_copy["target_final_phase"] = p.target_final_phase
        p_copy["next_phase"] = p.next_phase
        p_copy["source_preserved"] = True
        p_copy["status"] = "matrix_ready"
        rows.append(p_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_asof_join_policies(df)
    return df, summary


def safe_regime_matrix_asof_join_backward(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_on: str,
    right_on: str,
    by: Optional[str] = None,
    tolerance: Optional[Any] = None,
) -> pd.DataFrame:
    """Execute a strictly backward-only asof join without mutating inputs."""
    # Defensive copies
    left = left_df.copy()
    right = right_df.copy()

    # Ensure timestamp conversion and sorting
    left[left_on] = pd.to_datetime(left[left_on])
    right[right_on] = pd.to_datetime(right[right_on])

    left = left.sort_values(by=left_on)
    right = right.sort_values(by=right_on)

    kwargs: Dict[str, Any] = {
        "left_on": left_on,
        "right_on": right_on,
        "direction": "backward",
    }
    if by is not None and by in left.columns and by in right.columns:
        kwargs["by"] = by
    if tolerance is not None:
        kwargs["tolerance"] = tolerance

    joined = pd.merge_asof(left, right, **kwargs)
    return joined


def summarize_regime_matrix_asof_join_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize asof join policy registry."""
    return {
        "total_policies": len(df),
        "policy_ids": df["policy_id"].tolist() if not df.empty else [],
        "mandatory_direction": "backward",
        "all_enforced": bool(df["is_enforced"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_asof_join_policies = build_regime_matrix_asof_join_policy_registry

