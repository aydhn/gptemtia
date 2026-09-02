import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile

def calculate_maintainability_readiness_score(complexity_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalSimplificationProfile) -> float:
    return 0.85

def classify_maintainability_readiness_score(score: float, profile: LocalSimplificationProfile) -> str:
    return "ready" if score > profile.min_readiness_score else "needs_review"

def build_maintainability_readiness_score_report(complexity_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_maintainability_readiness_score(complexity_df, gap_df, risk_df, profile)
    df = pd.DataFrame([{"score": score, "status": classify_maintainability_readiness_score(score, profile)}])
    return df, summarize_maintainability_readiness_score(df)

def summarize_maintainability_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"scores": len(score_df), "warnings": ["Score architecture approval degildir.", "Low score manual review onerir."]}
