import pandas as pd
from .usability_config import LocalUsabilityProfile

def classify_usability_risk(row: pd.Series, profile: LocalUsabilityProfile) -> str:
    return "usability_low_risk"

def build_usability_risk_summary(gap_df: pd.DataFrame, exception_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "low"}])
    return df, {"total": len(df)}

def build_usability_risk_digest(risk_df: pd.DataFrame, profile: LocalUsabilityProfile) -> tuple[str, dict]:
    return "Low risk", {"length": 8}

def summarize_usability_risks(risk_df: pd.DataFrame) -> dict:
    return {"total": len(risk_df)}
