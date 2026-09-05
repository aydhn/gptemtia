from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    CanonicalField,
    build_canonical_field_id,
)

FIELDS_SPEC = [
    # FX Quote
    {"dataset_type": "dataset_fx_quote", "field": "timestamp", "type": "iso8601_utc", "required": True, "nullable": False, "unit": "time", "note": "UTC ISO8601"},
    {"dataset_type": "dataset_fx_quote", "field": "pair", "type": "string", "required": True, "nullable": False, "unit": "symbol", "note": "Standard ISO slash (EUR/USD)"},
    {"dataset_type": "dataset_fx_quote", "field": "bid", "type": "float", "required": True, "nullable": False, "unit": "price", "note": "Positive float"},
    {"dataset_type": "dataset_fx_quote", "field": "ask", "type": "float", "required": True, "nullable": False, "unit": "price", "note": "Positive float, >= bid"},
    {"dataset_type": "dataset_fx_quote", "field": "provider", "type": "string", "required": True, "nullable": False, "unit": "slug", "note": "Provider slug"},

    # FX OHLCV
    {"dataset_type": "dataset_fx_ohlcv", "field": "timestamp", "type": "iso8601_utc", "required": True, "nullable": False, "unit": "time", "note": "UTC ISO8601"},
    {"dataset_type": "dataset_fx_ohlcv", "field": "pair", "type": "string", "required": True, "nullable": False, "unit": "symbol", "note": "Standard ISO slash (EUR/USD)"},
    {"dataset_type": "dataset_fx_ohlcv", "field": "open", "type": "float", "required": True, "nullable": False, "unit": "price", "note": "Positive float"},
    {"dataset_type": "dataset_fx_ohlcv", "field": "high", "type": "float", "required": True, "nullable": False, "unit": "price", "note": "Positive float, high >= low"},
    {"dataset_type": "dataset_fx_ohlcv", "field": "low", "type": "float", "required": True, "nullable": False, "unit": "price", "note": "Positive float"},
    {"dataset_type": "dataset_fx_ohlcv", "field": "close", "type": "float", "required": True, "nullable": False, "unit": "price", "note": "Positive float"},
    {"dataset_type": "dataset_fx_ohlcv", "field": "volume", "type": "float", "required": False, "nullable": True, "unit": "volume", "note": "Non-negative float or null"},
    {"dataset_type": "dataset_fx_ohlcv", "field": "provider", "type": "string", "required": True, "nullable": False, "unit": "slug", "note": "Provider slug"},

    # Commodity Spot
    {"dataset_type": "dataset_commodity_spot", "field": "timestamp", "type": "iso8601_utc", "required": True, "nullable": False, "unit": "time", "note": "UTC ISO8601"},
    {"dataset_type": "dataset_commodity_spot", "field": "symbol", "type": "string", "required": True, "nullable": False, "unit": "symbol", "note": "Standard symbol (XAU/USD, BRENT)"},
    {"dataset_type": "dataset_commodity_spot", "field": "price", "type": "float", "required": True, "nullable": False, "unit": "price", "note": "Positive float"},
    {"dataset_type": "dataset_commodity_spot", "field": "currency", "type": "string", "required": True, "nullable": False, "unit": "iso_curr", "note": "ISO-4217 (USD)"},
    {"dataset_type": "dataset_commodity_spot", "field": "unit", "type": "string", "required": True, "nullable": False, "unit": "unit_vocab", "note": "Canonical unit (usd_per_oz, usd_per_barrel)"},
    {"dataset_type": "dataset_commodity_spot", "field": "provider", "type": "string", "required": True, "nullable": False, "unit": "slug", "note": "Provider slug"},

    # Macro Timeseries
    {"dataset_type": "dataset_macro_timeseries", "field": "timestamp", "type": "iso8601_utc", "required": True, "nullable": False, "unit": "time", "note": "Period start or release UTC"},
    {"dataset_type": "dataset_macro_timeseries", "field": "indicator", "type": "string", "required": True, "nullable": False, "unit": "symbol", "note": "Canonical code (US_CPI_YOY)"},
    {"dataset_type": "dataset_macro_timeseries", "field": "value", "type": "float", "required": True, "nullable": False, "unit": "numeric", "note": "Macro metric value"},
    {"dataset_type": "dataset_macro_timeseries", "field": "region", "type": "string", "required": True, "nullable": False, "unit": "iso_region", "note": "ISO alpha-2 (US, TR, EU)"},
    {"dataset_type": "dataset_macro_timeseries", "field": "frequency", "type": "string", "required": True, "nullable": False, "unit": "freq_code", "note": "Canonical frequency (1d, 1mo, 1q)"},
    {"dataset_type": "dataset_macro_timeseries", "field": "unit", "type": "string", "required": True, "nullable": False, "unit": "unit_vocab", "note": "percent, index_points, bps"},
    {"dataset_type": "dataset_macro_timeseries", "field": "provider", "type": "string", "required": True, "nullable": False, "unit": "slug", "note": "Provider slug"},

    # Calendar Event
    {"dataset_type": "dataset_calendar_event", "field": "event_id", "type": "string", "required": True, "nullable": False, "unit": "id", "note": "Unique canonical event id"},
    {"dataset_type": "dataset_calendar_event", "field": "canonical_event", "type": "string", "required": True, "nullable": False, "unit": "tag", "note": "Standard name (FOMC_RATE_DECISION)"},
    {"dataset_type": "dataset_calendar_event", "field": "country", "type": "string", "required": True, "nullable": False, "unit": "iso_region", "note": "ISO alpha-2 (US, TR)"},
    {"dataset_type": "dataset_calendar_event", "field": "currency", "type": "string", "required": True, "nullable": False, "unit": "iso_curr", "note": "ISO-4217 (USD, TRY)"},
    {"dataset_type": "dataset_calendar_event", "field": "scheduled_time", "type": "iso8601_utc", "required": True, "nullable": False, "unit": "time", "note": "UTC timestamp"},
    {"dataset_type": "dataset_calendar_event", "field": "impact", "type": "string", "required": True, "nullable": False, "unit": "category", "note": "high, medium, low"},
    {"dataset_type": "dataset_calendar_event", "field": "provider", "type": "string", "required": True, "nullable": False, "unit": "slug", "note": "Provider slug"},

    # News Metadata
    {"dataset_type": "dataset_news_metadata", "field": "news_id", "type": "string", "required": True, "nullable": False, "unit": "id", "note": "Unique news identifier"},
    {"dataset_type": "dataset_news_metadata", "field": "headline", "type": "string", "required": True, "nullable": False, "unit": "text", "note": "Short headline only (no full article)"},
    {"dataset_type": "dataset_news_metadata", "field": "source_name", "type": "string", "required": True, "nullable": False, "unit": "slug", "note": "Source publisher code"},
    {"dataset_type": "dataset_news_metadata", "field": "published_at", "type": "iso8601_utc", "required": True, "nullable": False, "unit": "time", "note": "UTC publish time"},
    {"dataset_type": "dataset_news_metadata", "field": "tags", "type": "list_or_string", "required": False, "nullable": True, "unit": "tags", "note": "Comma-separated or list of tags"},
    {"dataset_type": "dataset_news_metadata", "field": "sentiment", "type": "string", "required": False, "nullable": True, "unit": "category", "note": "positive, negative, neutral"},
    {"dataset_type": "dataset_news_metadata", "field": "provider", "type": "string", "required": True, "nullable": False, "unit": "slug", "note": "Provider slug"},
]


def build_default_canonical_fields(
    profile: DataNormalizationProfile,
) -> List[CanonicalField]:
    fields = []
    for spec in FIELDS_SPEC:
        f = CanonicalField(
            field_id=build_canonical_field_id(spec["dataset_type"], spec["field"]),
            dataset_type=spec["dataset_type"],
            canonical_field_name=spec["field"],
            field_type=spec["type"],
            required=spec["required"],
            nullable=spec["nullable"],
            unit_policy=spec["unit"],
            normalization_note=spec["note"],
            manual_review_required=False,
        )
        fields.append(f)
    return fields


def build_canonical_field_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    fields = build_default_canonical_fields(profile)
    records = [f.to_dict() for f in fields]
    df = pd.DataFrame.from_records(records)
    summary = summarize_canonical_field_registry(df)
    return df, summary


def summarize_canonical_field_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_canonical_fields": len(df),
        "dataset_types": df["dataset_type"].unique().tolist() if "dataset_type" in df.columns else [],
        "required_fields_count": int(df["required"].sum()) if "required" in df.columns else 0,
        "current_phase": 113,
        "target_final_phase": 160,
    }
