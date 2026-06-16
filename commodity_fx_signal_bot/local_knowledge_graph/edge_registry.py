import pandas as pd
from pathlib import Path
from typing import Tuple, Dict
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile
from local_knowledge_graph.graph_models import GraphEdge, build_graph_edge_id, graph_edge_to_dict

def build_edges_from_path_relationships(node_df: pd.DataFrame, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def build_edges_from_metadata_lineage(node_df: pd.DataFrame, project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def build_edges_from_evidence_mappings(node_df: pd.DataFrame, project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def build_edges_from_text_mentions(node_df: pd.DataFrame, project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def build_edges_from_symbol_mentions(node_df: pd.DataFrame, project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def build_graph_edge_registry(node_df: pd.DataFrame, project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    dfs = []
    warnings = []

    df1, w1 = build_edges_from_path_relationships(node_df, profile)
    dfs.append(df1)

    df2, w2 = build_edges_from_metadata_lineage(node_df, project_root, profile)
    dfs.append(df2)

    combined_df = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
    return combined_df, {"warnings": warnings, "total_edges": len(combined_df)}

def deduplicate_edges(edge_df: pd.DataFrame) -> pd.DataFrame:
    if edge_df is None or edge_df.empty:
        return edge_df
    return edge_df.drop_duplicates(subset=["source_node_id", "target_node_id", "edge_type"]).reset_index(drop=True)

def summarize_graph_edges(edge_df: pd.DataFrame) -> Dict:
    return {"edge_count": len(edge_df) if edge_df is not None and not edge_df.empty else 0}
