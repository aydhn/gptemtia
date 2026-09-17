# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty No-Lookahead Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

LOOKAHEAD_TERMS_UNCERTAINTY = [
    "future_return",
    "forward_return",
    "next_return",
    "shift(-1)",
    "shift_-1",
    "lead_1",
    "target_t_plus_1",
    "future_price",
]


def build_uncertainty_no_lookahead_guard_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for uncertainty no-lookahead guards."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "guard_id": "uncert_guard_no_future_columns",
            "rule_name": "prohibit_future_and_forward_return_columns",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "guard_id": "uncert_guard_temporal_asof_joins",
            "rule_name": "enforce_backward_asof_joins_only",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "guard_id": "uncert_guard_monotonic_timestamps",
            "rule_name": "enforce_strictly_monotonic_ascending_timestamps",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_no_lookahead_guards(df)
    return df, summary


def validate_uncertainty_no_lookahead_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate column names against future lookahead terms for uncertainty."""
    violations = []
    for col in column_names:
        c_lower = col.lower()
        for term in LOOKAHEAD_TERMS_UNCERTAINTY:
            if term in c_lower:
                violations.append(f"Column '{col}' violates no-lookahead policy (matches '{term}')")

    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violations": violations,
        "status": "PASS" if is_valid else "LOOKAHEAD_VIOLATION_DETECTED",
        "non_signal": True,
    }


def validate_no_future_uncertainty_join(
    left_df: pd.DataFrame, right_df: pd.DataFrame, left_ts: str, right_ts: str
) -> Dict[str, Any]:
    """Validate that joining left_df and right_df introduces no lookahead bias."""
    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {"is_valid": False, "reason": "Missing timestamp columns for temporal validation."}

    max_left = pd.to_datetime(left_df[left_ts]).max()
    min_right = pd.to_datetime(right_df[right_ts]).min()
    has_leakage = bool(min_right > max_left) if (not left_df.empty and not right_df.empty) else False

    return {
        "is_valid": not has_leakage,
        "temporal_alignment_valid": not has_leakage,
        "non_signal": True,
    }


def summarize_uncertainty_no_lookahead_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty no-lookahead guards DataFrame."""
    return {
        "total_guards": len(df),
        "guards": df["guard_id"].tolist() if not df.empty else [],
        "all_active": bool(df["is_active"].all()) if not df.empty else True,
        "all_blocking": bool(df["blocking"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
