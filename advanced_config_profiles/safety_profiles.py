import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_safety_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["standard_local_research_safety", "strict_no_advice_safety", "strict_no_live_broker_safety", 
             "strict_no_scraping_safety", "strict_no_deployment_safety", "strict_manual_review_safety", "full_safety_boundary"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("safety_profile_domain", n),
        profile_domain="safety_profile_domain",
        profile_name=n,
        description=f"Safety profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_safety_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_safety_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_safety_profiles(df)

def summarize_safety_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
