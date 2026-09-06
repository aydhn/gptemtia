"""Phase 132: News Metadata Regime Entity Registry (Strictly Metadata-Only)."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_NEWS_METADATA_ENTITIES = [
    {
        "entity_id": "news_topic_inflation",
        "entity_name": "Inflation & CPI News Topic Tag",
        "entity_type": "news_topic_tag",
        "tag_category": "topic",
        "source_system": "metadata_feed",
        "freshness_window_hours": 24,
    },
    {
        "entity_id": "news_topic_central_banks",
        "entity_name": "Central Bank & Policy News Topic Tag",
        "entity_type": "news_topic_tag",
        "tag_category": "topic",
        "source_system": "metadata_feed",
        "freshness_window_hours": 48,
    },
    {
        "entity_id": "news_asset_tag_gold",
        "entity_name": "Gold / Precious Metals Asset Tag",
        "entity_type": "news_asset_tag",
        "tag_category": "commodity",
        "source_system": "metadata_feed",
        "freshness_window_hours": 24,
    },
    {
        "entity_id": "news_asset_tag_brent",
        "entity_name": "Brent Crude Energy Asset Tag",
        "entity_type": "news_asset_tag",
        "tag_category": "commodity",
        "source_system": "metadata_feed",
        "freshness_window_hours": 24,
    },
    {
        "entity_id": "news_asset_tag_eurusd",
        "entity_name": "EURUSD Forex Major Asset Tag",
        "entity_type": "news_asset_tag",
        "tag_category": "forex",
        "source_system": "metadata_feed",
        "freshness_window_hours": 24,
    },
    {
        "entity_id": "news_macro_tag_rate_hike_cut",
        "entity_name": "Interest Rate Path Macro Tag",
        "entity_type": "news_macro_tag",
        "tag_category": "macro_theme",
        "source_system": "metadata_feed",
        "freshness_window_hours": 72,
    },
    {
        "entity_id": "news_event_ref_fomc_statement",
        "entity_name": "FOMC Statement Calendar Reference Tag",
        "entity_type": "news_event_reference",
        "tag_category": "calendar_link",
        "source_system": "calendar_news_bridge",
        "freshness_window_hours": 12,
    },
    {
        "entity_id": "news_source_wire_financial_press",
        "entity_name": "Financial Press & Wire Source Metadata",
        "entity_type": "news_source_metadata",
        "tag_category": "source_provenance",
        "source_system": "metadata_registry",
        "freshness_window_hours": 168,
    },
    {
        "entity_id": "news_timestamp_published_at_utc",
        "entity_name": "News Published UTC Timestamp Metadata",
        "entity_type": "news_timestamp_metadata",
        "tag_category": "time_alignment",
        "source_system": "timestamp_normalizer",
        "freshness_window_hours": 0,
    },
    {
        "entity_id": "news_freshness_half_life_tracker",
        "entity_name": "News Attention Freshness Half-Life Placeholder",
        "entity_type": "news_freshness_placeholder",
        "tag_category": "freshness",
        "source_system": "decay_estimator",
        "freshness_window_hours": 48,
    },
    {
        "entity_id": "news_language_iso_code_tag",
        "entity_name": "News Language ISO Metadata Tag",
        "entity_type": "news_language_metadata",
        "tag_category": "language",
        "source_system": "metadata_registry",
        "freshness_window_hours": 720,
    },
]


def build_news_metadata_regime_entity_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of metadata-only news regime entities."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_NEWS_METADATA_ENTITIES:
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
        "total_news_metadata_entities": len(df),
        "entity_types": df["entity_type"].unique().tolist(),
        "strictly_metadata_only": True,
        "zero_article_text": True,
        "zero_sentiment": True,
        "zero_embeddings": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_news_metadata_regime_entities(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for news metadata regime entities."""
    return {
        "total_news_metadata_entities": len(df),
        "entity_types": df["entity_type"].nunique() if "entity_type" in df.columns else 0,
        "zero_article_text": not bool(df["contains_full_article_text"].any()) if "contains_full_article_text" in df.columns else True,
        "zero_sentiment": not bool(df["sentiment_model_output"].any()) if "sentiment_model_output" in df.columns else True,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
