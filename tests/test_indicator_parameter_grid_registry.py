from advanced_feature_grid.indicator_parameter_grid_registry import (
    build_indicator_parameter_grid_registry,
    expand_parameter_grid,
    summarize_indicator_parameter_grids,
)


def test_indicator_parameter_grid_registry():
    df, summary = build_indicator_parameter_grid_registry()
    assert not df.empty
    assert summary["total_grids"] >= 8
    assert summary["total_expected_features"] > 30

    names = list(df["indicator_name"])
    for expected in ["sma", "ema", "rsi", "atr", "bollinger", "donchian", "rolling_zscore", "simple_return"]:
        assert expected in names

    # Test expansion
    grid = {"window": [10, 20], "std": [1.5, 2.0]}
    expanded = expand_parameter_grid(grid)
    assert len(expanded) == 4
