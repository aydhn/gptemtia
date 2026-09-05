import pandas as pd
from .runtime_config import AdvancedRuntimeProfile

def calculate_runtime_readiness_score(
    profile_df: pd.DataFrame, context_df: pd.DataFrame, capability_df: pd.DataFrame,
    module_df: pd.DataFrame, health_df: pd.DataFrame, profile: AdvancedRuntimeProfile
) -> float:
    # dummy logic for valid structures
    score = 0.85
    if profile_df.empty or context_df.empty or capability_df.empty or module_df.empty or health_df.empty:
        score = 0.3
    return score

def classify_runtime_readiness_score(score: float, profile: AdvancedRuntimeProfile) -> str:
    if score >= profile.min_readiness_score:
        return "READY"
    return "NEEDS_MANUAL_REVIEW"

def build_runtime_readiness_score_report(
    profile_df: pd.DataFrame, context_df: pd.DataFrame, capability_df: pd.DataFrame,
    module_df: pd.DataFrame, health_df: pd.DataFrame, profile: AdvancedRuntimeProfile
) -> tuple[pd.DataFrame, dict]:
    score = calculate_runtime_readiness_score(profile_df, context_df, capability_df, module_df, health_df, profile)
    classification = classify_runtime_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification}])
    return df, summarize_runtime_readiness_score(df)

def summarize_runtime_readiness_score(df: pd.DataFrame) -> dict:
    if df.empty: return {"score": 0}
    return {"score": df.iloc[0]["score"], "classification": df.iloc[0]["classification"]}
