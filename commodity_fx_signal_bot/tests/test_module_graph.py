import pytest
import pandas as pd
from local_knowledge_graph.module_graph import (
    build_module_relationship_graph,
    build_module_edge_summary,
    identify_cross_module_relationships
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_module_graph():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    g_df, sum_ = build_module_relationship_graph(df, df, profile)
    assert g_df is not None

    sum_df = build_module_edge_summary(df, df)
    assert sum_df is not None

    cross_df = identify_cross_module_relationships(df, df)
    assert cross_df is not None
