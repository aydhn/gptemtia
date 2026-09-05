import pandas as pd
from advanced_feature_grid.feature_grid_validation_rules import (
    build_feature_grid_validation_rule_registry,
    validate_feature_grid_dataframe,
    validate_feature_grid_output_no_forbidden_columns,
    validate_feature_grid_output_numeric_sanity,
    validate_feature_grid_output_count,
    summarize_feature_grid_validation_rules,
)


def test_feature_grid_validation_rules():
    df, summary = build_feature_grid_validation_rule_registry()
    assert not df.empty
    assert summary["all_enforced"] is True

    # Test clean dataframe
    clean_df = pd.DataFrame({"sma_w20": [1.0, 2.0], "rsi_w14": [50.0, 60.0]})
    res_clean = validate_feature_grid_dataframe(clean_df)
    assert res_clean["valid"] is True

    # Test forbidden column in dataframe
    bad_df = pd.DataFrame({"sma_w20": [1.0], "buy_signal": [1]})
    res_bad = validate_feature_grid_dataframe(bad_df)
    assert res_bad["valid"] is False

    # Test numeric sanity
    res_num = validate_feature_grid_output_numeric_sanity(clean_df, ["sma_w20", "rsi_w14"])
    assert res_num["valid"] is True

    # Test min count
    res_cnt = validate_feature_grid_output_count(clean_df, expected_min_count=2)
    assert res_cnt["valid"] is True
