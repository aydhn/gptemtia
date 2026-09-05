import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def resolve_fx_provider_preferences_from_config_profiles(profile: FXProviderProfile) -> pd.DataFrame:
    data = [
        {"preference": "no_scraping_public_api_preferred", "enabled": True},
        {"preference": "local_cache_preferred", "enabled": True},
        {"preference": "manual_file_import_preferred", "enabled": True},
        {"preference": "official_provider_preferred", "enabled": True},
        {"preference": "major_fx_pairs", "enabled": profile.enable_major_pairs},
        {"preference": "extended_fx_pairs", "enabled": profile.enable_minor_pairs or profile.enable_exotic_pairs},
        {"preference": "macro_cross_asset", "enabled": True}
    ]
    return pd.DataFrame(data)

def build_fx_provider_preference_resolver_report(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = resolve_fx_provider_preferences_from_config_profiles(profile)
    return df, summarize_fx_provider_preference_resolver(df)

def summarize_fx_provider_preference_resolver(df: pd.DataFrame) -> Dict:
    return {"total_preferences": len(df)}
