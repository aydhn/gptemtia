"""Phase 132: News Metadata Regime Context Taxonomy (Strictly Metadata-Only)."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_NEWS_TAXONOMIES = [
    {
        "taxonomy_id": "news_tax_topic_attention",
        "taxonomy_name": "news_topic_attention_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Aggregated tag count/frequency context for major macro topics without sentiment.",
        "parent_category": "tag_attention",
    },
    {
        "taxonomy_id": "news_tax_asset_tag",
        "taxonomy_name": "news_asset_tag_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Tag linkage to specific commodity or currency asset identifiers.",
        "parent_category": "asset_tagging",
    },
    {
        "taxonomy_id": "news_tax_macro_tag",
        "taxonomy_name": "news_macro_tag_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Macro thematic tag metadata (e.g. monetary policy, fiscal policy, supply chain).",
        "parent_category": "macro_tagging",
    },
    {
        "taxonomy_id": "news_tax_event_linkage",
        "taxonomy_name": "news_event_linkage_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Association metadata linking news items to scheduled calendar release events.",
        "parent_category": "calendar_linkage",
    },
    {
        "taxonomy_id": "news_tax_freshness",
        "taxonomy_name": "news_freshness_placeholder_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Elapsed hours since news publication timestamp context.",
        "parent_category": "temporal_metadata",
    },
    {
        "taxonomy_id": "news_tax_coverage",
        "taxonomy_name": "news_metadata_coverage_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Metadata completeness diagnostics (presence of timestamp, source, tags).",
        "parent_category": "metadata_quality",
    },
    {
        "taxonomy_id": "news_tax_source",
        "taxonomy_name": "source_metadata_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Provider and publisher provenance metadata attribution.",
        "parent_category": "provenance_metadata",
    },
    {
        "taxonomy_id": "news_tax_language",
        "taxonomy_name": "language_metadata_context",
        "domain": "news_metadata_context_taxonomy_domain",
        "description": "Language ISO classification metadata.",
        "parent_category": "linguistic_metadata",
    },
]


def build_news_metadata_regime_context_taxonomy_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build taxonomy registry DataFrame for news metadata regime context."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_NEWS_TAXONOMIES:
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
        "total_news_taxonomies": len(df),
        "domains": df["domain"].unique().tolist(),
        "strictly_metadata_only": True,
        "zero_article_text": True,
        "zero_sentiment": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_news_metadata_regime_context_taxonomy(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for news metadata context taxonomy."""
    return {
        "total_taxonomies": len(df),
        "parent_categories": df["parent_category"].nunique() if "parent_category" in df.columns else 0,
        "zero_article_text": not bool(df["contains_full_article_text"].any()) if "contains_full_article_text" in df.columns else True,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
