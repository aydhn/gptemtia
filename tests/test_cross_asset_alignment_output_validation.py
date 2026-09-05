import pytest
import pandas as pd
from advanced_feature_validation.cross_asset_alignment_output_validation import validate_cross_asset_alignment_outputs


def test_cross_asset_alignment_output_validation():
    valid_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "fx_usdtry_close": [30.1, 30.2, 30.3, 30.4, 30.5],
        "com_brent_close": [80.0, 81.0, 80.5, 82.0, 81.5],
    })
    res_valid = validate_cross_asset_alignment_outputs(valid_df)
    assert res_valid["is_valid"] is True
    assert res_valid["current_phase"] == 121

    # Misaligned indices/missing timestamps
    invalid_df = pd.DataFrame({
        "timestamp": [pd.NaT, pd.Timestamp("2024-01-02")],
        "fx_usdtry_close": [30.1, 30.2],
    })
    res_invalid = validate_cross_asset_alignment_outputs(invalid_df)
    assert res_invalid["is_valid"] is False
