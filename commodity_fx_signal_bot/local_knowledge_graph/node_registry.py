import pandas as pd
from pathlib import Path
from typing import Tuple, Dict
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile
from local_knowledge_graph.graph_models import GraphNode, build_graph_node_id, graph_node_to_dict

def build_nodes_from_artifact_metadata(project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    # Placeholder
    return pd.DataFrame(), {"warnings": ["Missing source"]}

def build_nodes_from_evidence_governance(project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": ["Missing source"]}

def build_nodes_from_report_summaries(project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": ["Missing source"]}

def build_nodes_from_docs(project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    node = GraphNode(
        node_id=build_graph_node_id("document_node", "README"),
        node_type="document_node",
        label="README",
        module_name=None,
        relative_path="README.md",
        title="README",
        summary="Main repository documentation",
        metadata={},
        warnings=[]
    )
    return pd.DataFrame([graph_node_to_dict(node)]), {"warnings": []}

def build_nodes_from_commands(project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": ["Missing source"]}

def build_symbol_nodes(profile: LocalKnowledgeGraphProfile) -> pd.DataFrame:
    node = GraphNode(
        node_id=build_graph_node_id("symbol_node", "GC=F"),
        node_type="symbol_node",
        label="GC=F",
        module_name=None,
        relative_path=None,
        title="Gold",
        summary="Gold Symbol",
        metadata={},
        warnings=[]
    )
    return pd.DataFrame([graph_node_to_dict(node)])

def build_module_nodes(profile: LocalKnowledgeGraphProfile) -> pd.DataFrame:
    node = GraphNode(
        node_id=build_graph_node_id("module_node", "local_knowledge_graph"),
        node_type="module_node",
        label="local_knowledge_graph",
        module_name="local_knowledge_graph",
        relative_path=None,
        title="Local Knowledge Graph",
        summary="Module for local graph",
        metadata={},
        warnings=[]
    )
    return pd.DataFrame([graph_node_to_dict(node)])

def build_graph_node_registry(project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    dfs = []
    warnings = []

    df_meta, w_meta = build_nodes_from_artifact_metadata(project_root, profile)
    dfs.append(df_meta)
    warnings.extend(w_meta.get("warnings", []))

    df_ev, w_ev = build_nodes_from_evidence_governance(project_root, profile)
    dfs.append(df_ev)
    warnings.extend(w_ev.get("warnings", []))

    df_rep, w_rep = build_nodes_from_report_summaries(project_root, profile)
    dfs.append(df_rep)
    warnings.extend(w_rep.get("warnings", []))

    df_docs, w_docs = build_nodes_from_docs(project_root, profile)
    dfs.append(df_docs)
    warnings.extend(w_docs.get("warnings", []))

    df_cmd, w_cmd = build_nodes_from_commands(project_root, profile)
    dfs.append(df_cmd)
    warnings.extend(w_cmd.get("warnings", []))

    dfs.append(build_symbol_nodes(profile))
    dfs.append(build_module_nodes(profile))

    combined_df = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
    return combined_df, {"warnings": list(set(warnings)), "total_nodes": len(combined_df)}

def summarize_graph_nodes(node_df: pd.DataFrame) -> Dict:
    return {"node_count": len(node_df) if node_df is not None and not node_df.empty else 0}
