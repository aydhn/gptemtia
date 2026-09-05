import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_backtest_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["simple_baseline_backtest", "cost_aware_backtest", "slippage_aware_backtest", 
             "walk_forward_backtest", "stress_test_backtest", "monte_carlo_robustness_backtest", "full_reliability_backtest"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("backtest_profile_domain", n),
        profile_domain="backtest_profile_domain",
        profile_name=n,
        description=f"Backtest profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_backtest_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_backtest_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_backtest_profiles(df)

def summarize_backtest_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
