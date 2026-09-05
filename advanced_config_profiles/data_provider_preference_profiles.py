import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_data_provider_preference_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["no_scraping_public_api_preferred", "local_cache_preferred", "manual_file_import_preferred", 
             "official_provider_preferred", "macro_calendar_provider_placeholder", "news_metadata_provider_placeholder"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("data_provider_preference_domain", n),
        profile_domain="data_provider_preference_domain",
        profile_name=n,
        description=f"Data provider preference for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=["Scraping yok", "Gerçek veri indirme değildir"],
        manual_review_required=False
    ) for n in names]

def build_data_provider_preference_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_data_provider_preference_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_data_provider_preference_profiles(df)

def summarize_data_provider_preference_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
