from advanced_feature_grid.range_channel_window_grid import (
    build_range_channel_window_grid_registry,
    summarize_range_channel_window_grid,
)


def test_range_channel_window_grid():
    df, summary = build_range_channel_window_grid_registry()
    assert not df.empty
    assert summary["total_grid_features"] >= 20
    assert summary["non_signal"] is True

    indicators = list(df["indicator_name"].unique())
    assert "bollinger" in indicators
    assert "donchian" in indicators
