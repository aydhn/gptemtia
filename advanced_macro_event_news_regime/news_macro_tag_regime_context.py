"""Phase 132: News Macro Tag Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_MACRO_TAG_CONTEXTS = [
    {
        "macro_tag_context_id": "mtag_rate_cycle",
        "tag_id": "news_macro_tag_rate_hike_cut",
        "macro_theme": "monetary_policy_cycle",
        "scope": "global_macro",
        "linkage_type": "thematic_metadata",
        "description": "Rate hike/cut cycle thematic tag metadata context.",
    },
    {
        "macro_tag_context_id": "mtag_inflation_shock",
        "tag_id": "news_topic_inflation",
        "macro_theme": "inflation_regime_persistence",
        "scope": "global_macro",
        "linkage_type": "thematic_metadata",
        "description": "Inflation regime persistence tag metadata context.",
    },
]


def build_news_macro_tag_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of news macro tag regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_MACRO_TAG_CONTEXTS:
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
        "total_macro_tag_contexts": len(df),
        "macro_themes": df["macro_theme"].unique().tolist(),
        "strictly_metadata_only": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_news_macro_tag_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for news macro tag context."""
    return {
        "total_tags": len(df),
        "macro_themes": df["macro_theme"].nunique() if "macro_theme" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
