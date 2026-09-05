import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_asset_class_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["fx", "precious_metals", "energy", "industrial_metals", "agriculture", "macro_indicators", "cross_asset"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("asset_class_profile_domain", n),
        profile_domain="asset_class_profile_domain",
        profile_name=n,
        description=f"Asset class profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_asset_class_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_asset_class_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_asset_class_profiles(df)

def summarize_asset_class_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
