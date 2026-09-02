import pandas as pd
import os
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_disk_usage_by_layer(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"layer": "datalake", "size_mb": 10, "warning": "Dosya icerigi okunmaz."}])

def build_disk_usage_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_disk_usage_by_layer(project_root, profile)
    return df, summarize_disk_estimates(df)

def summarize_disk_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
