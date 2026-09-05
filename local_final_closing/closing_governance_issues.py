import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_default_closing_issues(profile: LocalFinalClosingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"issue_id": "issue-1", "title": "Manual review needed", "status": "open"}
    ])

def build_default_closing_unresolved_items(profile: LocalFinalClosingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"item_id": "unresolved-1", "title": "Final operator sign-off pending", "status": "open"}
    ])

def build_closing_governance_final_issue_register(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closing_issues(profile)
    return df, summarize_closing_governance_issues(df, pd.DataFrame())

def build_closing_governance_final_unresolved_register(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closing_unresolved_items(profile)
    return df, summarize_closing_governance_issues(pd.DataFrame(), df)

def summarize_closing_governance_issues(issue_df: pd.DataFrame, unresolved_df: pd.DataFrame) -> dict:
    return {
        "total_issues": len(issue_df),
        "total_unresolved": len(unresolved_df)
    }
