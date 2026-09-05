from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


NEWS_METADATA_LINEAGE_ITEMS = [
    {
        "lineage_item_id": "news_lin_meta_only",
        "domain": "news_metadata_lineage_domain",
        "provider_profile": "balanced_no_scraping_news_metadata_provider",
        "raw_field": "headline, source_name, published_at",
        "canonical_field": "normalized_news_metadata",
        "schema_ref": "canonical://schema/news_metadata_canonical_v1",
        "policy_enforcement": "metadata_only_boundary_preservation",
        "copyright_boundary_status": "lineage_complete",
        "contains_full_text": False,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Strictly metadata only: zero article body, zero scraped content",
    },
    {
        "lineage_item_id": "news_lin_tags_norm",
        "domain": "news_metadata_lineage_domain",
        "provider_profile": "balanced_no_scraping_news_metadata_provider",
        "raw_field": "tags",
        "canonical_field": "normalized_tags",
        "schema_ref": "canonical://schema/news_metadata_canonical_v1",
        "policy_enforcement": "news_topic_tag_normalization_enforcement",
        "copyright_boundary_status": "lineage_complete",
        "contains_full_text": False,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Taxonomy standardization ('CENTRAL_BANK', 'CRUDE_OIL', 'INFLATION'); raw tags kept",
    },
    {
        "lineage_item_id": "news_lin_event_linkage",
        "domain": "news_metadata_lineage_domain",
        "provider_profile": "balanced_no_scraping_news_metadata_provider",
        "raw_field": "event_reference_id",
        "canonical_field": "canonical_event_linkage",
        "schema_ref": "canonical://schema/news_item_reference_v1",
        "policy_enforcement": "event_linkage_provenance",
        "copyright_boundary_status": "lineage_complete",
        "contains_full_text": False,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Linkage to economic calendar / macro release identifier; zero sentiment as signal",
    },
]


def build_news_metadata_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(NEWS_METADATA_LINEAGE_ITEMS)
    summary = summarize_news_metadata_lineage_registry(df)
    return df, summary


def summarize_news_metadata_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_news_metadata_lineage_items": len(df),
        "canonical_fields": df["canonical_field"].tolist() if "canonical_field" in df.columns else [],
        "zero_full_text": bool((~df["contains_full_text"]).all()) if "contains_full_text" in df.columns and len(df) > 0 else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
