import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_ml_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["no_ml_baseline", "classical_ml_research", "time_series_ml_research", 
             "ensemble_ml_research", "gpu_optional_ml_research", "explainable_ml_research", "drift_aware_ml_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("ml_profile_domain", n),
        profile_domain="ml_profile_domain",
        profile_name=n,
        description=f"ML profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=["ML profile model deployment değildir", "GPU optional olmalı; CPU fallback notu bulunmalı"],
        manual_review_required=False
    ) for n in names]

def build_ml_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_ml_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_ml_profiles(df)

def summarize_ml_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
