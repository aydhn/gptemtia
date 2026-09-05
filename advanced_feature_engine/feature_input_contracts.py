from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureInputContract,
    build_feature_input_contract_id,
)

DEFAULT_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "dataset_type": "dataset_fx_ohlcv",
        "required_fields": ["timestamp", "symbol", "open", "high", "low", "close"],
        "optional_fields": ["volume", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "symbol",
        "provider_field": "provider",
        "quality_dependency": "fx_quote_sanity_and_spread_validation",
        "normalization_dependency": "fx_symbol_uppercase_canonical_mapping",
        "lineage_dependency": "fx_lineage_transformation_audit",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_fx_quote",
        "required_fields": ["timestamp", "symbol", "bid", "ask"],
        "optional_fields": ["spread", "mid", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "symbol",
        "provider_field": "provider",
        "quality_dependency": "fx_quote_sanity_and_spread_validation",
        "normalization_dependency": "fx_symbol_uppercase_canonical_mapping",
        "lineage_dependency": "fx_lineage_transformation_audit",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_commodity_ohlcv",
        "required_fields": ["timestamp", "symbol", "open", "high", "low", "close"],
        "optional_fields": ["volume", "open_interest", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "symbol",
        "provider_field": "provider",
        "quality_dependency": "commodity_outlier_filtering_and_bounds",
        "normalization_dependency": "commodity_unit_normalization_enforcement",
        "lineage_dependency": "commodity_lineage_registry",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_commodity_spot",
        "required_fields": ["timestamp", "symbol", "spot_price"],
        "optional_fields": ["unit", "currency", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "symbol",
        "provider_field": "provider",
        "quality_dependency": "commodity_outlier_filtering_and_bounds",
        "normalization_dependency": "commodity_unit_normalization_enforcement",
        "lineage_dependency": "commodity_lineage_registry",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_macro_timeseries",
        "required_fields": ["timestamp", "indicator_id", "value"],
        "optional_fields": ["frequency", "revision_flag", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "indicator_id",
        "provider_field": "provider",
        "quality_dependency": "macro_frequency_and_revision_integrity",
        "normalization_dependency": "macro_indicator_standard_vocabulary",
        "lineage_dependency": "macro_source_agency_lineage",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_calendar_event",
        "required_fields": ["timestamp", "event_id", "actual", "consensus"],
        "optional_fields": ["previous", "surprise", "impact", "country", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "event_id",
        "provider_field": "provider",
        "quality_dependency": "calendar_consensus_surprise_precision",
        "normalization_dependency": "calendar_event_taxonomy_normalization",
        "lineage_dependency": "calendar_event_schedule_lineage",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_release_event",
        "required_fields": ["timestamp", "release_id", "scheduled_time", "release_time"],
        "optional_fields": ["delay_seconds", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "release_id",
        "provider_field": "provider",
        "quality_dependency": "calendar_consensus_surprise_precision",
        "normalization_dependency": "calendar_event_taxonomy_normalization",
        "lineage_dependency": "calendar_event_schedule_lineage",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_news_metadata",
        "required_fields": ["timestamp", "news_id", "headline_tokens", "asset_tags"],
        "optional_fields": ["macro_tags", "topic_tags", "provider"],
        "timestamp_field": "timestamp",
        "symbol_field": "news_id",
        "provider_field": "provider",
        "quality_dependency": "news_spam_and_duplicate_filtering",
        "normalization_dependency": "news_tag_taxonomy_and_asset_linking",
        "lineage_dependency": "news_metadata_only_provenance",
        "manual_review_required": False,
    },
]


def build_default_feature_input_contracts(
    profile: FeatureEngineProfile,
) -> List[FeatureInputContract]:
    contracts: List[FeatureInputContract] = []
    for item in DEFAULT_INPUT_CONTRACTS:
        c = FeatureInputContract(
            contract_id=build_feature_input_contract_id(item["dataset_type"]),
            dataset_type=item["dataset_type"],
            required_fields=list(item["required_fields"]),
            optional_fields=list(item["optional_fields"]),
            timestamp_field=item["timestamp_field"],
            symbol_field=item["symbol_field"],
            provider_field=item["provider_field"],
            quality_dependency=item["quality_dependency"],
            normalization_dependency=item["normalization_dependency"],
            lineage_dependency=item["lineage_dependency"],
            manual_review_required=item["manual_review_required"],
        )
        contracts.append(c)
    return contracts


def build_feature_input_contract_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    contracts = build_default_feature_input_contracts(profile)
    records = [c.to_dict() for c in contracts]
    df = pd.DataFrame.from_records(records)
    summary = summarize_feature_input_contracts(df)
    return df, summary


def validate_feature_input_contract(df: pd.DataFrame, dataset_type: str) -> Dict[str, Any]:
    matched = [c for c in DEFAULT_INPUT_CONTRACTS if c["dataset_type"] == dataset_type]
    if not matched:
        return {
            "valid": False,
            "dataset_type": dataset_type,
            "missing_fields": [],
            "error": f"Unknown dataset type: {dataset_type}",
        }

    contract = matched[0]
    required = set(contract["required_fields"])
    actual = set(df.columns)
    missing = list(required - actual)

    return {
        "valid": len(missing) == 0,
        "dataset_type": dataset_type,
        "missing_fields": missing,
        "required_fields_checked": list(contract["required_fields"]),
        "optional_fields_present": list(set(contract["optional_fields"]) & actual),
        "total_rows": len(df),
    }


def summarize_feature_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_contracts": len(df),
        "dataset_types": df["dataset_type"].tolist() if not df.empty and "dataset_type" in df.columns else [],
        "all_contracts_registered": len(df) >= 8,
        "manual_review_required_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "non_signal": True,
    }
