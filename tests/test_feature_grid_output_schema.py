import pandas as pd
from advanced_feature_grid.feature_grid_output_schema import (
    build_feature_grid_output_schema_registry,
    validate_feature_grid_output_schema,
    summarize_feature_grid_output_schema,
)


def test_feature_grid_output_schema():
    df, summary = build_feature_grid_output_schema_registry()
    assert not df.empty
    assert summary["all_numeric"] is True
    assert summary["warmup_nan_expected"] is True

    # Test validation
    test_df = pd.DataFrame({
        "sma_w20": [1.0, 2.0, 3.0],
        "rsi_w14": [45.0, 50.0, 55.0],
    })
    res = validate_feature_grid_output_schema(test_df, ["sma_w20", "rsi_w14"])
    assert res["valid"] is True

    # Test invalid schema (forbidden term)
    invalid_df = pd.DataFrame({
        "prediction_w20": [1.0, 2.0, 3.0]
    })
    res_inv = validate_feature_grid_output_schema(invalid_df, ["prediction_w20"])
    assert res_inv["valid"] is False
