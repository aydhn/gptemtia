from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.lineage_graph_placeholder import (
    build_lineage_graph_placeholder,
    summarize_lineage_graph_placeholder,
)


def test_lineage_graph_placeholder():
    profile = get_default_data_lineage_profile()
    df, summary = build_lineage_graph_placeholder(profile)
    assert len(df) >= 10
    assert summary["is_vector_db"] is False
    assert summary["is_graph_db"] is False
    assert "provided_by" in summary["relationships"]
