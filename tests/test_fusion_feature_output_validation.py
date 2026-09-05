import pytest
import pandas as pd
from advanced_feature_validation.fusion_feature_output_validation import validate_fusion_feature_outputs


def test_fusion_feature_output_validation():
    valid_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "macro_cpi_mom": [0.003, 0.002, 0.004, 0.003, 0.005],
        "calendar_event_days_until": [5, 4, 3, 2, 1],
    })
    res_valid = validate_fusion_feature_outputs(valid_df)
    assert res_valid["is_valid"] is True
    assert res_valid["current_phase"] == 121

    # Forbidden article body in fusion outputs
    invalid_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "article_body": ["text", "text", "text", "text", "text"],
    })
    res_invalid = validate_fusion_feature_outputs(invalid_df)
    assert res_invalid["is_valid"] is False
