from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile
from local_consistency.consistency_models import ReferenceFinding


def extract_path_references_from_text(text: str, source_path: str) -> list[ReferenceFinding]:
    return []

def scan_docs_reports_for_references(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def validate_reference_paths(reference_df: pd.DataFrame, project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_broken_internal_references(reference_df: pd.DataFrame, project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_report_references(reference_df: pd.DataFrame, project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def build_missing_and_broken_reference_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    reference_df, summary = scan_docs_reports_for_references(project_root, profile)
    return validate_reference_paths(reference_df, project_root)
