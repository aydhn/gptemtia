import pandas as pd
from pathlib import Path

def run_pytest_collect_only(project_root: Path, timeout_seconds: int = 300) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "collected"}

def run_pytest_suite(project_root: Path, timeout_seconds: int = 900) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "passed"}

def parse_pytest_output(output_text: str) -> dict:
    return {"parsed": True}

def build_test_health_table(test_discovery_df: pd.DataFrame, pytest_summary: dict | None = None) -> pd.DataFrame:
    return pd.DataFrame([{"test_file": "tests/test_mock.py"}])

def summarize_test_health(test_health_df: pd.DataFrame) -> dict:
    return {"health": "good"}
