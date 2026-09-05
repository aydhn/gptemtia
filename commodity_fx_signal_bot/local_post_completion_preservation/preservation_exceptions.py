import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def detect_preservation_exceptions(inventory_df: pd.DataFrame, evidence_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "none"}])

def build_preservation_exception_register(inventory_df: pd.DataFrame, evidence_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_preservation_exceptions(inventory_df, evidence_df, no_go_df)
    return df, summarize_preservation_exceptions(df)

def summarize_preservation_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"count": len(exception_df)}
