"""
Archival Risks.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def classify_archival_risk(row: pd.Series, profile: LocalArchivalProfile) -> str:
    return "archival_low_risk"

def build_archival_risk_digest(risk_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[str, dict]:
    return "No major risks.", {"digest": "No major risks"}

def build_archival_risk_summary(gap_df: pd.DataFrame, exception_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame(columns=["risk_id", "risk_label", "description"])
    return df, summarize_archival_risks(df)

def summarize_archival_risks(risk_df: pd.DataFrame) -> dict:
    return {"total_risks": len(risk_df) if risk_df is not None else 0}
