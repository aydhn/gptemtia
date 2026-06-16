import pytest
import pandas as pd
from local_knowledge_graph.graph_validation import (
    validate_graph_nodes,
    validate_graph_edges,
    validate_semantic_index,
    validate_relationship_queries,
    validate_no_external_vector_or_cloud_usage
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_graph_validation():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    assert validate_graph_nodes(df, profile) is not None
    assert validate_graph_edges(df, df, profile) is not None
    assert validate_semantic_index(df, {}, profile) is not None
    assert validate_relationship_queries(df, profile) is not None
    assert validate_no_external_vector_or_cloud_usage() is not None
