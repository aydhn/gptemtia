import pytest
import pandas as pd
from local_knowledge_graph.graph_quality import (
    check_node_registry_quality,
    check_edge_registry_quality,
    check_semantic_index_quality,
    check_graph_analysis_quality,
    check_graph_export_quality,
    check_for_forbidden_terms_in_graph,
    build_graph_quality_report
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_graph_quality():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    assert check_node_registry_quality(df, profile) is not None
    assert check_edge_registry_quality(df, df, profile) is not None
    assert check_semantic_index_quality(df, {}, profile) is not None
    assert check_graph_analysis_quality(df, df, profile) is not None
    assert check_graph_export_quality({}, profile) is not None

    f_res = check_for_forbidden_terms_in_graph(text="pinecone")
    assert f_res is not None

    q_rep = build_graph_quality_report({})
    assert "passed" in q_rep
