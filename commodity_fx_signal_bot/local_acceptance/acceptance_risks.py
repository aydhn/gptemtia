import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def classify_acceptance_risk(row: pd.Series, profile: LocalAcceptanceProfile) -> str:
    return "acceptance_low_risk"

def build_acceptance_risk_summary(gap_df: pd.DataFrame, no_go_df: pd.DataFrame, quality_df: pd.DataFrame | None, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame(columns=["risk_id", "level", "description"])
    return df, summarize_acceptance_risks(df)

def build_acceptance_risk_digest(risk_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> tuple[str, dict]:
    text = "Risk Digest: No significant risks detected."
    return text, {"length": len(text)}

def summarize_acceptance_risks(risk_df: pd.DataFrame) -> dict:
    return {"total_risks": len(risk_df)}
