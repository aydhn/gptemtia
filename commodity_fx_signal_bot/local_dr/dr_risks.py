
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def classify_dr_risk(row: pd.Series, profile: LocalDRProfile) -> str:
    return "resilience_low_risk"

def build_dr_risk_digest(risk_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[str, dict]:
    return "digest", {}

def build_dr_risk_summary(gap_df: pd.DataFrame, drill_df: pd.DataFrame, security_df: pd.DataFrame | None, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"risk": "low"}]), {"total": 1}

def summarize_dr_risks(risk_df: pd.DataFrame) -> dict:
    return {"total": len(risk_df)}
