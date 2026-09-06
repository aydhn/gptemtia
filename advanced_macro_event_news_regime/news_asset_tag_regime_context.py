"""Phase 132: News Asset Tag Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_ASSET_TAG_CONTEXTS = [
    {
        "asset_tag_context_id": "tag_ctx_gold",
        "asset_symbol": "XAUUSD",
        "asset_class": "precious_metals",
        "tag_id": "news_asset_tag_gold",
        "relevance_level": "direct",
        "description": "Gold metadata tag context mapping to XAUUSD regime dataset.",
    },
    {
        "asset_tag_context_id": "tag_ctx_brent",
        "asset_symbol": "BRENT",
        "asset_class": "energy",
        "tag_id": "news_asset_tag_brent",
        "relevance_level": "direct",
        "description": "Crude oil metadata tag context mapping to BRENT regime dataset.",
    },
    {
        "asset_tag_context_id": "tag_ctx_eurusd",
        "asset_symbol": "EURUSD",
        "asset_class": "forex",
        "tag_id": "news_asset_tag_eurusd",
        "relevance_level": "direct",
        "description": "Euro/Dollar metadata tag context mapping to EURUSD regime dataset.",
    },
]


def build_news_asset_tag_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of news asset tag regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_ASSET_TAG_CONTEXTS:
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
        "total_asset_tag_contexts": len(df),
        "asset_classes": df["asset_class"].unique().tolist(),
        "strictly_metadata_only": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_news_asset_tag_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for news asset tag context."""
    return {
        "total_tags": len(df),
        "asset_symbols": df["asset_symbol"].nunique() if "asset_symbol" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
