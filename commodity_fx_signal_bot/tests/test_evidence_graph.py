import pytest
import pandas as pd
from local_knowledge_graph.evidence_graph import (
    build_evidence_relationship_graph,
    link_controls_to_evidence_nodes,
    link_policies_to_controls
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_evidence_graph():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    g_df, sum_ = build_evidence_relationship_graph(df, df, profile)
    assert g_df is not None

    s_df = link_controls_to_evidence_nodes(df, df)
    assert s_df is not None

    sum_df = link_policies_to_controls(df, df)
    assert sum_df is not None
