import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def calculate_completion_readiness_score(inventory_df: pd.DataFrame, criteria_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalProjectCompletionProfile) -> float:
    return 0.5

def classify_completion_readiness_score(score: float, profile: LocalProjectCompletionProfile) -> str:
    return "needs_review"

def build_completion_readiness_score_report(inventory_df: pd.DataFrame, criteria_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_completion_readiness_score(inventory_df, criteria_df, risk_df, profile)
    df = pd.DataFrame([{"score": score, "class": classify_completion_readiness_score(score, profile)}])
    return df, summarize_completion_readiness_score(df)

def summarize_completion_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"score": float(score_df.iloc[0]["score"]), "note": "Low score manual review önerir. Score official completion approval değildir."}
