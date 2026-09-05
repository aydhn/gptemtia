import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def build_default_completion_unresolved_items(profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([{"issue": "No real broker integration", "status": "unresolved_intended"}])

def build_project_completion_unresolved_register(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_completion_unresolved_items(profile)
    return df, summarize_completion_unresolved(df)

def summarize_completion_unresolved(df: pd.DataFrame) -> dict:
    return {"items": len(df), "note": "Not an official issue tracker."}
