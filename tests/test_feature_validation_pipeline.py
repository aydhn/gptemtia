import pytest
import pandas as pd
from advanced_feature_validation.feature_validation_pipeline import run_feature_validation_pipeline


def test_feature_validation_pipeline():
    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=10),
        "asset_symbol": ["BRENT"] * 10,
        "feat_rsi_14": [45.0, 50.0, 52.0, 48.0, 53.0, 55.0, 57.0, 54.0, 52.0, 56.0],
    })

    result = run_feature_validation_pipeline(sample_df, profile_name="default")
    assert result["current_phase"] == 121
    assert result["target_final_phase"] == 160
    assert result["next_phase"] == 122
    assert "scores" in result
    assert result["scores"]["overall_score"] >= 0.8
    assert result["status"] in ["PASS", "WARNING", "FAIL"]
