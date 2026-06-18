from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def build_contradiction_rule_registry() -> pd.DataFrame:
    return pd.DataFrame([{"rule": "mock"}])

def scan_texts_for_contradictions(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_pairwise_contradictions(statement_df: pd.DataFrame, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def classify_contradiction_severity(source_statement: str, target_statement: str, contradiction_type: str) -> str:
    return "unknown_contradiction"

def build_contradiction_detection_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    statement_df, summary = scan_texts_for_contradictions(project_root, profile)
    return detect_pairwise_contradictions(statement_df, profile)
