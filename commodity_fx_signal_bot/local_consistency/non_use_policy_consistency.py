from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def scan_outputs_for_non_use_policy(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def check_required_non_use_policy_terms(text: str) -> dict:
    return {}

def build_non_use_policy_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return scan_outputs_for_non_use_policy(project_root, profile)

def summarize_non_use_policy_consistency(non_use_df: pd.DataFrame) -> dict:
    return {}
