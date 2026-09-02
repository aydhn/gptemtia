import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_test_runtime_from_static_features(path: Path, project_root: Path, profile: LocalPerformanceProfile) -> dict:
    return {"test": path.name, "estimate": "runtime_estimate_low", "warning": "Pytest calistirilmaz."}

def build_test_runtime_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"test": "test_example.py", "estimate": "runtime_estimate_low"}])
    return df, summarize_test_runtime_estimates(df)

def summarize_test_runtime_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
