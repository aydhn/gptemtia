from advanced_feature_grid.feature_grid_metadata_registry import (
    build_feature_grid_metadata_registry,
    summarize_feature_grid_metadata,
)


def test_feature_grid_metadata_registry():
    df, summary = build_feature_grid_metadata_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True
    assert summary["all_lookahead_checked"] is True
    assert summary["all_phase_119_ready"] is True
    assert (df["non_signal"] == True).all()
