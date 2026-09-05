import pytest
import pandas as pd
from advanced_feature_validation.indicator_output_validation import validate_indicator_outputs


def test_indicator_output_validation():
    valid_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "indicator_rsi_14": [45.0, 50.0, 55.0, 60.0, 65.0],
        "indicator_macd": [0.1, 0.2, 0.15, 0.25, 0.3],
    })
    res_valid = validate_indicator_outputs(valid_df)
    assert res_valid["is_valid"] is True
    assert res_valid["current_phase"] == 121

    # Out of range RSI (e.g. > 100)
    invalid_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "indicator_rsi_14": [45.0, 50.0, 155.0, 60.0, 65.0],
    })
    res_invalid = validate_indicator_outputs(invalid_df)
    assert res_invalid["is_valid"] is False
