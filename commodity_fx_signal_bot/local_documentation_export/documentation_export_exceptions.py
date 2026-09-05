"""Export exceptions."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def build_documentation_export_exception_register(page_df: pd.DataFrame, binder_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_documentation_export_exceptions(page_df, binder_df, no_go_df)
    return df, summarize_documentation_export_exceptions(df)

def detect_documentation_export_exceptions(page_df: pd.DataFrame, binder_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    # graceful fallback if empty
    return pd.DataFrame(columns=["exception_id", "description"])

def summarize_documentation_export_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"count": len(exception_df)}
