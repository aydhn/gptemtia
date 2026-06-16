import pandas as pd
from typing import Dict, Optional

def build_graph_disclaimer() -> str:
    return "Bu rapor offline/local knowledge graph ve artifact relationship çıktısıdır; canlı sinyal, broker talimatı, external vector DB, model deployment, production scheduler veya yatırım tavsiyesi değildir."

def build_graph_node_edge_registry_markdown_report(summary: Dict, node_df: Optional[pd.DataFrame] = None, edge_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Graph Node Edge Registry Report\n\n{build_graph_disclaimer()}\n"

def build_artifact_relationship_graph_markdown_report(summary: Dict, graph_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Artifact Relationship Graph Report\n\n{build_graph_disclaimer()}\n"

def build_semantic_index_markdown_report(summary: Dict, keyword_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Semantic Index Report\n\n{build_graph_disclaimer()}\n"

def build_relationship_query_markdown_report(summary: Dict, results_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Relationship Query Report\n\n{build_graph_disclaimer()}\n"

def build_graph_analysis_markdown_report(summary: Dict, centrality_df: Optional[pd.DataFrame] = None, gap_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Graph Analysis Report\n\n{build_graph_disclaimer()}\n"

def build_graph_quality_markdown_report(summary: Dict, quality: Optional[Dict] = None) -> str:
    return f"# Graph Quality Report\n\n{build_graph_disclaimer()}\n"

def build_graph_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Graph Status Report\n\n{build_graph_disclaimer()}\n"
