import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def detect_efficiency_candidates(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"candidate": "run status scripts before full reports", "rationale": "Saves time", "warning": "Otomatik optimizasyon degildir."}])

def build_efficiency_candidate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_efficiency_candidates(project_root, profile)
    return df, summarize_efficiency_candidates(df)

def summarize_efficiency_candidates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
