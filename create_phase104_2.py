import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file('advanced_config_profiles/portfolio_profiles.py', '''
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
''')

write_file('advanced_config_profiles/report_profiles.py', '''
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
''')

write_file('advanced_config_profiles/safety_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_safety_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["standard_local_research_safety", "strict_no_advice_safety", "strict_no_live_broker_safety", 
             "strict_no_scraping_safety", "strict_no_deployment_safety", "strict_manual_review_safety", "full_safety_boundary"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("safety_profile_domain", n),
        profile_domain="safety_profile_domain",
        profile_name=n,
        description=f"Safety profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_safety_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_safety_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_safety_profiles(df)

def summarize_safety_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/profile_composition.py', '''
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
''')

write_file('advanced_config_profiles/profile_compatibility.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ProfileCompatibilityItem, profile_compatibility_item_to_dict, build_profile_compatibility_id

def evaluate_profile_compatibility(left_profile: str, right_profile: str) -> ProfileCompatibilityItem:
    status = "profile_ready"
    reason = "No explicit conflict found."
    manual_review = False
    
    if "intraday_research_no_live" in left_profile and "live_trading" in right_profile:
        status = "profile_incompatible"
        reason = "intraday_research_no_live + live_trading hiçbir zaman uyumlu değil"
    elif "aggressive_research_only" in left_profile and "conservative report" in right_profile:
        status = "profile_ready_with_warnings"
        reason = "aggressive_research_only + conservative report uyumlu ama warning'li"
    elif "no_ml_baseline" in left_profile and "ML-heavy research" in right_profile:
        status = "profile_ready_with_warnings"
        reason = "no_ml_baseline + ML-heavy research uyumsuz/warning"
    elif "no_regime_baseline" in left_profile and "regime_adaptive" in right_profile:
        status = "profile_ready_with_warnings"
        reason = "no_regime_baseline + regime_adaptive strategy uyumsuz/warning"
        
    return ProfileCompatibilityItem(
        compatibility_id=build_profile_compatibility_id(left_profile, right_profile),
        left_profile=left_profile,
        right_profile=right_profile,
        compatibility_status=status,
        reason=reason,
        manual_review_required=manual_review
    )

def build_default_profile_compatibility_items(profile: AdvancedConfigSystemProfile) -> list[ProfileCompatibilityItem]:
    pairs = [
        ("intraday_research_no_live", "live_trading"),
        ("aggressive_research_only", "conservative report"),
        ("no_ml_baseline", "ML-heavy research"),
        ("no_regime_baseline", "regime_adaptive"),
        ("no_scraping", "any"),
        ("strict_no_advice_safety", "any"),
        ("strict_no_live_broker_safety", "any"),
        ("strict_no_deployment_safety", "any")
    ]
    return [evaluate_profile_compatibility(l, r) for l, r in pairs]

def build_profile_compatibility_matrix(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_profile_compatibility_items(profile)
    df = pd.DataFrame([profile_compatibility_item_to_dict(item) for item in items])
    return df, summarize_profile_compatibility(df)

def summarize_profile_compatibility(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')
