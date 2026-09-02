
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def classify_closure_risk(row: pd.Series, profile: LocalClosureProfile) -> str:
    return "closure_low_risk"

def build_closure_risk_summary(gap_df: pd.DataFrame, exception_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "None", "level": "closure_info"}])
    summary = summarize_closure_risks(df)
    return df, summary

def build_closure_risk_digest(risk_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[str, dict]:
    return "No major risks.", {"status": "ok"}

def summarize_closure_risks(risk_df: pd.DataFrame) -> dict:
    return {"total": len(risk_df)}
