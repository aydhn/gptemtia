"""Reproducibility governance issues."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_default_reproducibility_issues(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"issue": "issue1"}])

def build_default_reproducibility_unresolved_items(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"unresolved": "unresolved1"}])

def build_reproducibility_governance_issue_register(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reproducibility_issues(profile)
    return df, summarize_reproducibility_governance_issues(df, pd.DataFrame())

def build_reproducibility_governance_unresolved_register(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reproducibility_unresolved_items(profile)
    return df, summarize_reproducibility_governance_issues(pd.DataFrame(), df)

def summarize_reproducibility_governance_issues(issue_df: pd.DataFrame, unresolved_df: pd.DataFrame) -> dict:
    return {"issues": len(issue_df), "unresolved": len(unresolved_df), "note": "Issue register official issue tracker degildir."}
