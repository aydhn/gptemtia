import pandas as pd
from .usability_config import LocalUsabilityProfile

def calculate_usability_readiness_score(friction_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalUsabilityProfile) -> float:
    return 1.0

def classify_usability_readiness_score(score: float, profile: LocalUsabilityProfile) -> str:
    return "ready"

def build_usability_readiness_score_report(friction_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"score": 1.0, "status": "ready"}])
    return df, {"score": 1.0}

def summarize_usability_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"score": 1.0}
