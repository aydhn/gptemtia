import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def discover_resource_footprint_items(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "reports", "type": "disk", "warning": "Gercek profiler degildir."}])

def build_resource_footprint_rehearsal_report(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_resource_footprint_items(project_root, profile)
    return df, summarize_resource_footprint(df)

def summarize_resource_footprint(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
