import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def detect_safe_consolidation_candidates(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"candidate": "config_profiles", "safe": True}])

def build_safe_consolidation_candidate_registry(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_safe_consolidation_candidates(project_root, profile)
    return df, summarize_consolidation_candidates(df)

def summarize_consolidation_candidates(df: pd.DataFrame) -> dict:
    return {"candidates": len(df), "warnings": ["Otomatik refactor degildir.", "Manual review required"]}
