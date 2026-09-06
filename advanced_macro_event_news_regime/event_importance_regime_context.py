"""Phase 132: Event Importance Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_IMPORTANCE_CONTEXTS = [
    {
        "importance_tier": "critical",
        "description": "Systemic central bank policy rate decisions and major geopolitical emergency statements.",
        "weight_rank": 4,
        "requires_pre_buffer": True,
        "requires_post_buffer": True,
        "min_buffer_mins": 120,
    },
    {
        "importance_tier": "high",
        "description": "Primary economic indicators (CPI, NFP, GDP, key PMIs) driving major asset repricing.",
        "weight_rank": 3,
        "requires_pre_buffer": True,
        "requires_post_buffer": True,
        "min_buffer_mins": 60,
    },
    {
        "importance_tier": "medium",
        "description": "Secondary tier macro data (Retail Sales, PPI, Consumer Sentiment surveys).",
        "weight_rank": 2,
        "requires_pre_buffer": False,
        "requires_post_buffer": True,
        "min_buffer_mins": 30,
    },
    {
        "importance_tier": "low",
        "description": "Tertiary economic indicators and routine statistical releases.",
        "weight_rank": 1,
        "requires_pre_buffer": False,
        "requires_post_buffer": False,
        "min_buffer_mins": 0,
    },
]


def build_event_importance_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of event importance regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_IMPORTANCE_CONTEXTS:
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
        "total_importance_tiers": len(df),
        "tiers": df["importance_tier"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_event_importance_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for event importance context."""
    return {
        "total_tiers": len(df),
        "highest_tier": df["importance_tier"].iloc[0] if not df.empty else "none",
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
