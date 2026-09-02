import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_operator_time_budget(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"category": "docs review", "time_budget": "1h", "warning": "Resmi is gucu plani degildir."}])

def build_operator_time_budget_report(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_operator_time_budget(profile)
    return df, summarize_operator_time_budget(df)

def summarize_operator_time_budget(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
