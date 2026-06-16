import pytest
import pandas as pd
from local_knowledge_graph.graph_traversal import (
    get_node_neighbors,
    get_shortest_relationship_path,
    build_graph_neighborhood_report
)

def test_graph_traversal():
    df = pd.DataFrame()

    n_df = get_node_neighbors("id", df, df)
    assert n_df is not None

    p_df = get_shortest_relationship_path("id1", "id2", df)
    assert p_df is not None

    r_df, _ = build_graph_neighborhood_report("id", df, df)
    assert r_df is not None
