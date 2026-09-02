import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def classify_governance_risk(row: pd.Series, profile: LocalGovernanceControlProfile) -> str:
    return "governance_low_risk"

def build_governance_risk_summary(exception_df: pd.DataFrame, unresolved_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    data = [{"risk": "Mock Risk", "classification": "governance_low_risk", "is_investment_risk": False}]
    df = pd.DataFrame(data)
    return df, summarize_governance_risks(df)

def build_governance_risk_digest(risk_df: pd.DataFrame, profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    return "Digest", {"length": 6}

def summarize_governance_risks(risk_df: pd.DataFrame) -> dict:
    if risk_df is None or risk_df.empty:
        return {"total": 0}
    return {"total": len(risk_df)}
