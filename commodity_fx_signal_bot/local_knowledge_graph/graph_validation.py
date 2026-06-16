import pandas as pd
from typing import Tuple, Dict, Optional
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile

def validate_graph_nodes(node_df: pd.DataFrame, profile: LocalKnowledgeGraphProfile) -> Dict:
    return {"warnings": []}

def validate_graph_edges(edge_df: pd.DataFrame, node_df: pd.DataFrame, profile: LocalKnowledgeGraphProfile) -> Dict:
    return {"warnings": []}

def validate_semantic_index(keyword_df: Optional[pd.DataFrame], tfidf_manifest: Optional[Dict], profile: LocalKnowledgeGraphProfile) -> Dict:
    return {"warnings": []}

def validate_relationship_queries(results_df: Optional[pd.DataFrame], profile: LocalKnowledgeGraphProfile) -> Dict:
    return {"warnings": []}

def validate_no_external_vector_or_cloud_usage(text: Optional[str] = None, df: Optional[pd.DataFrame] = None, summary: Optional[Dict] = None) -> Dict:
    return {"warnings": []}

def build_graph_validation_report(tables: Dict[str, pd.DataFrame], profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}
