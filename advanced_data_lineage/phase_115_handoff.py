from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


HANDOFF_ITEMS = [
    {
        "benchmark_area": "Provider capability benchmark inputs",
        "provider_or_dataset": "advanced_data_providers_abstraction",
        "required_lineage_input": "provider_provenance_registry",
        "quality_input": "provider_metadata_quality_rules",
        "normalization_input": "provider_name_normalization",
        "traceability_input": "provider_traceability_score",
        "comparison_note": "Multi-provider abstraction ready for capability scoring matrix in Phase 115",
        "manual_review_required": False,
    },
    {
        "benchmark_area": "Provider coverage benchmark inputs",
        "provider_or_dataset": "advanced_fx_providers_engine",
        "required_lineage_input": "fx_lineage_registry",
        "quality_input": "fx_quote_sanity_rule",
        "normalization_input": "fx_symbol_normalization_enforcement",
        "traceability_input": "dataset_traceability_score",
        "comparison_note": "Major/minor/exotic FX pair coverage baseline ready for benchmark",
        "manual_review_required": False,
    },
    {
        "benchmark_area": "Quality score benchmark inputs",
        "provider_or_dataset": "advanced_commodity_providers_engine",
        "required_lineage_input": "commodity_lineage_registry",
        "quality_input": "commodity_quality_rules",
        "normalization_input": "commodity_symbol_normalization_enforcement",
        "traceability_input": "dataset_traceability_score",
        "comparison_note": "Spot and futures contract metadata sanity inputs ready for benchmark",
        "manual_review_required": False,
    },
    {
        "benchmark_area": "Normalization score benchmark inputs",
        "provider_or_dataset": "advanced_macro_providers_engine",
        "required_lineage_input": "macro_lineage_registry",
        "quality_input": "macro_quality_rules",
        "normalization_input": "macro_indicator_normalization_enforcement",
        "traceability_input": "provider_traceability_score",
        "comparison_note": "Macro indicator frequency/unit normalization inputs ready for benchmark",
        "manual_review_required": False,
    },
    {
        "benchmark_area": "Traceability score benchmark inputs",
        "provider_or_dataset": "advanced_economic_calendar_engine",
        "required_lineage_input": "calendar_lineage_registry",
        "quality_input": "calendar_quality_rules",
        "normalization_input": "calendar_event_normalization_enforcement",
        "traceability_input": "provider_traceability_score",
        "comparison_note": "Economic calendar scheduled vs actual release traceability ready",
        "manual_review_required": False,
    },
    {
        "benchmark_area": "License/provenance benchmark inputs",
        "provider_or_dataset": "licensed_vendor_provider_placeholder",
        "required_lineage_input": "license_provenance_registry",
        "quality_input": "provider_metadata_quality_rules",
        "normalization_input": "schema_version_normalization",
        "traceability_input": "provider_traceability_score",
        "comparison_note": "Vendor licensing constraints and redistribution boundaries ready",
        "manual_review_required": True,
    },
    {
        "benchmark_area": "Metadata-only compliance benchmark inputs",
        "provider_or_dataset": "advanced_news_metadata_engine",
        "required_lineage_input": "news_metadata_lineage_registry",
        "quality_input": "news_copyright_quality_rules",
        "normalization_input": "news_topic_tag_normalization_enforcement",
        "traceability_input": "provider_traceability_score",
        "comparison_note": "Zero full text and metadata-only compliance verified for benchmark",
        "manual_review_required": False,
    },
    {
        "benchmark_area": "Cross-domain provider comparison inputs",
        "provider_or_dataset": "all_domain_providers",
        "required_lineage_input": "cross_domain_provenance_map",
        "quality_input": "dataset_quality_scoring",
        "normalization_input": "cross_domain_mapping_report",
        "traceability_input": "traceability_score_report",
        "comparison_note": "Cross-asset linkage and traceability metrics consolidated for Phase 115",
        "manual_review_required": False,
    },
    {
        "benchmark_area": "Dry-run provider benchmark rehearsal",
        "provider_or_dataset": "all_dry_run_fixtures",
        "required_lineage_input": "provenance_source_registry",
        "quality_input": "data_quality_pipeline",
        "normalization_input": "data_normalization_pipeline",
        "traceability_input": "data_lineage_pipeline",
        "comparison_note": "Deterministic offline mock datasets ready for comparative evaluation",
        "manual_review_required": False,
    },
]


def build_phase_115_provider_benchmark_handoff_report(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(HANDOFF_ITEMS)
    summary = summarize_phase_115_handoff(df)
    return df, summary


def summarize_phase_115_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_handoff_items": len(df),
        "benchmark_areas": df["benchmark_area"].tolist() if "benchmark_area" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_phase": 115,
        "target_phase_name": "Data Provider Benchmark Report",
        "target_final_phase": 160,
    }
