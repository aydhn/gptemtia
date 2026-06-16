import pandas as pd
from typing import Tuple, Dict
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile

def build_scenario_regression_relationship_graph(node_df: pd.DataFrame, edge_df: pd.DataFrame, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def link_scenarios_to_regressions(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def link_regressions_to_golden_snapshots_replays(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_scenario_regression_relationship_graph(graph_df: pd.DataFrame) -> Dict:
    return {"scenario_regression_relationships": len(graph_df) if graph_df is not None else 0}
