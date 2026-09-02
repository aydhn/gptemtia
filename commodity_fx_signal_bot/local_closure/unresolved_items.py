
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_unresolved_items(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"item": "Full unit test coverage", "status": "unresolved"}
    ])

def build_closure_unresolved_items_register(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_unresolved_items(profile)
    summary = summarize_unresolved_items(df)
    return df, summary

def summarize_unresolved_items(unresolved_df: pd.DataFrame) -> dict:
    return {"total": len(unresolved_df)}
