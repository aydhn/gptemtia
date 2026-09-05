"""Phase 126: News Metadata Regime Context Registry.

Registers metadata-only news attention, tag linkage, and freshness contexts.
Strictly prohibits full article text, scraping, embeddings, and sentiment models.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

NEWS_METADATA_CONTEXTS: List[Dict[str, Any]] = [
    {
        "context_id": "news_ctx_01_attention",
        "context_name": "news_topic_attention_context",
        "regime_family": "regime_family_news_metadata_context",
        "description": "Rolling volume of categorized news metadata headers without accessing body text",
        "metadata_fields": "news_volume_1h, news_volume_24h, topic_entropy",
        "contains_full_text": False,
        "contains_sentiment_model_output": False,
        "contains_embeddings": False,
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "news_ctx_02_asset_tag",
        "context_name": "news_asset_tag_context",
        "regime_family": "regime_family_news_metadata_context",
        "description": "Normalized asset ticker tag associations (e.g. XAU, WTI, USD) in news headers",
        "metadata_fields": "primary_asset_tag, secondary_asset_tag_count",
        "contains_full_text": False,
        "contains_sentiment_model_output": False,
        "contains_embeddings": False,
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "news_ctx_03_macro_tag",
        "context_name": "news_macro_tag_context",
        "regime_family": "regime_family_news_metadata_context",
        "description": "Macroeconomic categorization tags (central_bank, inflation, energy_supply) attached to headlines",
        "metadata_fields": "macro_topic_tag, topic_concentration_score",
        "contains_full_text": False,
        "contains_sentiment_model_output": False,
        "contains_embeddings": False,
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "news_ctx_04_linkage",
        "context_name": "news_event_linkage_context",
        "regime_family": "regime_family_news_metadata_context",
        "description": "Correlation between scheduled calendar event IDs and incoming headline metadata timestamps",
        "metadata_fields": "calendar_event_linkage_id, event_headline_delta_seconds",
        "contains_full_text": False,
        "contains_sentiment_model_output": False,
        "contains_embeddings": False,
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "news_ctx_05_freshness",
        "context_name": "news_freshness_context_placeholder",
        "regime_family": "regime_family_news_metadata_context",
        "description": "Placeholder measuring age of most recent metadata timestamp relative to current bar asof timestamp",
        "metadata_fields": "minutes_since_last_headline, headline_staleness_flag",
        "contains_full_text": False,
        "contains_sentiment_model_output": False,
        "contains_embeddings": False,
        "non_signal": True,
        "status": "regime_placeholder_only",
    },
]


def build_news_metadata_regime_context_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for news metadata regime context registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(NEWS_METADATA_CONTEXTS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_contexts": len(df),
        "regime_family": "regime_family_news_metadata_context",
        "all_metadata_only": bool(
            (df["contains_full_text"] == False).all()
            and (df["contains_sentiment_model_output"] == False).all()
            and (df["contains_embeddings"] == False).all()
        ),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_news_metadata_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize news metadata regime context DataFrame."""
    return {
        "total_contexts": len(df),
        "context_names": list(df["context_name"].unique()) if "context_name" in df.columns else [],
        "metadata_only": True,
        "non_signal": True,
    }
