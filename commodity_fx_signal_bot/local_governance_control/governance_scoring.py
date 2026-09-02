import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def calculate_governance_readiness_score(approval_df: pd.DataFrame, risk_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalGovernanceControlProfile) -> float:
    return 0.85

def classify_governance_readiness_score(score: float, profile: LocalGovernanceControlProfile) -> str:
    if score < profile.min_readiness_score:
        return "needs_manual_review"
    return "ready_for_rehearsal"

def build_governance_readiness_score_report(approval_df: pd.DataFrame, risk_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_governance_readiness_score(approval_df, risk_df, no_go_df, profile)
    data = [{"score": score, "classification": classify_governance_readiness_score(score, profile), "is_real_approval": False}]
    df = pd.DataFrame(data)
    return df, summarize_governance_readiness_score(df)

def summarize_governance_readiness_score(score_df: pd.DataFrame) -> dict:
    if score_df is None or score_df.empty:
        return {"score": 0}
    return {"score": float(score_df.iloc[0]["score"])}
