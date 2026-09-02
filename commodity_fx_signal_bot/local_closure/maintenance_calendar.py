
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_maintenance_calendar(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"task": "Check logs", "frequency": "monthly"}])

def build_closure_maintenance_calendar_rehearsal(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_maintenance_calendar(profile)
    summary = summarize_maintenance_calendar(df)
    return df, summary

def summarize_maintenance_calendar(calendar_df: pd.DataFrame) -> dict:
    return {"total": len(calendar_df)}
