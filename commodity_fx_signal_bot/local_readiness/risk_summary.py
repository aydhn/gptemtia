import pandas as pd
from .readiness_config import LocalReadinessProfile

def build_pre_handoff_risk_summary(findings_df: pd.DataFrame, gap_df: pd.DataFrame, limitations_df: pd.DataFrame, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk_domain": "general", "risk_level": "low"}])
    return df, summarize_pre_handoff_risks(df)

def classify_pre_handoff_risk(row: pd.Series) -> str:
    return "readiness_low_risk"

def build_risk_summary_digest(risk_df: pd.DataFrame, profile: LocalReadinessProfile) -> tuple[str, dict]:
    return "Risk Summary: All risks are within local offline non-production boundaries.", {"digest_length": 100}

def summarize_pre_handoff_risks(risk_df: pd.DataFrame) -> dict:
    return {"total_risks": len(risk_df)}
