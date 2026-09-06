"""Phase 132: Macro/Event/News Asof Join Policies (Guaranteed Backward-Only)."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_ASOF_POLICIES = [
    {
        "asof_policy_id": "asof_backward_join_policy",
        "direction": "backward",
        "allow_forward": False,
        "allow_nearest": False,
        "allow_exact_match": True,
        "description": "Strictly merges right-side context on <= left-side timestamp to eliminate lookahead.",
    }
]


def build_macro_event_news_asof_join_policy_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of asof join policies."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_ASOF_POLICIES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_asof_policies": len(df),
        "direction": "backward",
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def safe_macro_event_news_asof_join_backward(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_on: str,
    right_on: str,
    by: Optional[str] = None,
    tolerance: Optional[str] = None,
) -> pd.DataFrame:
    """Perform a strictly backward-only asof join without mutating inputs."""
    if left_df.empty:
        return left_df.copy()
    if right_df.empty:
        return left_df.copy()

    # Deep copy to preserve input DataFrames
    l_copy = left_df.copy()
    r_copy = right_df.copy()

    # Ensure datetime sorting for pd.merge_asof
    l_copy[left_on] = pd.to_datetime(l_copy[left_on])
    r_copy[right_on] = pd.to_datetime(r_copy[right_on])

    l_sorted = l_copy.sort_values(left_on)
    r_sorted = r_copy.sort_values(right_on)

    kwargs: Dict[str, Any] = {
        "left_on": left_on,
        "right_on": right_on,
        "direction": "backward",
        "allow_exact_matches": True,
    }
    if by and by in l_sorted.columns and by in r_sorted.columns:
        kwargs["by"] = by
    if tolerance:
        kwargs["tolerance"] = pd.Timedelta(tolerance)

    result = pd.merge_asof(l_sorted, r_sorted, **kwargs)
    return result


def summarize_macro_event_news_asof_join_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for asof join policy registry."""
    return {
        "total_policies": len(df),
        "direction": df["direction"].iloc[0] if not df.empty else "unknown",
        "allow_forward": bool(df["allow_forward"].any()) if "allow_forward" in df.columns else False,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
