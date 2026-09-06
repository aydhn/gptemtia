"""Phase 132: News Freshness Regime Context Placeholders."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_FRESHNESS_PLACEHOLDERS = [
    {
        "placeholder_id": "freshness_fast_decay",
        "entity_id": "news_freshness_half_life_tracker",
        "window_tier": "breaking_news_tier",
        "half_life_hours": 6,
        "max_active_window_hours": 24,
        "decay_model_placeholder": "exponential_time_decay_placeholder",
        "description": "Temporal freshness decay placeholder for breaking economic release tags.",
    },
    {
        "placeholder_id": "freshness_medium_decay",
        "entity_id": "news_freshness_half_life_tracker",
        "window_tier": "thematic_cycle_tier",
        "half_life_hours": 24,
        "max_active_window_hours": 72,
        "decay_model_placeholder": "linear_time_decay_placeholder",
        "description": "Temporal decay placeholder for intermediate macro theme attention metadata.",
    },
]


def build_news_freshness_regime_context_placeholder_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of news freshness regime context placeholders."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_FRESHNESS_PLACEHOLDERS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["contains_full_article_text"] = False
        row["contains_article_body"] = False
        row["contains_raw_content"] = False
        row["contains_scraped_html"] = False
        row["contains_embedding"] = False
        row["contains_vector"] = False
        row["sentiment_model_output"] = False
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_freshness_placeholders": len(df),
        "strictly_metadata_only": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_news_freshness_regime_context_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for news freshness placeholders."""
    return {
        "total_placeholders": len(df),
        "mean_half_life": float(df["half_life_hours"].mean()) if "half_life_hours" in df.columns else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
