import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile

def build_default_packaging_issues(profile: LocalDistributionPackagingProfile) -> pd.DataFrame:
    return pd.DataFrame([{"issue": "dummy issue"}])

def build_default_packaging_unresolved_items(profile: LocalDistributionPackagingProfile) -> pd.DataFrame:
    return pd.DataFrame([{"unresolved": "dummy item"}])

def build_packaging_governance_issue_register(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_packaging_issues(profile)
    return df, summarize_packaging_governance_issues(df, pd.DataFrame())

def build_packaging_governance_unresolved_register(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_packaging_unresolved_items(profile)
    return df, summarize_packaging_governance_issues(pd.DataFrame(), df)

def summarize_packaging_governance_issues(issue_df: pd.DataFrame, unresolved_df: pd.DataFrame) -> dict:
    return {"status": "generated", "issues": len(issue_df), "unresolved": len(unresolved_df)}
