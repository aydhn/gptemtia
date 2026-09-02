import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def detect_duplicate_pattern_candidates(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"pattern": "repeated report builder pattern"}])

def build_duplicate_pattern_consolidation_candidate_registry(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_duplicate_pattern_candidates(project_root, profile)
    return df, summarize_duplicate_pattern_candidates(df)

def summarize_duplicate_pattern_candidates(df: pd.DataFrame) -> dict:
    return {"patterns": len(df), "warnings": ["False positive ihtimali olabilir.", "Destructive action onerisi yok."]}
