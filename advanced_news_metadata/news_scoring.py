import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def calculate_news_readiness_score(
    profile_df: pd.DataFrame,
    domain_df: pd.DataFrame,
    source_df: pd.DataFrame,
    schema_df: pd.DataFrame,
    capability_df: pd.DataFrame,
    registry_df: pd.DataFrame,
    safety_df: pd.DataFrame,
    health_df: pd.DataFrame,
    profile: NewsProviderProfile,
) -> float:
    score = 0.0
    if not profile_df.empty:
        score += 0.15
    if not domain_df.empty:
        score += 0.10
    if not source_df.empty:
        score += 0.15
    if not schema_df.empty:
        score += 0.15
    if not capability_df.empty:
        score += 0.15
    if not registry_df.empty:
        score += 0.10
    if not safety_df.empty:
        score += 0.10
    if not health_df.empty and len(health_df[health_df["status"] == "pass"]) == len(health_df):
        score += 0.10
    return min(1.0, round(score, 4))

def classify_news_readiness_score(score: float, profile: NewsProviderProfile) -> str:
    if score >= 0.80:
        return "HIGH"
    if score >= profile.min_readiness_score:
        return "MEDIUM"
    return "LOW"

def build_news_readiness_score_report(
    profile_df: pd.DataFrame,
    domain_df: pd.DataFrame,
    source_df: pd.DataFrame,
    schema_df: pd.DataFrame,
    capability_df: pd.DataFrame,
    registry_df: pd.DataFrame,
    safety_df: pd.DataFrame,
    health_df: pd.DataFrame,
    profile: NewsProviderProfile,
) -> Tuple[pd.DataFrame, Dict]:
    score = calculate_news_readiness_score(
        profile_df, domain_df, source_df, schema_df,
        capability_df, registry_df, safety_df, health_df, profile
    )
    cls = classify_news_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": cls, "profile_name": profile.name}])
    summary = summarize_news_readiness_score(df)
    return df, summary

def summarize_news_readiness_score(df: pd.DataFrame) -> Dict:
    if df.empty:
        return {}
    return df.iloc[0].to_dict()
