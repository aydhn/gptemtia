
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_closure_future_improvement_backlog(lessons_df: pd.DataFrame, roadmap_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"improvement": "Better logging"}])
    summary = summarize_future_improvement_backlog(df)
    return df, summary

def summarize_future_improvement_backlog(improvement_df: pd.DataFrame) -> dict:
    return {"total": len(improvement_df)}
