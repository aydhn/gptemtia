import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_growth_by_family(project_root: Path, base_dir_name: str, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family_name": base_dir_name, "current_item_count": 0, "current_size_bytes": 0, "estimated_growth_pressure": "low", "retention_note": "Manual review", "warnings": "Forecast guarantee degildir."}])

def build_report_output_growth_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_growth_by_family(project_root, "reports", profile)
    return df, summarize_growth_estimates(df)

def build_datalake_growth_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_growth_by_family(project_root, "datalake", profile)
    return df, summarize_growth_estimates(df)

def build_generated_docs_growth_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_growth_by_family(project_root, "docs", profile)
    return df, summarize_growth_estimates(df)

def summarize_growth_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
