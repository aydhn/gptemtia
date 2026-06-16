import pytest
import pandas as pd
from local_knowledge_graph.graph_builder import (
    build_artifact_relationship_graph,
    build_adjacency_table,
    build_node_degree_table,
    validate_graph_structure
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_graph_builder():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    ndf = pd.DataFrame()
    edf = pd.DataFrame()

    graph, sum_ = build_artifact_relationship_graph(ndf, edf, profile)
    assert "nodes" in graph
    assert "edges" in graph

    adj = build_adjacency_table(ndf, edf)
    assert adj is not None

    deg = build_node_degree_table(ndf, edf)
    assert deg is not None

    val = validate_graph_structure(ndf, edf)
    assert "warnings" in val
