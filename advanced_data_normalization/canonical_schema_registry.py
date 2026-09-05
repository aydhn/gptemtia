from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    CanonicalSchema,
    build_canonical_schema_id,
)

SCHEMAS_SPEC = [
    {
        "dataset_type": "dataset_fx_quote",
        "schema_name": "fx_quote_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["timestamp", "pair", "bid", "ask", "provider"],
        "primary_key_fields": ["timestamp", "pair", "provider"],
        "timestamp_field": "timestamp",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_fx_ohlcv",
        "schema_name": "fx_ohlcv_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["timestamp", "pair", "open", "high", "low", "close", "volume", "provider"],
        "primary_key_fields": ["timestamp", "pair", "provider"],
        "timestamp_field": "timestamp",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_commodity_spot",
        "schema_name": "commodity_spot_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["timestamp", "symbol", "price", "currency", "unit", "provider"],
        "primary_key_fields": ["timestamp", "symbol", "provider"],
        "timestamp_field": "timestamp",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_commodity_ohlcv",
        "schema_name": "commodity_ohlcv_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["timestamp", "symbol", "open", "high", "low", "close", "volume", "provider"],
        "primary_key_fields": ["timestamp", "symbol", "provider"],
        "timestamp_field": "timestamp",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_commodity_spot",
        "schema_name": "commodity_futures_metadata_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["contract_code", "root_symbol", "expiry_date", "roll_rule", "provider"],
        "primary_key_fields": ["contract_code", "provider"],
        "timestamp_field": "expiry_date",
        "provider_field": "provider",
        "manual_review_required": True,
    },
    {
        "dataset_type": "dataset_macro_timeseries",
        "schema_name": "macro_timeseries_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["timestamp", "indicator", "value", "region", "frequency", "unit", "provider"],
        "primary_key_fields": ["timestamp", "indicator", "region", "provider"],
        "timestamp_field": "timestamp",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_macro_timeseries",
        "schema_name": "macro_release_metadata_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["release_id", "indicator", "scheduled_time", "actual_time", "status", "provider"],
        "primary_key_fields": ["release_id", "provider"],
        "timestamp_field": "scheduled_time",
        "provider_field": "provider",
        "manual_review_required": True,
    },
    {
        "dataset_type": "dataset_calendar_event",
        "schema_name": "calendar_event_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["event_id", "canonical_event", "country", "currency", "scheduled_time", "impact", "provider"],
        "primary_key_fields": ["event_id", "provider"],
        "timestamp_field": "scheduled_time",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_release_event",
        "schema_name": "release_event_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["event_id", "actual", "forecast", "previous", "revised", "unit", "provider"],
        "primary_key_fields": ["event_id", "provider"],
        "timestamp_field": "event_id",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_news_metadata",
        "schema_name": "news_metadata_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["news_id", "headline", "source_name", "published_at", "tags", "sentiment", "provider"],
        "primary_key_fields": ["news_id", "provider"],
        "timestamp_field": "published_at",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_news_metadata",
        "schema_name": "news_item_reference_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["reference_id", "news_id", "url_reference_only", "external_id", "provider"],
        "primary_key_fields": ["reference_id", "provider"],
        "timestamp_field": "news_id",
        "provider_field": "provider",
        "manual_review_required": False,
    },
    {
        "dataset_type": "dataset_provider_metadata",
        "schema_name": "provider_metadata_v1",
        "schema_version": "v1.0",
        "canonical_fields": ["provider_id", "provider_name", "provider_type", "version", "status"],
        "primary_key_fields": ["provider_id"],
        "timestamp_field": "provider_id",
        "provider_field": "provider_name",
        "manual_review_required": False,
    },
]


def build_default_canonical_schemas(
    profile: DataNormalizationProfile,
) -> List[CanonicalSchema]:
    schemas = []
    for spec in SCHEMAS_SPEC:
        s = CanonicalSchema(
            schema_id=build_canonical_schema_id(spec["dataset_type"], spec["schema_version"]),
            dataset_type=spec["dataset_type"],
            schema_name=spec["schema_name"],
            schema_version=spec["schema_version"],
            canonical_fields=spec["canonical_fields"],
            primary_key_fields=spec["primary_key_fields"],
            timestamp_field=spec["timestamp_field"],
            provider_field=spec["provider_field"],
            manual_review_required=spec["manual_review_required"],
        )
        schemas.append(s)
    return schemas


def build_canonical_schema_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    schemas = build_default_canonical_schemas(profile)
    records = [s.to_dict() for s in schemas]
    df = pd.DataFrame.from_records(records)
    summary = summarize_canonical_schema_registry(df)
    return df, summary


def summarize_canonical_schema_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_schemas": len(df),
        "schemas": df["schema_name"].tolist() if "schema_name" in df.columns else [],
        "dataset_types": df["dataset_type"].unique().tolist() if "dataset_type" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
