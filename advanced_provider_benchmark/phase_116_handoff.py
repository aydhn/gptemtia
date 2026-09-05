from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile

HANDOFF_ITEMS = [
    {
        "feature_engine_input_area": "FX Technical Indicators & Return Features",
        "source_provider_domain": "provider_domain_fx",
        "required_benchmark_input": "fx_provider_benchmark_report",
        "quality_dependency": "fx_quote_sanity_and_spread_validation",
        "normalization_dependency": "fx_symbol_uppercase_canonical_mapping",
        "lineage_dependency": "fx_lineage_transformation_audit",
        "recommended_feature_readiness_note": "Canonical OHLCV ready for RSI, MACD, ATR and log returns computation in Phase 116",
        "manual_review_required": False,
    },
    {
        "feature_engine_input_area": "Commodity Momentum & Term Structure Features",
        "source_provider_domain": "provider_domain_commodity",
        "required_benchmark_input": "commodity_provider_benchmark_report",
        "quality_dependency": "commodity_outlier_filtering_and_bounds",
        "normalization_dependency": "commodity_unit_normalization_enforcement",
        "lineage_dependency": "commodity_lineage_registry",
        "recommended_feature_readiness_note": "Spot and futures metadata ready for roll yield and term-structure slope factors in Phase 116",
        "manual_review_required": False,
    },
    {
        "feature_engine_input_area": "Macroeconomic Regime & Policy Factors",
        "source_provider_domain": "provider_domain_macro",
        "required_benchmark_input": "macro_provider_benchmark_report",
        "quality_dependency": "macro_frequency_and_revision_integrity",
        "normalization_dependency": "macro_indicator_standard_vocabulary",
        "lineage_dependency": "macro_source_agency_lineage",
        "recommended_feature_readiness_note": "Macro time series ready for YoY inflation drift and policy rate differential features in Phase 116",
        "manual_review_required": False,
    },
    {
        "feature_engine_input_area": "Economic Calendar Event & Surprise Features",
        "source_provider_domain": "provider_domain_calendar",
        "required_benchmark_input": "calendar_provider_benchmark_report",
        "quality_dependency": "calendar_consensus_surprise_precision",
        "normalization_dependency": "calendar_event_taxonomy_normalization",
        "lineage_dependency": "calendar_event_schedule_lineage",
        "recommended_feature_readiness_note": "Standardized release timestamps ready for event-window volatility spike features in Phase 116",
        "manual_review_required": False,
    },
    {
        "feature_engine_input_area": "News Sentiment & Topic Impact Placeholders",
        "source_provider_domain": "provider_domain_news_metadata",
        "required_benchmark_input": "news_metadata_provider_benchmark_report",
        "quality_dependency": "news_spam_and_duplicate_filtering",
        "normalization_dependency": "news_tag_taxonomy_and_asset_linking",
        "lineage_dependency": "news_metadata_only_provenance",
        "recommended_feature_readiness_note": "Asset-linked metadata ready for topic frequency and headline shock placeholders (zero full text)",
        "manual_review_required": False,
    },
    {
        "feature_engine_input_area": "Diagnostic Quality & Traceability Feature Filters",
        "source_provider_domain": "provider_domain_cross_domain",
        "required_benchmark_input": "provider_benchmark_score_report",
        "quality_dependency": "dataset_quality_scoring_report",
        "normalization_dependency": "normalization_scoring_report",
        "lineage_dependency": "traceability_scoring_report",
        "recommended_feature_readiness_note": "Missing/stale/outlier flags serve as masking filters to prevent noisy factor computation",
        "manual_review_required": False,
    },
    {
        "feature_engine_input_area": "Manual Review Prerequisite Gate",
        "source_provider_domain": "provider_domain_cross_domain",
        "required_benchmark_input": "provider_benchmark_manual_review_queue",
        "quality_dependency": "manual_review_backlog_audit",
        "normalization_dependency": "custom_schema_mapping_review",
        "lineage_dependency": "unresolved_lineage_finding_review",
        "recommended_feature_readiness_note": "Critical vendor or unmapped custom schemas require operational sign-off before factor inclusion",
        "manual_review_required": True,
    },
]


def build_phase_116_indicator_feature_factor_engine_handoff_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(HANDOFF_ITEMS)
    summary = summarize_phase_116_handoff(df)
    return df, summary


def summarize_phase_116_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_handoff_items": len(df),
        "readiness_status": "READY",
        "target_phase": 116,
        "target_phase_name": "Advanced Indicator/Feature/Factor Engine",
        "manual_review_required_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "disclaimer": "This handoff specifies data readiness prerequisites only; it does NOT generate indicators, features, signals, or trading advice.",
        "current_phase": 115,
        "target_final_phase": 160,
    }
