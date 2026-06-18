from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def load_metadata_artifact_tables(project_root: Path) -> dict[str, pd.DataFrame]:
    return {}

def compare_cards_to_artifacts(tables: dict[str, pd.DataFrame], profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_card_without_artifact(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_artifact_without_required_cards(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_card_missing_non_use_policy(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def build_metadata_artifact_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    tables = load_metadata_artifact_tables(project_root)
    return compare_cards_to_artifacts(tables, profile)
