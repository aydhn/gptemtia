"""Reproducibility risks."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def classify_reproducibility_risk(row: pd.Series, profile: LocalReproducibilityGovernanceProfile) -> str:
    return "reproducibility_low_risk"

def build_reproducibility_risk_digest(risk_df: pd.DataFrame, profile: LocalReproducibilityGovernanceProfile) -> tuple[str, dict]:
    return "Risk digest", {"status": "ok"}

def build_reproducibility_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "low"}])
    return df, summarize_reproducibility_risks(df)

def summarize_reproducibility_risks(risk_df: pd.DataFrame) -> dict:
    return {"risks": len(risk_df), "note": "Reproducibility risk yatirim riski degildir."}
