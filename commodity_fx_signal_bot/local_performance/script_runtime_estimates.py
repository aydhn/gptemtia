import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_script_runtime_from_static_features(path: Path, project_root: Path, profile: LocalPerformanceProfile) -> dict:
    return {"script": path.name, "estimate": "runtime_estimate_low", "warning": "Komut calistirilmaz."}

def build_script_runtime_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"script": "example.py", "estimate": "runtime_estimate_low"}])
    return df, summarize_script_runtime_estimates(df)

def summarize_script_runtime_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
