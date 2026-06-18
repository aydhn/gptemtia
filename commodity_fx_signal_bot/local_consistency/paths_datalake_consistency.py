from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def extract_paths_registry(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def extract_datalake_methods(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def compare_paths_to_datalake_methods(paths_df: pd.DataFrame, dl_df: pd.DataFrame, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_missing_datalake_save_load_pairs(dl_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_paths_datalake_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    paths_df = extract_paths_registry(project_root)
    dl_df = extract_datalake_methods(project_root)
    return compare_paths_to_datalake_methods(paths_df, dl_df, profile)
