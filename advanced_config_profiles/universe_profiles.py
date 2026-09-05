import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_universe_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["major_fx_pairs", "extended_fx_pairs", "precious_metals", "energy_commodities", 
             "industrial_metals", "agriculture_commodities", "macro_cross_asset", "custom_research_universe_placeholder"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("universe_profile_domain", n),
        profile_domain="universe_profile_domain",
        profile_name=n,
        description=f"Universe profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_universe_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_universe_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_universe_profiles(df)

def summarize_universe_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
