import pytest
import pandas as pd
from advanced_feature_validation.feature_grid_output_validation import validate_feature_grid_outputs


def test_feature_grid_output_validation():
    valid_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "grid_ret_5d": [0.01, 0.02, -0.01, 0.03, 0.0],
        "grid_vol_20d": [0.15, 0.16, 0.14, 0.15, 0.17],
    })
    res_valid = validate_feature_grid_outputs(valid_df)
    assert res_valid["is_valid"] is True
    assert res_valid["current_phase"] == 121

    # Negative volatility should fail
    invalid_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "grid_vol_20d": [0.15, -0.16, 0.14, 0.15, 0.17],
    })
    res_invalid = validate_feature_grid_outputs(invalid_df)
    assert res_invalid["is_valid"] is False
