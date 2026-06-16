import pandas as pd
from typing import Tuple, Dict
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile

def build_card_relationship_graph(node_df: pd.DataFrame, edge_df: pd.DataFrame, profile: LocalKnowledgeGraphProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": []}

def link_cards_to_artifacts(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def link_cards_to_limitations_and_non_use(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_card_relationship_graph(card_graph_df: pd.DataFrame) -> Dict:
    return {"card_relationships": len(card_graph_df) if card_graph_df is not None else 0}
