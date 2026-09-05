import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchEngineProfileItem, build_research_engine_profile_id

def build_default_research_engine_profile_items(profile: AdvancedResearchEngineProfile) -> list[ResearchEngineProfileItem]:
    return [
        ResearchEngineProfileItem(
            profile_id=build_research_engine_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=profile.current_phase,
            target_final_phase=profile.target_final_phase,
            local_only=profile.local_only,
            non_production=profile.non_production,
            research_only=profile.research_only,
            status_label="research_engine_ready",
            warnings=[]
        )
    ]

def build_research_engine_profile_registry(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_research_engine_profile_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_research_engine_profile_registry(df)
    return df, summary

def summarize_research_engine_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df), "status_ready": len(df[df['status_label'] == "research_engine_ready"])}
