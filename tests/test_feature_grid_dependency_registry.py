from advanced_feature_grid.feature_grid_dependency_registry import (
    build_feature_grid_dependency_registry,
    summarize_feature_grid_dependency_registry,
)


def test_feature_grid_dependency_registry():
    df, summary = build_feature_grid_dependency_registry()
    assert not df.empty
    assert summary["no_forward_dependencies"] is True
    assert summary["total_dependencies"] >= 8

    grids = list(df["grid_name"])
    assert "sma_window_grid" in grids
    assert "atr_window_grid" in grids
    assert "bollinger_window_grid" in grids
