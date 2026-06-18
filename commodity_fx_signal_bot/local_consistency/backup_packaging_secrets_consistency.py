from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def load_backup_packaging_secrets_tables(project_root: Path) -> dict[str, pd.DataFrame]:
    return {}

def compare_backup_packaging_secret_boundaries(tables: dict[str, pd.DataFrame], profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_secret_inclusion_contradictions(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_manifest_only_policy_contradictions(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_backup_packaging_boundary_gaps(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def build_backup_packaging_secrets_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    tables = load_backup_packaging_secrets_tables(project_root)
    return compare_backup_packaging_secret_boundaries(tables, profile)
