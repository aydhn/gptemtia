import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderCapability, build_provider_capability_id
from dataclasses import asdict

def build_default_provider_capabilities(profile: DataProviderAbstractionProfile) -> list[ProviderCapability]:
    caps = [
        ("dry_run_fixture_ohlcv", "provider_dry_run_fixture", ["coverage_cross_asset"], ["data_ohlcv"]),
        ("dry_run_fixture_macro", "provider_dry_run_fixture", ["coverage_macro"], ["data_macro_timeseries"]),
        ("dry_run_fixture_calendar", "provider_dry_run_fixture", ["coverage_economic_calendar"], ["data_event_calendar"]),
        ("dry_run_fixture_news_metadata", "provider_dry_run_fixture", ["coverage_news_metadata"], ["data_news_metadata"]),
        ("manual_file_ohlcv", "provider_manual_file", ["coverage_cross_asset"], ["data_ohlcv"]),
        ("manual_file_macro", "provider_manual_file", ["coverage_macro"], ["data_macro_timeseries"]),
        ("local_cache_ohlcv", "provider_local_cache", ["coverage_cross_asset"], ["data_ohlcv"]),
        ("official_api_fx_placeholder", "provider_official_api_placeholder", ["coverage_fx"], ["data_ohlcv", "data_quote"]),
        ("official_api_commodities_placeholder", "provider_official_api_placeholder", ["coverage_commodities"], ["data_ohlcv"]),
        ("official_api_macro_placeholder", "provider_official_api_placeholder", ["coverage_macro"], ["data_macro_timeseries"]),
        ("licensed_calendar_placeholder", "provider_licensed_placeholder", ["coverage_economic_calendar"], ["data_event_calendar"]),
        ("licensed_news_metadata_placeholder", "provider_licensed_placeholder", ["coverage_news_metadata"], ["data_news_metadata"]),
    ]
    
    return [
        ProviderCapability(
            capability_id=build_provider_capability_id(name, dtypes[0]),
            provider_name=name,
            provider_type=ptype,
            asset_coverage=cov,
            data_types=dtypes,
            timeframe_support=["1d", "1h"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            no_scraping_compliant=True,
            status_label="provider_ready",
            warnings=[]
        )
        for name, ptype, cov, dtypes in caps
    ]

def build_provider_capability_registry(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_provider_capabilities(profile)
    df = pd.DataFrame([asdict(item) for item in items])
    return df, summarize_provider_capabilities(df)

def summarize_provider_capabilities(df: pd.DataFrame) -> dict:
    return {"total_capabilities": len(df)}
