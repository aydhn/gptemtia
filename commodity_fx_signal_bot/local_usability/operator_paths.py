import pandas as pd
from .usability_config import LocalUsabilityProfile

def build_first_hour_operator_path(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"step": "README oku"}, {"step": "SAFE_USAGE_GUIDE oku"}])
    return df, {"total_steps": len(df)}

def build_first_day_operator_path(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"step": "architecture"}])
    return df, {"total_steps": len(df)}

def build_weekly_operator_review_path(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"step": "status reports"}])
    return df, {"total_steps": len(df)}

def summarize_operator_paths(path_dfs: dict[str, pd.DataFrame]) -> dict:
    return {k: len(v) for k, v in path_dfs.items()}
