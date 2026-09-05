from advanced_feature_grid.mean_reversion_window_grid import (
    build_mean_reversion_window_grid_registry,
    summarize_mean_reversion_window_grid,
)


def test_mean_reversion_window_grid():
    df, summary = build_mean_reversion_window_grid_registry()
    assert not df.empty
    assert summary["total_grid_features"] >= 10
    assert summary["non_signal"] is True

    indicators = list(df["indicator_name"].unique())
    assert "rolling_zscore" in indicators
    assert "distance_to_sma" in indicators
    assert "distance_to_ema" in indicators
