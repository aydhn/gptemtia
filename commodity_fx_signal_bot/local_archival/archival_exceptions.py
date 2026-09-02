"""
Archival Exceptions.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def detect_archival_exceptions(inventory_df: pd.DataFrame, hash_df: pd.DataFrame, exclusion_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["item_id", "exception_type", "description"])

def build_archival_exception_register(inventory_df: pd.DataFrame, hash_df: pd.DataFrame, exclusion_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_archival_exceptions(inventory_df, hash_df, exclusion_df)
    return df, summarize_archival_exceptions(df)

def summarize_archival_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total_exceptions": len(exception_df) if exception_df is not None else 0}
