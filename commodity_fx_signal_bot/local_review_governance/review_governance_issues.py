import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_default_review_issues(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [{"issue": "Test issue", "status": "open"}]
    return pd.DataFrame(data)

def build_default_review_unresolved_items(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [{"unresolved": "Test unresolved", "status": "open"}]
    return pd.DataFrame(data)

def build_review_governance_issue_register(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_review_issues(profile)
    return df, summarize_review_governance_issues(df, pd.DataFrame())

def build_review_governance_unresolved_register(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_review_unresolved_items(profile)
    return df, summarize_review_governance_issues(pd.DataFrame(), df)

def summarize_review_governance_issues(issue_df: pd.DataFrame, unresolved_df: pd.DataFrame) -> dict:
    return {"issues": len(issue_df), "unresolved": len(unresolved_df)}
