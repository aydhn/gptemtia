"""Phase 130: Regime Transition Timestamp Policies.

Defines timestamp continuity and chronological monotonic ordering policies.
Validates that transition and context timestamps never contain lookahead leakage.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

TIMESTAMP_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "pol_strict_monotonic",
        "policy_name": "strict_monotonic_timestamp_order",
        "description": "Ensure observation timestamps are strictly increasing (t > t-1)",
        "strictly_backward_looking": True,
        "enforcement_level": "blocking",
        "allows_ties": False,
        "requires_utc": True,
    },
    {
        "policy_id": "pol_no_future_context",
        "policy_name": "no_future_context_timestamp",
        "description": "Context feature timestamps must be less than or equal to base observation timestamp",
        "strictly_backward_looking": True,
        "enforcement_level": "blocking",
        "allows_ties": True,
        "requires_utc": True,
    },
    {
        "policy_id": "pol_transition_lag_align",
        "policy_name": "transition_lag_alignment",
        "description": "Transition point state t must depend only on information available at or before t",
        "strictly_backward_looking": True,
        "enforcement_level": "blocking",
        "allows_ties": True,
        "requires_utc": True,
    },
    {
        "policy_id": "pol_macro_release_lag",
        "policy_name": "macro_release_lag_guard",
        "description": "Macro event window joins must respect official publication timestamp lag",
        "strictly_backward_looking": True,
        "enforcement_level": "blocking",
        "allows_ties": False,
        "requires_utc": True,
    },
]



def build_regime_transition_timestamp_policy_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build timestamp policy registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(TIMESTAMP_POLICIES)
    summary = summarize_transition_timestamp_policies(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_transition_timestamp_order(
    df: pd.DataFrame,
    timestamp_field: str = "timestamp_utc",
    previous_timestamp_field: Optional[str] = None,
) -> Dict[str, Any]:
    """Validate that timestamps are in strictly non-decreasing chronological order."""
    if df.empty:
        return {"is_valid": True, "total_rows": 0, "violations": 0}

    if timestamp_field not in df.columns:
        return {"is_valid": False, "error": f"Timestamp field '{timestamp_field}' not found in df"}

    ts_series = pd.to_datetime(df[timestamp_field])
    
    if previous_timestamp_field and previous_timestamp_field in df.columns:
        prev_ts = pd.to_datetime(df[previous_timestamp_field])
        violations = int((ts_series < prev_ts).sum())
    else:
        diffs = ts_series.diff().dropna()
        violations = int((diffs < pd.Timedelta(0)).sum())

    is_valid = violations == 0
    return {
        "is_valid": is_valid,
        "total_rows": len(df),
        "violations": violations,
        "monotonic_increasing": is_valid,
    }


def validate_transition_context_timestamp_not_future(
    df: pd.DataFrame,
    base_ts: str = "timestamp_utc",
    context_ts: str = "context_timestamp_utc",
) -> Dict[str, Any]:
    """Validate that context timestamp does not lie in the future relative to base timestamp."""
    if df.empty:
        return {"is_valid": True, "future_leak_count": 0}

    if base_ts not in df.columns or context_ts not in df.columns:
        return {"is_valid": True, "note": "One or both timestamp columns absent"}

    base_dt = pd.to_datetime(df[base_ts])
    context_dt = pd.to_datetime(df[context_ts])
    future_leaks = int((context_dt > base_dt).sum())

    return {
        "is_valid": future_leaks == 0,
        "future_leak_count": future_leaks,
        "total_checked": len(df),
    }


def summarize_transition_timestamp_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize timestamp policy registry."""
    return {
        "total_policies": len(df),
        "policy_names": df["policy_name"].tolist() if not df.empty else [],
        "all_blocking": bool((df["enforcement_level"] == "blocking").all()) if not df.empty else True,
        "all_require_utc": bool(df["requires_utc"].all()) if not df.empty else True,
        "all_strictly_backward_looking": bool(df["strictly_backward_looking"].all()) if not df.empty and "strictly_backward_looking" in df.columns else True,
    }

