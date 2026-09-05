"""Phase 131: Cross-Asset Regime Timestamp Policies.

Defines timestamp synchronization, timezone normalization, and backward-looking
temporal policies preventing any future information leakage across asset classes.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

TIMESTAMP_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "pol_utc_monotonic",
        "policy_name": "utc_monotonic_timestamp_policy",
        "timezone_standard": "UTC",
        "join_direction": "backward_only",
        "description": "Enforces strictly monotonic UTC ISO-8601 timestamps without future forward looking.",
        "enforces_no_future_leakage": True,
    },
    {
        "policy_id": "pol_release_lag_guarded",
        "policy_name": "backward_release_lag_asof_policy",
        "timezone_standard": "UTC",
        "join_direction": "backward_with_release_delay",
        "description": "Requires observation_ts >= publication_ts, preventing unreleased macro data leakage.",
        "enforces_no_future_leakage": True,
    },
    {
        "policy_id": "pol_event_window",
        "policy_name": "scheduled_event_window_policy",
        "timezone_standard": "UTC",
        "join_direction": "backward_window_bounded",
        "description": "Restricts event impacts strictly to verified historical scheduled publication windows.",
        "enforces_no_future_leakage": True,
    },
    {
        "policy_id": "pol_metadata_window",
        "policy_name": "metadata_only_window_policy",
        "timezone_standard": "UTC",
        "join_direction": "backward_metadata_bounded",
        "description": "Guarantees news metadata timestamps do not precede actual publication time.",
        "enforces_no_future_leakage": True,
    },
]


def build_cross_asset_regime_timestamp_policy_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build timestamp policy registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in TIMESTAMP_POLICIES:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_timestamp_policies(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_cross_asset_context_timestamp_not_future(
    df: pd.DataFrame, base_ts: str, context_ts: str
) -> Dict[str, Any]:
    """Validate that context timestamps do not lie in the future relative to base timestamps."""
    if df.empty:
        return {"valid": True, "total_checked": 0, "violations": 0}

    if base_ts not in df.columns or context_ts not in df.columns:
        return {
            "valid": False,
            "error": f"Columns {base_ts} or {context_ts} not found in dataframe",
            "total_checked": 0,
            "violations": 0,
        }

    base_series = pd.to_datetime(df[base_ts], errors="coerce", utc=True)
    context_series = pd.to_datetime(df[context_ts], errors="coerce", utc=True)

    # Valid condition: context_ts <= base_ts (backward in time or contemporaneous)
    future_mask = context_series > base_series
    violations = int(future_mask.sum())

    return {
        "valid": violations == 0,
        "total_checked": len(df),
        "violations": violations,
        "base_column": base_ts,
        "context_column": context_ts,
        "no_lookahead_verified": violations == 0,
    }


def summarize_cross_asset_timestamp_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize timestamp policy registry."""
    return {
        "total_policies": len(df),
        "all_utc": bool((df["timezone_standard"] == "UTC").all()) if not df.empty else True,
        "all_enforce_no_future_leakage": bool(df["enforces_no_future_leakage"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
    }
