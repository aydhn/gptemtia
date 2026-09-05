import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ComposedResearchProfile, composed_research_profile_to_dict, build_composed_profile_id

def compose_research_profile(
    composed_profile_name: str, research_mode: str, universe_profile: str, timeframe_profile: str,
    asset_class_profile: str, strategy_family_profile: str, risk_preference_profile: str,
    data_provider_preference_profile: str, feature_profile: str, regime_profile: str,
    ml_profile: str, backtest_profile: str, portfolio_profile: str, report_profile: str, safety_profile: str,
) -> ComposedResearchProfile:
    return ComposedResearchProfile(
        composed_profile_id=build_composed_profile_id(composed_profile_name),
        composed_profile_name=composed_profile_name,
        research_mode=research_mode,
        universe_profile=universe_profile,
        timeframe_profile=timeframe_profile,
        asset_class_profile=asset_class_profile,
        strategy_family_profile=strategy_family_profile,
        risk_preference_profile=risk_preference_profile,
        data_provider_preference_profile=data_provider_preference_profile,
        feature_profile=feature_profile,
        regime_profile=regime_profile,
        ml_profile=ml_profile,
        backtest_profile=backtest_profile,
        portfolio_profile=portfolio_profile,
        report_profile=report_profile,
        safety_profile=safety_profile,
        compatibility_status="profile_needs_manual_review",
        warnings=["Canlı trading veya yatırım tavsiyesi değildir", "dry-run/local-only"],
        manual_review_required=True
    )

def build_default_composed_research_profiles(profile: AdvancedConfigSystemProfile) -> list[ComposedResearchProfile]:
    names = ["balanced_fx_daily_research", "conservative_gold_macro_research", "oil_volatility_research",
             "cross_asset_macro_research", "trend_following_fx_research", "mean_reversion_metals_research",
             "regime_adaptive_commodities_research", "ml_gpu_optional_research", "portfolio_risk_simulation_research",
             "full_advanced_research_dry_run"]
    
    return [compose_research_profile(
        n, "default", "default", "default", "default", "default", "default", "default",
        "default", "default", "default", "default", "default", "default", "default"
    ) for n in names]

def build_composed_research_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_composed_research_profiles(profile)
    df = pd.DataFrame([composed_research_profile_to_dict(item) for item in items])
    return df, summarize_composed_profiles(df)

def summarize_composed_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
