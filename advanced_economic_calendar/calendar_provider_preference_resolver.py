import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def resolve_calendar_provider_preferences_from_config_profiles(profile: CalendarProviderProfile) -> pd.DataFrame:
    preferences = [
        {"config_profile": "no_scraping_public_api_preferred", "preference": "official_api"},
        {"config_profile": "local_cache_preferred", "preference": "local_cache"},
        {"config_profile": "manual_file_import_preferred", "preference": "manual_file"},
        {"config_profile": "official_provider_preferred", "preference": "official_api"},
        {"config_profile": "macro_calendar_provider_placeholder", "preference": "dry_run"},
        {"config_profile": "macro_sensitive_research", "preference": "licensed"},
        {"config_profile": "gold_macro_research", "preference": "licensed"},
        {"config_profile": "oil_macro_research", "preference": "licensed"},
        {"config_profile": "cross_asset_macro_research", "preference": "licensed"},
        {"config_profile": "volatility_regime_research", "preference": "licensed"}
    ]
    return pd.DataFrame(preferences)

def build_calendar_provider_preference_resolver_report(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = resolve_calendar_provider_preferences_from_config_profiles(profile)
    summary = summarize_calendar_provider_preference_resolver(df)
    return df, summary

def summarize_calendar_provider_preference_resolver(df: pd.DataFrame) -> Dict:
    return {
        "total_preferences": len(df)
    }
