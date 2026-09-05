import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_feature_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["minimal_technical_features", "standard_technical_features", "advanced_technical_features", 
             "volatility_features", "trend_momentum_features", "mean_reversion_features", 
             "macro_factor_features", "cross_asset_features", "full_feature_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("feature_profile_domain", n),
        profile_domain="feature_profile_domain",
        profile_name=n,
        description=f"Feature profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_feature_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_feature_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_feature_profiles(df)

def summarize_feature_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
