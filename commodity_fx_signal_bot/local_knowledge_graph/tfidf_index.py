import pandas as pd
from pathlib import Path
from typing import Tuple, Dict
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile

def build_local_tfidf_index(node_df: pd.DataFrame, project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[Dict, Dict]:
    return {}, {"warnings": ["sklearn fallback not implemented"]}

def build_tfidf_index_manifest(tfidf_index: Dict, profile: LocalKnowledgeGraphProfile) -> Dict:
    return {"status": "fallback"}

def search_tfidf_index(query_text: str, tfidf_index: Dict, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def summarize_tfidf_index(tfidf_index: Dict) -> Dict:
    return {"index_size": len(tfidf_index) if tfidf_index else 0}
