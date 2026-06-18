from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def scan_reports_and_docs_for_disclaimers(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def check_required_disclaimer_concepts(text: str, domain: str) -> dict:
    return {}

def build_disclaimer_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return scan_reports_and_docs_for_disclaimers(project_root, profile)

def summarize_disclaimer_consistency(disclaimer_df: pd.DataFrame) -> dict:
    return {}
