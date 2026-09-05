import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_strategy_family_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["trend_following_research", "mean_reversion_research", "volatility_breakout_research", 
             "macro_event_research", "regime_adaptive_research", "cross_asset_confirmation_research", 
             "ensemble_research", "portfolio_signal_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("strategy_family_profile_domain", n),
        profile_domain="strategy_family_profile_domain",
        profile_name=n,
        description=f"Strategy family profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_strategy_family_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_strategy_family_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_strategy_family_profiles(df)

def summarize_strategy_family_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
