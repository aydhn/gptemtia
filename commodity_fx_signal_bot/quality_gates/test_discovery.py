import pandas as pd
from pathlib import Path

def discover_test_files(project_root: Path) -> pd.DataFrame:
    # discover test files mock
    return pd.DataFrame([{"test_file": "tests/test_mock.py"}])

def discover_source_modules(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"module_name": "mock"}])

def map_tests_to_modules(test_df: pd.DataFrame, source_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"test_file": "tests/test_mock.py", "inferred_module": "mock", "exists": True, "size_bytes": 100, "modified_at_utc": "2024-05-25T00:00:00Z", "test_name_count_estimate": 1, "warnings": []}])

def summarize_test_discovery(test_df: pd.DataFrame, source_df: pd.DataFrame) -> dict:
    return {"total_tests": 1}
