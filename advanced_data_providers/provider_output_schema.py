import pandas as pd
from .provider_config import DataProviderAbstractionProfile

def build_default_provider_output_schemas(profile: DataProviderAbstractionProfile) -> pd.DataFrame:
    schemas = [
        {"schema": "ohlcv", "fields": "symbol, timestamp, open, high, low, close, volume, provider_name, retrieval_mode, data_quality_status"},
        {"schema": "quote", "fields": "symbol, timestamp, bid, ask, mid, provider_name"},
        {"schema": "macro_timeseries", "fields": "indicator, timestamp, value, unit, region, provider_name"},
        {"schema": "event_calendar", "fields": "event_id, timestamp, region, event_name, importance, actual, forecast, previous, provider_name"},
        {"schema": "news_metadata", "fields": "item_id, timestamp, source_name, title_or_summary_ref, asset_tags, macro_tags, provider_name"},
        {"schema": "provider_metadata", "fields": "provider_name, provider_type, coverage, license_note, credential_policy, no_scraping_policy"},
    ]
    return pd.DataFrame(schemas)

def build_provider_output_schema_contract(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_provider_output_schemas(profile)
    return df, summarize_provider_output_schema(df)

def summarize_provider_output_schema(df: pd.DataFrame) -> dict:
    return {"total_schemas": len(df)}
