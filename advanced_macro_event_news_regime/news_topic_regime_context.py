"""Phase 132: News Topic Regime Context Registry (Metadata-Only)."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_NEWS_TOPIC_CONTEXTS = [
    {
        "topic_context_id": "topic_ctx_inflation",
        "topic_name": "Inflation & Prices",
        "tag_id": "news_topic_inflation",
        "attention_tier": "high_coverage_context",
        "frequency_window": "24h",
        "description": "Tag frequency for inflation theme metadata without text or sentiment.",
    },
    {
        "topic_context_id": "topic_ctx_monetary_policy",
        "topic_name": "Central Bank Policy",
        "tag_id": "news_topic_central_banks",
        "attention_tier": "critical_coverage_context",
        "frequency_window": "48h",
        "description": "Tag frequency for monetary policy theme metadata.",
    },
    {
        "topic_context_id": "topic_ctx_energy_markets",
        "topic_name": "Energy Markets & OPEC",
        "tag_id": "news_asset_tag_brent",
        "attention_tier": "high_coverage_context",
        "frequency_window": "24h",
        "description": "Tag frequency for energy markets theme metadata.",
    },
]


def build_news_topic_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of news topic regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_NEWS_TOPIC_CONTEXTS:
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
        "total_topic_contexts": len(df),
        "strictly_metadata_only": True,
        "zero_sentiment": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_news_topic_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for news topic context."""
    return {
        "total_topics": len(df),
        "zero_article_text": not bool(df["contains_full_article_text"].any()) if "contains_full_article_text" in df.columns else True,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
