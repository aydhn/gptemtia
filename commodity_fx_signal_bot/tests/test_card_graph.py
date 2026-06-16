import pytest
import pandas as pd
from local_knowledge_graph.card_graph import (
    build_card_relationship_graph,
    link_cards_to_artifacts,
    link_cards_to_limitations_and_non_use
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_card_graph():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    g_df, sum_ = build_card_relationship_graph(df, df, profile)
    assert g_df is not None

    s_df = link_cards_to_artifacts(df, df)
    assert s_df is not None

    sum_df = link_cards_to_limitations_and_non_use(df, df)
    assert sum_df is not None
