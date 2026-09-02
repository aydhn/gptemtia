
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def calculate_resilience_score(drill_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalDRProfile) -> float:
    return 1.0

def classify_resilience_score(score: float, profile: LocalDRProfile) -> str:
    return "high"

def build_resilience_score_report(drill_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"score": 1.0}]), {"total": 1}

def summarize_resilience_score(score_df: pd.DataFrame) -> dict:
    return {"total": len(score_df)}
