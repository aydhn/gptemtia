from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile
from local_consistency.consistency_models import ConsistencyFinding


def scan_outputs_for_safety_boundary_consistency(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_forbidden_safety_boundary_claims(text: str, relative_path: str) -> list[ConsistencyFinding]:
    return []

def detect_missing_safety_boundary_language(text: str, relative_path: str, domain: str) -> list[ConsistencyFinding]:
    return []

def build_safety_boundary_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return scan_outputs_for_safety_boundary_consistency(project_root, profile)

def summarize_safety_boundary_consistency(safety_df: pd.DataFrame) -> dict:
    return {}
