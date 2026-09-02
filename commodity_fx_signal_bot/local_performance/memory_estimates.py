import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_memory_pressure_for_layer(layer_name: str, item_count: int, profile: LocalPerformanceProfile) -> dict:
    return {"layer": layer_name, "pressure": "memory_estimate_low", "warning": "Gercek memory profiler degildir."}

def build_memory_usage_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([estimate_memory_pressure_for_layer("datalake", 10, profile)])
    return df, summarize_memory_estimates(df)

def summarize_memory_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
