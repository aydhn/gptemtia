import pytest
import pandas as pd
from local_knowledge_graph.graph_gap_detection import (
    detect_graph_gaps,
    detect_orphan_artifact_gaps,
    detect_missing_expected_relationships,
    detect_stale_relationships
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_graph_gap_detection():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    g_df = detect_graph_gaps(df, df, profile)
    assert g_df is not None

    o_df = detect_orphan_artifact_gaps(df, df)
    assert o_df is not None

    m_df = detect_missing_expected_relationships(df, df)
    assert m_df is not None

    s_df = detect_stale_relationships(df, df, profile)
    assert s_df is not None
