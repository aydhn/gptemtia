"""
Archival Scoring.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def calculate_archival_readiness_score(hash_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalArchivalProfile) -> float:
    return 1.0

def classify_archival_readiness_score(score: float, profile: LocalArchivalProfile) -> str:
    if score < profile.min_readiness_score: return "needs_review"
    return "ready"

def build_archival_readiness_score_report(hash_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_archival_readiness_score(hash_df, gap_df, risk_df, profile)
    df = pd.DataFrame([{"score": score, "status": classify_archival_readiness_score(score, profile)}])
    return df, summarize_archival_readiness_score(df)

def summarize_archival_readiness_score(score_df: pd.DataFrame) -> dict:
    if score_df is None or score_df.empty: return {}
    return score_df.iloc[0].to_dict()
