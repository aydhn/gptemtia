import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_config_profile_to_provider_preference_handoff(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"source_layer": "config", "manual_review_required": True}])
    return df, summarize_config_provider_handoff(df)

def summarize_config_provider_handoff(df: pd.DataFrame) -> dict: return {"total": len(df)}
