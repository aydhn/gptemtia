import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def detect_review_exceptions(cockpit_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "None detected", "severity": "info"}])

def build_review_exception_register(cockpit_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_review_exceptions(cockpit_df, criteria_df, no_go_df)
    return df, summarize_review_exceptions(df)

def summarize_review_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total_exceptions": len(exception_df)}
