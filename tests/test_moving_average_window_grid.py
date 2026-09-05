from advanced_feature_grid.moving_average_window_grid import (
    build_moving_average_window_grid_registry,
    summarize_moving_average_window_grid,
)


def test_moving_average_window_grid():
    df, summary = build_moving_average_window_grid_registry()
    assert not df.empty
    assert summary["total_grid_features"] >= 15
    assert summary["non_signal"] is True

    indicators = list(df["indicator_name"].unique())
    assert "sma" in indicators
    assert "ema" in indicators
    assert "wma" in indicators

    cols = list(df["column_name"])
    assert "sma_w20" in cols
    assert "ema_w50" in cols
