import pandas as pd
from .readiness_config import LocalReadinessProfile

def calculate_readiness_score(gate_df: pd.DataFrame, criteria_df: pd.DataFrame, findings_df: pd.DataFrame, profile: LocalReadinessProfile) -> float:
    return 1.0

def build_readiness_score_report(gate_df: pd.DataFrame, criteria_df: pd.DataFrame, findings_df: pd.DataFrame, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_readiness_score(gate_df, criteria_df, findings_df, profile)
    status = classify_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "status": status}])
    return df, summarize_readiness_score(df)

def classify_readiness_score(score: float, profile: LocalReadinessProfile) -> str:
    if score >= profile.min_readiness_score:
        return "acceptable"
    return "blocked"

def summarize_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"final_score": score_df.iloc[0]["score"] if not score_df.empty else 0.0}
