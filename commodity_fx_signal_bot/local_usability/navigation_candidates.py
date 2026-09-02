import pandas as pd
from pathlib import Path
from .usability_config import LocalUsabilityProfile

def detect_confusing_name_candidates(project_root: Path, profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"path": "foo", "reason": "confusing"}])

def detect_missing_navigation_candidates(project_root: Path, profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"path": "bar", "reason": "missing nav"}])

def build_confusing_name_candidate_registry(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_confusing_name_candidates(project_root, profile)
    return df, {"total": len(df)}

def build_missing_navigation_candidate_registry(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_missing_navigation_candidates(project_root, profile)
    return df, {"total": len(df)}

def summarize_navigation_candidates(candidate_df: pd.DataFrame) -> dict:
    return {"total": len(candidate_df)}
