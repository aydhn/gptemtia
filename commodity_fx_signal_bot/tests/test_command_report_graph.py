import pytest
import pandas as pd
from local_knowledge_graph.command_report_graph import (
    build_command_report_relationship_graph,
    link_commands_to_expected_outputs,
    link_aliases_to_scripts_and_reports
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_command_report_graph():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    g_df, sum_ = build_command_report_relationship_graph(df, df, profile)
    assert g_df is not None

    s_df = link_commands_to_expected_outputs(df, df)
    assert s_df is not None

    sum_df = link_aliases_to_scripts_and_reports(df, df)
    assert sum_df is not None
