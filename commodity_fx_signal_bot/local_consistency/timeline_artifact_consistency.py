from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def load_timeline_and_artifact_tables(project_root: Path) -> dict[str, pd.DataFrame]:
    return {}

def compare_timeline_events_to_artifacts(tables: dict[str, pd.DataFrame], profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_artifact_without_timeline_event(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_timeline_event_without_existing_artifact(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_stale_timeline_vs_metadata(tables: dict[str, pd.DataFrame], profile: LocalConsistencyProfile) -> pd.DataFrame:
    return pd.DataFrame()

def build_timeline_artifact_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    tables = load_timeline_and_artifact_tables(project_root)
    return compare_timeline_events_to_artifacts(tables, profile)
