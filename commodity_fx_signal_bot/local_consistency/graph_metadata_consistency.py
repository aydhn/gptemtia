from pathlib import Path

import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def load_graph_and_metadata_tables(project_root: Path) -> dict[str, pd.DataFrame]:
    return {}

def compare_graph_nodes_to_metadata_artifacts(tables: dict[str, pd.DataFrame], profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def detect_graph_node_without_metadata(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_metadata_artifact_without_graph_node(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def detect_graph_edge_to_missing_artifact(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    return pd.DataFrame()

def build_graph_metadata_consistency_report(project_root: Path, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    tables = load_graph_and_metadata_tables(project_root)
    return compare_graph_nodes_to_metadata_artifacts(tables, profile)
