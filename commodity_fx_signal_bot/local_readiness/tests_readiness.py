import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def build_test_readiness_report(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_test_files(project_root)
    return df, summarize_test_readiness(df)

def discover_test_files(project_root: Path) -> pd.DataFrame:
    tests_dir = project_root / "tests"
    files = []
    if tests_dir.exists():
        for p in tests_dir.rglob("test_*.py"):
            files.append({"test_file": p.name})
    return pd.DataFrame(files)

def check_test_domains_coverage(test_df: pd.DataFrame) -> pd.DataFrame:
    return test_df.copy()

def infer_missing_test_domains(test_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_test_readiness(test_df: pd.DataFrame) -> dict:
    return {
        "total_test_files": len(test_df)
    }
