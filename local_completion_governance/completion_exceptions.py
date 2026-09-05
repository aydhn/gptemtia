import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def detect_completion_exceptions(closure_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "none"}])

def build_completion_exception_register(closure_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_completion_exceptions(closure_df, criteria_df, no_go_df)
    return df, summarize_completion_exceptions(df)

def summarize_completion_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"exceptions": len(exception_df)}\n