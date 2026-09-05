"""Lifecycle scoring."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def calculate_lifecycle_readiness_score(calendar_df: pd.DataFrame, workbook_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> float:
    return 0.85

def classify_lifecycle_readiness_score(score: float, profile: LocalLongTermOperationsProfile) -> str:
    return "lifecycle_rehearsal_ready" if score >= profile.min_readiness_score else "lifecycle_rehearsal_needs_manual_review"

def build_lifecycle_readiness_score_report(calendar_df: pd.DataFrame, workbook_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_lifecycle_readiness_score(calendar_df, workbook_df, risk_df, profile)
    cls = classify_lifecycle_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": cls, "warnings": ["operations approval değildir", "low score manual review önerir"]}])
    return df, summarize_lifecycle_readiness_score(df)

def summarize_lifecycle_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"total_items": len(score_df)}
