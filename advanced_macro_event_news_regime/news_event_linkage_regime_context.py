"""Phase 132: News Event Linkage Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_EVENT_LINKAGES = [
    {
        "linkage_id": "link_fomc_news_event",
        "tag_id": "news_event_ref_fomc_statement",
        "event_id": "event_fomc_rate_decision",
        "linkage_type": "calendar_news_metadata_linkage",
        "correlation_tier": "direct_reference",
        "description": "Metadata linkage tying news items to FOMC interest rate decision events.",
    },
    {
        "linkage_id": "link_cpi_news_event",
        "tag_id": "news_topic_inflation",
        "event_id": "event_us_cpi_release",
        "linkage_type": "calendar_news_metadata_linkage",
        "correlation_tier": "direct_reference",
        "description": "Metadata linkage tying inflation news tags to US CPI scheduled releases.",
    },
]


def build_news_event_linkage_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of news-event linkage regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_EVENT_LINKAGES:
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
        "total_news_event_linkages": len(df),
        "strictly_metadata_only": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_news_event_linkage_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for news event linkage context."""
    return {
        "total_linkages": len(df),
        "events_linked": df["event_id"].nunique() if "event_id" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
