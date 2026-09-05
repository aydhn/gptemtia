from advanced_feature_grid.feature_grid_naming import (
    build_feature_grid_naming_registry,
    build_feature_grid_column_name,
    validate_feature_grid_column_name,
    summarize_feature_grid_naming,
)


def test_feature_grid_naming():
    df, summary = build_feature_grid_naming_registry()
    assert not df.empty
    assert summary["naming_standard"] == "lowercase_snake_case"

    # Test column name builder
    name1 = build_feature_grid_column_name("sma", {"window": 20})
    assert name1 == "sma_w20"

    name2 = build_feature_grid_column_name("rsi", {"window": 14})
    assert name2 == "rsi_w14"

    name3 = build_feature_grid_column_name("bb", {"window": 20, "num_std": 2.0}, subcomponent="width")
    assert name3 == "bb_width_w20_std2"

    # Test validation
    res_valid = validate_feature_grid_column_name("ema_w50")
    assert res_valid["valid"] is True

    # Test forbidden words
    res_forbidden = validate_feature_grid_column_name("buy_signal_rsi_w14")
    assert res_forbidden["valid"] is False
    assert len(res_forbidden["errors"]) >= 1

    res_target = validate_feature_grid_column_name("target_return_w5")
    assert res_target["valid"] is False
