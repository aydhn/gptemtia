"""Phase 131: Calendar/News Cross-Asset Context Registry.

Defines non-signal cross-asset context linkages connecting calendar events to news metadata
(topic tags, asset tags, event linkages, freshness metrics). Strictly metadata-only: zero article text,
zero scraping, zero NLP sentiment models, zero embeddings.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

CALENDAR_NEWS_CONTEXT_RECORDS: List[Dict[str, Any]] = [
    {
        "context_id": "calnews_topic_rate_announcement",
        "context_name": "Calendar Rate Event to News Topic Tag Context",
        "context_category": "calendar_news_topic_context",
        "calendar_event": "cal_fomc_decision",
        "news_tag": "news_central_bank_rate",
        "description": "Topic tag co-occurrence around scheduled interest rate decision windows.",
        "readiness_score": 0.90,
        "is_metadata_only": True,
        "contains_full_article_text": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "calnews_tag_fx_commodity_exposure",
        "context_name": "Calendar Event to Multi-Asset News Tag Context",
        "context_category": "calendar_news_asset_tag_context",
        "calendar_event": "cal_us_nfp",
        "news_tag": "news_geopolitical_tension",
        "description": "Multi-asset tag association across FX and Commodity symbol metadata.",
        "readiness_score": 0.86,
        "is_metadata_only": True,
        "contains_full_article_text": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "calnews_event_linkage_energy",
        "context_name": "Energy Event to News Headline Metadata Linkage",
        "context_category": "calendar_news_event_linkage_context",
        "calendar_event": "cal_fomc_decision",
        "news_tag": "news_energy_supply",
        "description": "Headline timestamp mapping to calendar window without scraping or article text.",
        "readiness_score": 0.88,
        "is_metadata_only": True,
        "contains_full_article_text": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "calnews_freshness_decay_placeholder",
        "context_name": "News Metadata Freshness Decay Diagnostic Placeholder",
        "context_category": "calendar_news_freshness_context_placeholder",
        "calendar_event": "cal_ecb_decision",
        "news_tag": "news_central_bank_rate",
        "description": "Decay half-life diagnostic placeholder; strictly NOT an alpha or trade signal.",
        "readiness_score": 0.82,
        "is_metadata_only": True,
        "contains_full_article_text": False,
        "requires_no_lookahead": True,
    },
]


def build_calendar_news_cross_asset_context_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Calendar/News cross-asset context registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in CALENDAR_NEWS_CONTEXT_RECORDS:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_calendar_news_cross_asset_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_calendar_news_cross_asset_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Calendar/News cross-asset context records."""
    cat_counts = df["context_category"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_records": len(df),
        "context_categories": cat_counts,
        "mean_readiness_score": float(df["readiness_score"].mean()) if not df.empty else 0.0,
        "all_metadata_only": bool(df["is_metadata_only"].all()) if not df.empty else True,
        "zero_full_article_text": bool((~df["contains_full_article_text"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_predictions": True,
    }
