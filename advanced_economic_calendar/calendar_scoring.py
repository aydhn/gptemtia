import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def calculate_calendar_readiness_score(
    profile_df: pd.DataFrame,
    domain_df: pd.DataFrame,
    event_df: pd.DataFrame,
    capability_df: pd.DataFrame,
    registry_df: pd.DataFrame,
    safety_df: pd.DataFrame,
    health_df: pd.DataFrame,
    profile: CalendarProviderProfile,
) -> float:
    # Dummy calculation for demonstration
    score = 0.0
    if not profile_df.empty: score += 0.15
    if not domain_df.empty: score += 0.15
    if not event_df.empty: score += 0.15
    if not capability_df.empty: score += 0.15
    if not registry_df.empty: score += 0.10
    if not safety_df.empty: score += 0.15
    if not health_df.empty and len(health_df[health_df["status"] == "pass"]) == len(health_df):
        score += 0.15
    return min(1.0, score)

def classify_calendar_readiness_score(score: float, profile: CalendarProviderProfile) -> str:
    if score >= 0.8: return "HIGH"
    if score >= profile.min_readiness_score: return "MEDIUM"
    return "LOW"

def build_calendar_readiness_score_report(
    profile_df: pd.DataFrame,
    domain_df: pd.DataFrame,
    event_df: pd.DataFrame,
    capability_df: pd.DataFrame,
    registry_df: pd.DataFrame,
    safety_df: pd.DataFrame,
    health_df: pd.DataFrame,
    profile: CalendarProviderProfile,
) -> Tuple[pd.DataFrame, Dict]:
    score = calculate_calendar_readiness_score(profile_df, domain_df, event_df, capability_df, registry_df, safety_df, health_df, profile)
    cls = classify_calendar_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": cls}])
    return df, summarize_calendar_readiness_score(df)

def summarize_calendar_readiness_score(df: pd.DataFrame) -> Dict:
    if df.empty: return {}
    return df.iloc[0].to_dict()
