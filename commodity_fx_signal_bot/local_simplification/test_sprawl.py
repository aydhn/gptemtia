import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_tests_by_family(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "unit", "tests": 1}])

def build_test_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_tests_by_family(project_root, profile)
    return df, summarize_test_sprawl(df)

def summarize_test_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["pytest calistirilmaz."]}
