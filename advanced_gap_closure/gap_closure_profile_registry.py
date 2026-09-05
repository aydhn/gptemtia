import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import GapClosureProfileItem, build_gap_closure_profile_id, to_dict

def build_default_gap_closure_profile_items(profile: FunctionalGapClosureProfile) -> list[GapClosureProfileItem]:
    return [GapClosureProfileItem(
        profile_id=build_gap_closure_profile_id(profile.name),
        profile_name=profile.name,
        current_phase=105,
        target_final_phase=160,
        next_phase=106,
        local_only=True,
        non_production=True,
        research_only=True,
        status_label="gap_closed",
        warnings=[]
    )]

def build_functional_gap_closure_profile_registry(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_gap_closure_profile_items(profile)
    df = pd.DataFrame([to_dict(i) for i in items])
    summary = summarize_gap_closure_profile_registry(df)
    return df, summary

def summarize_gap_closure_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df)}
