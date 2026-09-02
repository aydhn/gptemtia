
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_ownership_matrix(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"domain": "data_lake", "owner": "offline_system"}])

def build_closure_ownership_matrix_rehearsal(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_ownership_matrix(profile)
    summary = summarize_ownership_matrix(df)
    return df, summary

def summarize_ownership_matrix(owner_df: pd.DataFrame) -> dict:
    return {"total": len(owner_df)}
