"""Atlas exceptions module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def detect_meta_index_exceptions(meta_df: pd.DataFrame, lookup_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "none", "severity": "low"}])

def build_meta_index_exception_register(meta_df: pd.DataFrame, lookup_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_meta_index_exceptions(meta_df, lookup_df, no_go_df)
    return df, summarize_meta_index_exceptions(df)

def summarize_meta_index_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"exceptions": len(exception_df)}
