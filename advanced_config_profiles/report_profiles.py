import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_report_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["concise_research_report", "detailed_research_report", "analyst_handbook_report", 
             "model_validation_report", "backtest_reliability_report", "portfolio_risk_report", "full_advanced_delivery_report"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("report_profile_domain", n),
        profile_domain="report_profile_domain",
        profile_name=n,
        description=f"Report profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_report_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_report_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_report_profiles(df)

def summarize_report_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
