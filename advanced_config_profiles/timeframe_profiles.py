import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_timeframe_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["1h_research_no_live", "4h_research", "daily_research", "weekly_research", 
             "multi_timeframe_research", "macro_event_window_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("timeframe_profile_domain", n),
        profile_domain="timeframe_profile_domain",
        profile_name=n,
        description=f"Timeframe profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_timeframe_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_timeframe_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_timeframe_profiles(df)

def summarize_timeframe_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
