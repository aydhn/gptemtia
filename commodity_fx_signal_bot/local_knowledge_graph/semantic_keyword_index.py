import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, List
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile

def build_local_semantic_keyword_index(node_df: pd.DataFrame, project_root: Path, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def tokenize_local_text(text: str) -> List[str]:
    return text.lower().split() if text else []

def extract_top_keywords(text: str, max_keywords: int = 20) -> List[str]:
    tokens = tokenize_local_text(text)
    return list(set(tokens))[:max_keywords]

def search_keyword_index(query_text: str, keyword_df: pd.DataFrame, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def summarize_keyword_index(keyword_df: pd.DataFrame) -> Dict:
    return {"keyword_count": len(keyword_df) if keyword_df is not None else 0}
