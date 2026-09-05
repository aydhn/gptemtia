import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_risk_preference_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["conservative_research", "balanced_research", "aggressive_research_only", 
             "low_drawdown_research", "volatility_adjusted_research", "experimental_research_only"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("risk_preference_profile_domain", n),
        profile_domain="risk_preference_profile_domain",
        profile_name=n,
        description=f"Risk preference profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=["Risk profiles sadece simülasyon ve araştırma bağlamıdır", "Gerçek portföy yönetimi değildir"],
        manual_review_required=False
    ) for n in names]

def build_risk_preference_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_risk_preference_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_risk_preference_profiles(df)

def summarize_risk_preference_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
