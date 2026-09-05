import pandas as pd
from .provider_config import DataProviderAbstractionProfile

def resolve_provider_preferences_from_config_profiles(profile: DataProviderAbstractionProfile) -> pd.DataFrame:
    prefs = [
        {"preference": "no_scraping_public_api_preferred", "enabled": True},
        {"preference": "local_cache_preferred", "enabled": True},
        {"preference": "manual_file_import_preferred", "enabled": True},
        {"preference": "official_provider_preferred", "enabled": True},
        {"preference": "macro_calendar_provider_placeholder", "enabled": True},
        {"preference": "news_metadata_provider_placeholder", "enabled": True}
    ]
    return pd.DataFrame(prefs)

def build_provider_preference_resolver_report(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    df = resolve_provider_preferences_from_config_profiles(profile)
    return df, summarize_provider_preference_resolver(df)

def summarize_provider_preference_resolver(df: pd.DataFrame) -> dict:
    return {"total_preferences": len(df)}
