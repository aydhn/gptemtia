import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_storage_retention_items(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "reports", "retention": "30 days", "warning": "Dosya silmez."}])

def build_storage_retention_rehearsal_plan(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_storage_retention_items(profile)
    return df, summarize_storage_retention_plan(df)

def summarize_storage_retention_plan(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
