from advanced_feature_grid.momentum_window_grid import (
    build_momentum_window_grid_registry,
    summarize_momentum_window_grid,
)


def test_momentum_window_grid():
    df, summary = build_momentum_window_grid_registry()
    assert not df.empty
    assert summary["total_grid_features"] >= 10
    assert summary["non_signal"] is True

    indicators = list(df["indicator_name"].unique())
    assert "rsi" in indicators
    assert "roc" in indicators
    assert "momentum" in indicators
