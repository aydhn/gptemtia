"""Lifecycle risks."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def classify_lifecycle_risk(row: pd.Series, profile: LocalLongTermOperationsProfile) -> str:
    return "lifecycle_low_risk"

def build_lifecycle_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "low", "warnings": ["Yatırım riski değildir."]}])
    return df, summarize_lifecycle_risks(df)

def build_lifecycle_risk_digest(risk_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> tuple[str, dict]:
    return "Risk digest.", {"length": 12}

def summarize_lifecycle_risks(risk_df: pd.DataFrame) -> dict:
    return {"total_items": len(risk_df)}
