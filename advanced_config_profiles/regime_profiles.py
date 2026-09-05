import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_regime_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["no_regime_baseline", "volatility_regime", "trend_range_regime", 
             "macro_regime", "cross_asset_regime", "full_regime_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("regime_profile_domain", n),
        profile_domain="regime_profile_domain",
        profile_name=n,
        description=f"Regime profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_regime_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_regime_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_regime_profiles(df)

def summarize_regime_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
