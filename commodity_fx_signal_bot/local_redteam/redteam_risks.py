import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def classify_redteam_risk(row: pd.Series, profile: LocalRedTeamProfile) -> str:
    return "redteam_low_risk"

def build_redteam_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "example_risk", "level": "redteam_low_risk"}])
    return df, summarize_redteam_risks(df)

def build_redteam_risk_digest(risk_df: pd.DataFrame, profile: LocalRedTeamProfile) -> tuple[str, dict]:
    text = "RedTeam Risk Digest\n"
    return text, {"length": len(text)}

def summarize_redteam_risks(risk_df: pd.DataFrame) -> dict:
    return {"total": len(risk_df), "note": "Not investment risk."}
