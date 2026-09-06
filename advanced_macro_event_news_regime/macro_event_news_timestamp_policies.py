"""Phase 132: Macro/Event/News Timestamp Policies (Strict Lookahead Prevention)."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_TIMESTAMP_POLICIES = [
    {
        "policy_id": "policy_backward_timestamp_only",
        "policy_name": "Backward-Only Historical Timestamp Policy",
        "direction": "backward",
        "allow_future_timestamp": False,
        "allow_nearest_future": False,
        "description": "Ensures context data timestamp is strictly <= observation base timestamp.",
    },
    {
        "policy_id": "policy_scheduled_actual_alignment",
        "policy_name": "Scheduled vs Actual Availability Alignment Policy",
        "direction": "backward",
        "allow_future_timestamp": False,
        "allow_nearest_future": False,
        "description": "Enforces that release context is only known after actual release timestamp.",
    },
    {
        "policy_id": "policy_published_at_utc_only",
        "policy_name": "Published-At UTC News Timestamp Policy",
        "direction": "backward",
        "allow_future_timestamp": False,
        "allow_nearest_future": False,
        "description": "Ensures news metadata is only joined as of published_at_utc.",
    },
]


def build_macro_event_news_timestamp_policy_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of timestamp alignment policies."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_TIMESTAMP_POLICIES:
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
        "total_timestamp_policies": len(df),
        "all_backward_only": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def validate_macro_event_news_context_timestamp_not_future(
    df: pd.DataFrame,
    base_ts: str,
    context_ts: str,
) -> Dict[str, Any]:
    """Validate that context timestamp is strictly <= base price observation timestamp."""
    if df.empty or base_ts not in df.columns or context_ts not in df.columns:
        return {
            "valid": False,
            "error": "Required timestamp columns not found or DataFrame empty",
            "future_leakage_detected": True,
        }

    base = pd.to_datetime(df[base_ts], errors="coerce")
    ctx = pd.to_datetime(df[context_ts], errors="coerce")

    future_count = int((ctx > base).sum())
    is_valid = (future_count == 0)

    return {
        "valid": is_valid,
        "total_rows": len(df),
        "future_leak_count": future_count,
        "future_leakage_detected": not is_valid,
        "status": "PASS" if is_valid else "FAIL_FUTURE_TIMESTAMP_DETECTED",
    }


def summarize_macro_event_news_timestamp_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for timestamp policy registry."""
    return {
        "total_policies": len(df),
        "all_backward": bool((df["direction"] == "backward").all()) if "direction" in df.columns else False,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
