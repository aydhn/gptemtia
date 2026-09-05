import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile

def calculate_profile_readiness_score(
    registry_df: pd.DataFrame, preset_df: pd.DataFrame, composed_df: pd.DataFrame,
    compatibility_df: pd.DataFrame, validation_df: pd.DataFrame, profile: AdvancedConfigSystemProfile
) -> float:
    score = 0.5
    if registry_df is not None and not registry_df.empty: score += 0.1
    if preset_df is not None and not preset_df.empty: score += 0.1
    if composed_df is not None and not composed_df.empty: score += 0.1
    if validation_df is not None and not validation_df.empty and (validation_df["status"] == "passed").all(): score += 0.2
    return min(1.0, score)

def build_profile_readiness_score_report(
    registry_df: pd.DataFrame, preset_df: pd.DataFrame, composed_df: pd.DataFrame,
    compatibility_df: pd.DataFrame, validation_df: pd.DataFrame, profile: AdvancedConfigSystemProfile
) -> tuple[pd.DataFrame, dict]:
    score = calculate_profile_readiness_score(registry_df, preset_df, composed_df, compatibility_df, validation_df, profile)
    classification = classify_profile_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification}])
    return df, {"score": score, "classification": classification}

def classify_profile_readiness_score(score: float, profile: AdvancedConfigSystemProfile) -> str:
    if score >= profile.min_readiness_score:
        return "ready"
    return "needs_manual_review"

def summarize_profile_readiness_score(df: pd.DataFrame) -> dict:
    return {"mean_score": df["score"].mean() if df is not None and not df.empty else 0}
