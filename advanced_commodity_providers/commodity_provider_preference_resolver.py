
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def resolve_commodity_provider_preferences_from_config_profiles(profile: CommodityProviderProfile) -> pd.DataFrame:
    data = [
        {"preference": "no_scraping_public_api_preferred", "enabled": not profile.allow_web_scraping},
        {"preference": "local_cache_preferred", "enabled": profile.enable_local_cache_provider},
        {"preference": "manual_file_import_preferred", "enabled": profile.enable_manual_file_provider},
        {"preference": "official_provider_preferred", "enabled": profile.enable_official_api_placeholder},
        {"preference": "precious_metals", "enabled": profile.enable_precious_metals},
        {"preference": "energy_commodities", "enabled": profile.enable_energy},
        {"preference": "industrial_metals", "enabled": profile.enable_industrial_metals},
        {"preference": "agriculture_commodities", "enabled": profile.enable_agriculture},
        {"preference": "broad_commodities_research", "enabled": True},
        {"preference": "gold_macro_research", "enabled": True},
        {"preference": "oil_macro_research", "enabled": True}
    ]
    return pd.DataFrame(data)

def build_commodity_provider_preference_resolver_report(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = resolve_commodity_provider_preferences_from_config_profiles(profile)
    return df, summarize_commodity_provider_preference_resolver(df)

def summarize_commodity_provider_preference_resolver(df: pd.DataFrame) -> dict:
    return {"total_preferences": len(df)}
