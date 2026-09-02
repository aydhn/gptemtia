
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def calculate_closure_readiness_score(domain_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalClosureProfile) -> float:
    return 1.0

def classify_closure_readiness_score(score: float, profile: LocalClosureProfile) -> str:
    if score < profile.min_readiness_score:
        return "closure_needs_manual_review"
    return "closure_ready_for_rehearsal"

def build_closure_readiness_score_report(domain_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_closure_readiness_score(domain_df, gap_df, risk_df, profile)
    status = classify_closure_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "status": status}])
    summary = summarize_closure_readiness_score(df)
    return df, summary

def summarize_closure_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"score": float(score_df.iloc[0]["score"])}
