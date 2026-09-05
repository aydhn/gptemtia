"""Lifecycle exceptions."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def detect_lifecycle_exceptions(calendar_df: pd.DataFrame, workbook_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "none", "warnings": ["auto-fix yoktur"]}])

def build_lifecycle_exception_register(calendar_df: pd.DataFrame, workbook_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_lifecycle_exceptions(calendar_df, workbook_df, no_go_df)
    return df, summarize_lifecycle_exceptions(df)

def summarize_lifecycle_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total_items": len(exception_df)}
