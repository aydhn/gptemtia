
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def resolve_macro_provider_preferences_from_config_profiles(profile: MacroProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"preference": "no_scraping_public_api_preferred"}])

def build_macro_provider_preference_resolver_report(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = resolve_macro_provider_preferences_from_config_profiles(profile)
    return df, summarize_macro_provider_preference_resolver(df)

def summarize_macro_provider_preference_resolver(df: pd.DataFrame) -> dict:
    return {"total_preferences": len(df)}
