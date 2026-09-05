import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def calculate_fx_readiness_score(
    profile_df: pd.DataFrame, domain_df: pd.DataFrame, pair_df: pd.DataFrame, capability_df: pd.DataFrame,
    registry_df: pd.DataFrame, safety_df: pd.DataFrame, health_df: pd.DataFrame, profile: FXProviderProfile,
) -> float:
    # mock scoring logic
    if health_df.empty or safety_df.empty: return 0.0
    score = 0.5 + 0.5 * (len(health_df[health_df["status"]=="healthy"]) / len(health_df))
    return min(1.0, max(0.0, score))

def classify_fx_readiness_score(score: float, profile: FXProviderProfile) -> str:
    if score >= 0.8: return "high"
    if score >= profile.min_readiness_score: return "medium"
    return "low (manual review suggested)"

def build_fx_readiness_score_report(
    profile_df: pd.DataFrame, domain_df: pd.DataFrame, pair_df: pd.DataFrame, capability_df: pd.DataFrame,
    registry_df: pd.DataFrame, safety_df: pd.DataFrame, health_df: pd.DataFrame, profile: FXProviderProfile,
) -> Tuple[pd.DataFrame, Dict]:
    score = calculate_fx_readiness_score(profile_df, domain_df, pair_df, capability_df, registry_df, safety_df, health_df, profile)
    cls = classify_fx_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": cls}])
    return df, summarize_fx_readiness_score(df)

def summarize_fx_readiness_score(df: pd.DataFrame) -> Dict:
    return {"score": float(df.iloc[0]["score"]) if not df.empty else 0.0}
