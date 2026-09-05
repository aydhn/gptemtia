from advanced_feature_grid.return_window_grid import (
    build_return_window_grid_registry,
    summarize_return_window_grid,
)


def test_return_window_grid():
    df, summary = build_return_window_grid_registry()
    assert not df.empty
    assert summary["total_grid_features"] >= 10
    assert summary["non_signal"] is True

    indicators = list(df["indicator_name"].unique())
    assert "simple_return" in indicators
    assert "log_return" in indicators
    assert "cumulative_return" in indicators
