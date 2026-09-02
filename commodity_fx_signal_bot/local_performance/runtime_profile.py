import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_runtime_profile_items(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        {"mode_name": "full_local_report_generation", "description": "Full generation", "dry_run_only": True},
        {"mode_name": "lightweight_status_only", "description": "Status only", "dry_run_only": True},
        {"mode_name": "manual_review_mode", "description": "Manual review", "dry_run_only": True}
    ]
    return pd.DataFrame(data)

def classify_runtime_mode(row: pd.Series, profile: LocalPerformanceProfile) -> str:
    return row["mode_name"]

def build_lightweight_runtime_profile(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_runtime_profile_items(profile)
    df["classified_mode"] = df.apply(lambda r: classify_runtime_mode(r, profile), axis=1)
    return df, summarize_lightweight_runtime_profile(df)

def summarize_lightweight_runtime_profile(profile_df: pd.DataFrame) -> dict:
    return {"total": len(profile_df) if profile_df is not None else 0}
