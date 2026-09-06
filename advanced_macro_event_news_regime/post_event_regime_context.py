"""Phase 132: Post-Event Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_POST_EVENT_CONTEXTS = [
    {
        "post_event_id": "post_fomc_digestion",
        "event_id": "event_fomc_rate_decision",
        "buffer_minutes": 240,
        "absorption_tier": "extended_digestion_context",
        "volatility_expansion_flag": True,
        "description": "Post-FOMC statement and press conference market absorption window.",
    },
    {
        "post_event_id": "post_cpi_digestion",
        "event_id": "event_us_cpi_release",
        "buffer_minutes": 120,
        "absorption_tier": "rapid_absorption_context",
        "volatility_expansion_flag": True,
        "description": "Post-CPI inflation data digestion window.",
    },
    {
        "post_event_id": "post_nfp_digestion",
        "event_id": "event_us_nfp_actual",
        "buffer_minutes": 120,
        "absorption_tier": "rapid_absorption_context",
        "volatility_expansion_flag": True,
        "description": "Post-NFP employment release digestion window.",
    },
]


def build_post_event_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of post-event regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_POST_EVENT_CONTEXTS:
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
        "total_post_event_contexts": len(df),
        "mean_post_buffer_mins": float(df["buffer_minutes"].mean()) if "buffer_minutes" in df.columns else 0.0,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_post_event_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for post-event context."""
    return {
        "total_post_events": len(df),
        "absorption_tiers": df["absorption_tier"].nunique() if "absorption_tier" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
