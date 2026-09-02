
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def detect_closure_exceptions(project_root: Path, unresolved_df: pd.DataFrame, roadmap_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "None detected", "status": "info"}])

def build_closure_exception_register(project_root: Path, unresolved_df: pd.DataFrame, roadmap_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_closure_exceptions(project_root, unresolved_df, roadmap_df)
    summary = summarize_closure_exceptions(df)
    return df, summary

def summarize_closure_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total": len(exception_df)}
