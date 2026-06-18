from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def build_stale_artifact_reconciliation_plan(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def identify_stale_artifacts_from_timeline(project_root: Path, profile: LocalConsistencyProfile) -> pd.DataFrame:
    return pd.DataFrame()

def identify_stale_docs_vs_outputs(project_root: Path, profile: LocalConsistencyProfile) -> pd.DataFrame:
    return pd.DataFrame()

def identify_stale_reports_vs_datalake(project_root: Path, profile: LocalConsistencyProfile) -> pd.DataFrame:
    return pd.DataFrame()

def classify_reconciliation_status(row: pd.Series, profile: LocalConsistencyProfile) -> str:
    return "reconciliation_unknown"

def summarize_stale_reconciliation(plan_df: pd.DataFrame) -> dict:
    return {}
