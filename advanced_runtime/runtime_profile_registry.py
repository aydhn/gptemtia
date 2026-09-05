import pandas as pd
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeProfileItem, build_runtime_profile_id

def build_default_runtime_profile_items(profile: AdvancedRuntimeProfile) -> list[RuntimeProfileItem]:
    return [RuntimeProfileItem(
        profile_id=build_runtime_profile_id(profile.name),
        profile_name=profile.name,
        current_phase=profile.current_phase,
        target_final_phase=profile.target_final_phase,
        local_only=profile.local_only,
        non_production=profile.non_production,
        research_only=profile.research_only,
        status_label="runtime_ready",
        warnings=[]
    )]

def build_advanced_runtime_profile_registry(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_runtime_profile_items(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    summary = summarize_runtime_profile_registry(df)
    return df, summary

def summarize_runtime_profile_registry(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total": len(df), "ready": len(df[df["status_label"] == "runtime_ready"])}
