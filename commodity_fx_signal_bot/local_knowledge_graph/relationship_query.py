import pandas as pd
from typing import Tuple, Dict, Optional
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile
from local_knowledge_graph.graph_models import RelationshipQuery
from local_knowledge_graph.graph_models import build_relationship_query_id

def parse_relationship_query(query_text: str, profile: LocalKnowledgeGraphProfile) -> RelationshipQuery:
    return RelationshipQuery(
        query_id=build_relationship_query_id(query_text),
        query_text=query_text,
        query_intent=classify_relationship_query_intent(query_text),
        matched_terms=[],
        filters={},
        warnings=[]
    )

def classify_relationship_query_intent(query_text: str) -> str:
    text = query_text.lower()
    if "al" in text or "sat" in text:
        return "unknown_query" # Or direct to safe non-use policy
    return "find_reports_query"

def execute_relationship_query(
    query: RelationshipQuery,
    node_df: pd.DataFrame,
    edge_df: pd.DataFrame,
    keyword_df: Optional[pd.DataFrame] = None,
    tfidf_index: Optional[Dict] = None,
    profile: Optional[LocalKnowledgeGraphProfile] = None
) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame(), {"warnings": ["Not fully implemented"]}

def rank_relationship_query_results(results_df: pd.DataFrame) -> pd.DataFrame:
    return results_df

def build_relationship_query_examples(profile: LocalKnowledgeGraphProfile) -> pd.DataFrame:
    examples = [
        {"query": "GC=F ile ilgili hangi raporlar ve card'lar var?", "intent": "find_reports_query"},
        {"query": "scenario regression çıktıları hangi evidence dosyalarına bağlı?", "intent": "find_evidence_query"}
    ]
    return pd.DataFrame(examples)

def summarize_relationship_query_results(results_df: pd.DataFrame) -> Dict:
    return {"result_count": len(results_df) if results_df is not None else 0}
