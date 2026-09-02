
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def classify_hardening_risk(row: pd.Series, profile: LocalHardeningProfile) -> str: return "unknown"
def build_hardening_risk_digest(risk_df: pd.DataFrame, profile: LocalHardeningProfile) -> tuple[str, dict]: return "", {}
def summarize_hardening_risks(risk_df: pd.DataFrame) -> dict: return {"total": len(risk_df)}
def build_final_hardening_risk_summary(gap_df: pd.DataFrame, safety_df: pd.DataFrame, command_df: pd.DataFrame, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_hardening_risks(df)
