import pytest
import pandas as pd
from local_knowledge_graph.report_graph import (
    build_report_relationship_graph,
    link_reports_to_source_artifacts,
    link_reports_to_summaries
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_report_graph():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    g_df, sum_ = build_report_relationship_graph(df, df, profile)
    assert g_df is not None

    s_df = link_reports_to_source_artifacts(df, df)
    assert s_df is not None

    sum_df = link_reports_to_summaries(df, df)
    assert sum_df is not None
