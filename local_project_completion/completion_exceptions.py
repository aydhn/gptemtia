import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def detect_completion_exceptions(inventory_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "mock_exception", "type": "info"}])

def build_completion_exception_register(inventory_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_completion_exceptions(inventory_df, criteria_df, no_go_df)
    return df, summarize_completion_exceptions(df)

def summarize_completion_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"exceptions": len(exception_df), "note": "Exception register auto-fix yapmaz."}
