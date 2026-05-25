import pandas as pd
from pathlib import Path
from .quality_config import QualityGateProfile

def build_smoke_test_command_registry() -> pd.DataFrame:
    return pd.DataFrame()

def run_safe_smoke_command(command: str, project_root: Path, timeout_seconds: int = 120) -> dict:
    return {}

def run_smoke_tests(project_root: Path, profile: QualityGateProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def summarize_smoke_tests(smoke_df: pd.DataFrame) -> dict:
    return {}
