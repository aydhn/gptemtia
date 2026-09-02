import pandas as pd
from .performance_config import LocalPerformanceProfile

def calculate_performance_readiness_score(budget_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalPerformanceProfile) -> float:
    return 1.0

def classify_performance_readiness_score(score: float, profile: LocalPerformanceProfile) -> str:
    if score < profile.min_readiness_score: return "needs_manual_review"
    return "ready"

def build_performance_readiness_score_report(budget_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_performance_readiness_score(budget_df, gap_df, risk_df, profile)
    classification = classify_performance_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification, "warning": "benchmark/capacity approval degildir. Low score manual review onerir."}])
    return df, summarize_performance_readiness_score(df)

def summarize_performance_readiness_score(score_df: pd.DataFrame) -> dict:
    if score_df is None or score_df.empty: return {"score": 0.0}
    return {"score": float(score_df.iloc[0]["score"])}
