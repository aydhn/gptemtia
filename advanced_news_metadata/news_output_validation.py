import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_default_news_output_validation_rules(profile: NewsProviderProfile) -> pd.DataFrame:
    rules = [
        {
            "rule_id": "val_rule_missing_metadata",
            "target_schema": "news_metadata_schema",
            "field_name": "item_id, timestamp, source_name",
            "rule_description": "Ensure required identifiers and timestamps are present and non-empty.",
            "severity": "CRITICAL",
            "future_phase_owner": "Phase 112 Data Quality Engine",
            "manual_review_required": False
        },
        {
            "rule_id": "val_rule_metadata_only_boundary",
            "target_schema": "news_metadata_schema",
            "field_name": "metadata_only",
            "rule_description": "Affirm that metadata_only is True and raw article text is absent.",
            "severity": "CRITICAL",
            "future_phase_owner": "Phase 112 Data Quality Engine",
            "manual_review_required": False
        },
        {
            "rule_id": "val_rule_duplicate_item",
            "target_schema": "news_item_reference_schema",
            "field_name": "item_id, content_hash_placeholder",
            "rule_description": "Identify and flag duplicate news entries based on item IDs and hashes.",
            "severity": "HIGH",
            "future_phase_owner": "Phase 112 Data Quality Engine",
            "manual_review_required": True
        },
        {
            "rule_id": "val_rule_stale_news",
            "target_schema": "news_metadata_schema",
            "field_name": "timestamp",
            "rule_description": "Evaluate publication timestamp against freshness thresholds.",
            "severity": "MEDIUM",
            "future_phase_owner": "Phase 112 Data Quality Engine",
            "manual_review_required": False
        },
        {
            "rule_id": "val_rule_topic_tag_normalization",
            "target_schema": "news_metadata_schema",
            "field_name": "topic_tags, asset_tags",
            "rule_description": "Validate tags against canonical taxonomy registries.",
            "severity": "MEDIUM",
            "future_phase_owner": "Phase 113 Data Normalization Layer",
            "manual_review_required": False
        },
        {
            "rule_id": "val_rule_source_lineage_provenance",
            "target_schema": "news_metadata_schema",
            "field_name": "source_name, provider_name",
            "rule_description": "Trace source origin, retrieval mode, and compliance trail.",
            "severity": "HIGH",
            "future_phase_owner": "Phase 114 Data Lineage and Provenance",
            "manual_review_required": True
        },
        {
            "rule_id": "val_rule_provider_coverage_benchmark",
            "target_schema": "news_provider_capability",
            "field_name": "topic_support, region_support",
            "rule_description": "Benchmark coverage breadth and latency across registered providers.",
            "severity": "INFO",
            "future_phase_owner": "Phase 115 Data Provider Benchmark Report",
            "manual_review_required": False
        }
    ]
    return pd.DataFrame(rules)

def build_news_output_validation_contract(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_news_output_validation_rules(profile)
    summary = summarize_news_output_validation(df)
    return df, summary

def summarize_news_output_validation(df: pd.DataFrame) -> Dict:
    return {
        "total_rules": len(df),
        "critical_rules": len(df[df["severity"] == "CRITICAL"]) if not df.empty else 0
    }
