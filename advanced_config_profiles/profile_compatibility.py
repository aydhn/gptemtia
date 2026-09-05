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
