import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def detect_exception_escalations(escalation_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    # Simulated detection
    return pd.DataFrame([{"exception": "Mock Exception", "external_approval_allowed": False}])

def build_exception_escalation_register(escalation_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_exception_escalations(escalation_df, no_go_df)
    return df, summarize_exception_escalations(df)

def summarize_exception_escalations(exception_df: pd.DataFrame) -> dict:
    if exception_df is None or exception_df.empty:
        return {"total": 0}
    return {"total": len(exception_df)}
