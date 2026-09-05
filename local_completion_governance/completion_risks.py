import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def classify_completion_risk(row: pd.Series, profile: LocalCompletionGovernanceProfile) -> str:
    return "completion_low_risk"

def build_completion_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "none"}])
    return df, summarize_completion_risks(df)

def build_completion_risk_digest(risk_df: pd.DataFrame, profile: LocalCompletionGovernanceProfile) -> tuple[str, dict]:
    return "Digest", {"digest": True}

def summarize_completion_risks(risk_df: pd.DataFrame) -> dict:
    return {"risks": len(risk_df)}\n