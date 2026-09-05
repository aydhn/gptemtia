"""Phase 122 News Attention Factor Families Registry.

Defines metadata-only headline topic counts, asset tag frequencies, and linkage indicators.
Strictly non-signal, zero article body text, zero scraping, and zero NLP model sentiment.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import (
    FACTOR_PLACEHOLDER_ONLY,
    FACTOR_READY,
)

NEWS_ATTENTION_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_news_topic_attention_context",
        "factor_family": "news_attention",
        "input_features": ["fusion__news_topic_attention_count"],
        "calculation_type": "topic_category_frequency_counter",
        "non_signal_usage": "Counts published headlines under relevant macro/commodity topics. Zero text NLP.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_asset_tag_attention_context",
        "factor_family": "news_attention",
        "input_features": ["fusion__news_asset_tag_count"],
        "calculation_type": "entity_tag_frequency_counter",
        "non_signal_usage": "Counts direct asset entity tags (e.g. GOLD, OIL, USDTRY) in metadata feed.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_macro_tag_attention_context",
        "factor_family": "news_attention",
        "input_features": ["fusion__news_macro_tag_count"],
        "calculation_type": "macro_tag_frequency_counter",
        "non_signal_usage": "Counts macroeconomic tag occurrences (e.g. FED, CBRT, CPI, RATES).",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_event_linkage_context",
        "factor_family": "news_attention",
        "input_features": ["fusion__news_event_linkage_flag"],
        "calculation_type": "binary_event_news_overlap_flag",
        "non_signal_usage": "Flag indicating headline is explicitly tied to scheduled calendar event.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_freshness_placeholder_context",
        "factor_family": "news_attention",
        "input_features": ["fusion__news_freshness_decay"],
        "calculation_type": "exponential_time_decay_weight",
        "non_signal_usage": "Time elapsed since last headline metadata item placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_news_attention_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build News Attention Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in NEWS_ATTENTION_FACTOR_METADATA]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_factors": len(records),
        "ready_factors": sum(1 for r in records if r["status_label"] == FACTOR_READY),
        "placeholder_factors": sum(1 for r in records if r["status_label"] == FACTOR_PLACEHOLDER_ONLY),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "metadata_only_verified": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_news_attention_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize news attention factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "metadata_only": True,
        "non_signal": True,
    }
