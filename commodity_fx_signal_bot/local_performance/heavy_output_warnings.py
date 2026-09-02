import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def detect_heavy_output_warnings(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"warning": "review CSV indexes before markdown binders", "type": "heavy_output_warning", "note": "Dosya silme onermez."}])

def build_heavy_output_warning_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_heavy_output_warnings(project_root, profile)
    return df, summarize_heavy_output_warnings(df)

def summarize_heavy_output_warnings(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
