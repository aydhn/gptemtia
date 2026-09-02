import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_maintenance_cost_by_layer(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"layer": "docs", "cost_category": "docs review", "warning": "Parasal kesinlik degildir."}])

def build_maintenance_cost_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_maintenance_cost_by_layer(project_root, profile)
    return df, summarize_maintenance_cost(df)

def summarize_maintenance_cost(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
