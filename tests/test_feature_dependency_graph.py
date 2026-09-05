from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_dependency_graph import (
    build_feature_dependency_graph_placeholder,
    summarize_feature_dependency_graph,
)


def test_feature_dependency_graph():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_dependency_graph_placeholder(profile)

    assert not df.empty
    assert len(df) >= 10
    assert "source_node" in df.columns
    assert "target_node" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["external_database_required"] is False
