import pytest
import pandas as pd
from local_knowledge_graph.relationship_query import (
    parse_relationship_query,
    classify_relationship_query_intent,
    execute_relationship_query
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_relationship_query():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")

    q = parse_relationship_query("test query", profile)
    assert q.query_text == "test query"

    i1 = classify_relationship_query_intent("al sat")
    assert i1 == "unknown_query"

    i2 = classify_relationship_query_intent("hangi raporlar var")
    assert i2 == "find_reports_query"

    df = pd.DataFrame()
    s_df, _ = execute_relationship_query(q, df, df, None, None, profile)
    assert s_df is not None
