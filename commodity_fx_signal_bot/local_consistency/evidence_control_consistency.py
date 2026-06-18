from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def load_evidence_control_tables(project_root: Path) -> dict[str, pd.DataFrame]:
    return {}

def compare_controls_to_evidence_mappings(tables: dict[str, pd.DataFrame], profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_controls_without_evidence(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_evidence_without_control_reference(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def build_evidence_control_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    tables = load_evidence_control_tables(project_root)
    return compare_controls_to_evidence_mappings(tables, profile)
