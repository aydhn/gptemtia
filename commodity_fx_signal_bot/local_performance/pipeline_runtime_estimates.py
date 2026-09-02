import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_known_pipeline_runtime_estimates(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"pipeline": "main", "estimate": "runtime_estimate_low", "warning": "Gercek benchmark degildir."}])

def build_pipeline_runtime_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_known_pipeline_runtime_estimates(profile)
    return df, summarize_pipeline_runtime_estimates(df)

def summarize_pipeline_runtime_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
