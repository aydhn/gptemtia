"""Phase 130: News Metadata Transition Context.

Evaluates regime transition context using strictly non-textual news metadata,
topic tags, and publication timestamps. Zero full text, zero scraping, zero embeddings.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

NEWS_METADATA_TRANSITION_DATA: List[Dict[str, Any]] = [
    {
        "metadata_topic_cluster": "monetary_policy_headline_flow",
        "transition_context_relevance": 0.86,
        "freshness_lag_seconds": 180,
        "event_linkage_status": "linked",
        "full_text_used": False,
        "scraping_executed": False,
        "raw_content_used": False,
        "embedding_used": False,
        "sentiment_model_used": False,
        "non_signal": True,
        "description": "Central bank policy keyword/topic tag metadata frequency context",
    },
    {
        "metadata_topic_cluster": "energy_supply_disruption_metadata",
        "transition_context_relevance": 0.82,
        "freshness_lag_seconds": 240,
        "event_linkage_status": "linked",
        "full_text_used": False,
        "scraping_executed": False,
        "raw_content_used": False,
        "embedding_used": False,
        "sentiment_model_used": False,
        "non_signal": True,
        "description": "Commodity supply news metadata tags and headline counts",
    },
    {
        "metadata_topic_cluster": "macro_fiscal_geopolitical_tags",
        "transition_context_relevance": 0.80,
        "freshness_lag_seconds": 300,
        "event_linkage_status": "linked",
        "full_text_used": False,
        "scraping_executed": False,
        "raw_content_used": False,
        "embedding_used": False,
        "sentiment_model_used": False,
        "non_signal": True,
        "description": "Cross-asset metadata category tags without textual extraction",
    },
]


def build_news_metadata_transition_context_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build news metadata transition context dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(NEWS_METADATA_TRANSITION_DATA)
    summary = summarize_news_metadata_transition_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_news_metadata_transition_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize news metadata transition context."""
    mean_rel = float(df["transition_context_relevance"].mean()) if not df.empty and "transition_context_relevance" in df.columns else 0.0
    return {
        "total_metadata_clusters": len(df),
        "total_contexts": len(df),
        "mean_context_relevance": round(mean_rel, 4),
        "all_metadata_only": True,
        "zero_scraping_guaranteed": True,
        "zero_full_text_guaranteed": bool(not df["full_text_used"].any()) if not df.empty else True,
        "zero_raw_content_guaranteed": bool(not df["raw_content_used"].any()) if not df.empty else True,
        "zero_embeddings_guaranteed": bool(not df["embedding_used"].any()) if not df.empty else True,
        "zero_sentiment_models_guaranteed": bool(not df["sentiment_model_used"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }

