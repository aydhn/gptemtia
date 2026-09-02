import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def detect_test_suite_simplification_candidates(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"candidate": "example"}])

def build_test_suite_simplification_candidate_registry(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_test_suite_simplification_candidates(project_root, profile)
    return df, summarize_test_suite_simplification(df)

def summarize_test_suite_simplification(df: pd.DataFrame) -> dict:
    return {"candidates": len(df), "warnings": ["Hicbir dosyayi degistirmez.", "Manual review required"]}
