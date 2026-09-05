"""Phase 131: Cross-Asset Regime Asof Join Policies.

Defines safe backward-only asof join operations ensuring zero lookahead bias
and complete non-mutation of input dataframes.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

ASOF_JOIN_POLICIES: List[Dict[str, Any]] = [
    {
        "asof_policy_id": "asof_backward_exact_or_prior",
        "policy_name": "backward_asof_join_policy",
        "direction": "backward",
        "allow_exact_match": True,
        "allow_forward_join": False,
        "description": "Matches most recent prior or contemporaneous record (right_ts <= left_ts).",
        "enforces_zero_lookahead": True,
    },
    {
        "asof_policy_id": "asof_backward_release_lag",
        "policy_name": "backward_release_lag_asof_policy",
        "direction": "backward",
        "allow_exact_match": True,
        "allow_forward_join": False,
        "description": "Enforces publication availability lag before allowing join matching.",
        "enforces_zero_lookahead": True,
    },
]


def build_cross_asset_regime_asof_join_policy_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build asof join policy registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in ASOF_JOIN_POLICIES:
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
    summary = summarize_cross_asset_asof_join_policies(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def safe_cross_asset_asof_join_backward(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_on: str,
    right_on: str,
    by: Optional[str] = None,
    tolerance: Optional[str] = None,
) -> pd.DataFrame:
    """Safely perform backward-only asof join without mutating inputs or introducing lookahead."""
    left = left_df.copy()
    right = right_df.copy()

    if left.empty or right.empty:
        return left

    # Normalize timestamps to datetime UTC and sort
    left[left_on] = pd.to_datetime(left[left_on], errors="coerce", utc=True)
    right[right_on] = pd.to_datetime(right[right_on], errors="coerce", utc=True)

    left = left.sort_values(by=left_on).reset_index(drop=True)
    right = right.sort_values(by=right_on).reset_index(drop=True)

    # Perform pandas merge_asof with direction='backward' strictly
    join_kwargs: Dict[str, Any] = {
        "left_on": left_on,
        "right_on": right_on,
        "direction": "backward",
        "allow_exact_matches": True,
    }
    if by is not None and by in left.columns and by in right.columns:
        join_kwargs["by"] = by
    if tolerance is not None:
        join_kwargs["tolerance"] = pd.Timedelta(tolerance)

    joined = pd.merge_asof(left, right, **join_kwargs)

    # Ensure no forbidden output columns were introduced
    forbidden = [
        "signal", "buy", "sell", "long", "short", "position",
        "target", "label", "prediction", "recommendation",
        "future_return", "forward_return", "next_return",
    ]
    detected_forbidden = [c for c in joined.columns if any(f in c.lower() for f in forbidden)]
    if detected_forbidden:
        joined = joined.drop(columns=detected_forbidden)

    return joined


def summarize_cross_asset_asof_join_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize asof join policies."""
    return {
        "total_policies": len(df),
        "all_backward_direction": bool((df["direction"] == "backward").all()) if not df.empty else True,
        "zero_forward_allowed": bool((~df["allow_forward_join"]).all()) if not df.empty else True,
        "all_enforce_zero_lookahead": bool(df["enforces_zero_lookahead"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
    }
