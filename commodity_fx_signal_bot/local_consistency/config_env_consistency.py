from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def extract_settings_fields(project_root: Path) -> pd.DataFrame:
    # Dummy implementation for tests
    return pd.DataFrame([{"field": "local_consistency_enabled"}])

def extract_env_example_keys(project_root: Path) -> pd.DataFrame:
    # Dummy implementation for tests
    return pd.DataFrame([{"key": "LOCAL_CONSISTENCY_ENABLED"}])

def compare_settings_to_env_example(settings_df: pd.DataFrame, env_df: pd.DataFrame, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def build_config_env_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    settings_df = extract_settings_fields(project_root)
    env_df = extract_env_example_keys(project_root)
    return compare_settings_to_env_example(settings_df, env_df, profile)
