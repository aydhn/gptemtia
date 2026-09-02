import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_cpu_pressure_for_file(path: Path, project_root: Path, profile: LocalPerformanceProfile) -> dict:
    return {"file": str(path.name), "pressure": "cpu_estimate_low", "warning": "Gercek CPU olcumu degildir."}

def build_cpu_usage_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"layer": "scripts", "pressure": "cpu_estimate_low"}])
    return df, summarize_cpu_estimates(df)

def summarize_cpu_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
