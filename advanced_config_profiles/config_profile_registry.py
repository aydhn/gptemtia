import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_config_profile_items(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    domains = [
        "research modes", "universe profiles", "timeframe profiles", "asset class profiles",
        "strategy family profiles", "risk preference profiles", "data provider preference profiles",
        "feature profiles", "regime profiles", "ML profiles", "backtest profiles",
        "portfolio profiles", "report profiles", "safety profiles"
    ]
    items = []
    for d in domains:
        items.append(ConfigProfileItem(
            profile_id=build_config_profile_id(d.replace(" ", "_"), "default"),
            profile_domain=d,
            profile_name="default",
            description=f"Default profile for {d}",
            parameters={"is_default": True},
            status_label="profile_ready",
            warnings=[],
            manual_review_required=False
        ))
    return items

def build_advanced_config_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_config_profile_items(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    summary = summarize_config_profile_registry(df)
    return df, summary

def summarize_config_profile_registry(df: pd.DataFrame) -> dict:
    return {
        "total_profiles": len(df) if df is not None else 0,
        "domains": df['profile_domain'].unique().tolist() if df is not None and not df.empty else []
    }
