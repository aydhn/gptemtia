import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_portfolio_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["no_portfolio_single_asset_research", "equal_weight_simulation", "volatility_scaled_simulation", 
             "risk_budget_simulation", "risk_parity_research", "drawdown_aware_research", "constrained_optimization_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("portfolio_profile_domain", n),
        profile_domain="portfolio_profile_domain",
        profile_name=n,
        description=f"Portfolio profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=["Portfolio profile gerçek portföy yönetimi değildir", "Broker order veya gerçek pozisyon yok"],
        manual_review_required=False
    ) for n in names]

def build_portfolio_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_portfolio_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_portfolio_profiles(df)

def summarize_portfolio_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
