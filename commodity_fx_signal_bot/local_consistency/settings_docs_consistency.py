from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def extract_documented_settings(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def compare_settings_to_docs(settings_df: pd.DataFrame, docs_df: pd.DataFrame, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_undocumented_settings(settings_df: pd.DataFrame, docs_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_stale_documented_settings(settings_df: pd.DataFrame, docs_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_settings_docs_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    from local_consistency.config_env_consistency import extract_settings_fields
    settings_df = extract_settings_fields(project_root)
    docs_df = extract_documented_settings(project_root)
    return compare_settings_to_docs(settings_df, docs_df, profile)
