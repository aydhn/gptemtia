import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_default_completion_issues(profile: LocalCompletionGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"issue_id": "I1", "status": "closed"}])

def build_default_completion_unresolved_items(profile: LocalCompletionGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"issue_id": "U1", "status": "open"}])

def build_completion_governance_issue_register(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_completion_issues(profile)
    return df, summarize_completion_governance_issues(df, pd.DataFrame())

def build_completion_governance_unresolved_register(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_completion_unresolved_items(profile)
    return df, summarize_completion_governance_issues(pd.DataFrame(), df)

def summarize_completion_governance_issues(issue_df: pd.DataFrame, unresolved_df: pd.DataFrame) -> dict:
    return {"issues": len(issue_df), "unresolved": len(unresolved_df)}\n