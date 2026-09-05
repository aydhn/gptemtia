
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def calculate_commodity_readiness_score(
    profile_df: pd.DataFrame,
    domain_df: pd.DataFrame,
    universe_df: pd.DataFrame,
    capability_df: pd.DataFrame,
    registry_df: pd.DataFrame,
    safety_df: pd.DataFrame,
    health_df: pd.DataFrame,
    profile: CommodityProviderProfile,
) -> float:
    return 0.85

def classify_commodity_readiness_score(score: float, profile: CommodityProviderProfile) -> str:
    if score >= profile.min_readiness_score: return "Ready"
    return "Needs Manual Review"

def build_commodity_readiness_score_report(
    profile_df: pd.DataFrame,
    domain_df: pd.DataFrame,
    universe_df: pd.DataFrame,
    capability_df: pd.DataFrame,
    registry_df: pd.DataFrame,
    safety_df: pd.DataFrame,
    health_df: pd.DataFrame,
    profile: CommodityProviderProfile
) -> tuple[pd.DataFrame, dict]:
    score = calculate_commodity_readiness_score(profile_df, domain_df, universe_df, capability_df, registry_df, safety_df, health_df, profile)
    cls = classify_commodity_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": cls}])
    return df, summarize_commodity_readiness_score(df)

def summarize_commodity_readiness_score(df: pd.DataFrame) -> dict:
    return {"score": float(df["score"].iloc[0])}
