from advanced_feature_grid.volatility_window_grid import (
    build_volatility_window_grid_registry,
    summarize_volatility_window_grid,
)


def test_volatility_window_grid():
    df, summary = build_volatility_window_grid_registry()
    assert not df.empty
    assert summary["total_grid_features"] >= 10
    assert summary["non_signal"] is True

    indicators = list(df["indicator_name"].unique())
    assert "atr" in indicators
    assert "rolling_std" in indicators
    assert "realized_volatility" in indicators
