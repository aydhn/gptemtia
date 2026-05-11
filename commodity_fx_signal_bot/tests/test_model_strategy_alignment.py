import pytest
import pandas as pd
from ml_integration.integration_config import get_default_ml_integration_profile
from ml_integration.model_strategy_alignment import calculate_model_strategy_alignment

def test_strategy_alignment():
    profile = get_default_ml_integration_profile()

    str_trend = pd.Series({"candidate_type": "long_entry", "strategy_family": "trend_following"})
    ml_up = pd.Series({"predicted_direction": "up", "confidence_score": 0.8})
    res = calculate_model_strategy_alignment(str_trend, ml_up, profile)
    assert res["alignment_label"] == "model_aligned_with_candidate"

    str_mean = pd.Series({"candidate_type": "neutral", "strategy_family": "mean_reversion"})
    ml_flat = pd.Series({"predicted_direction": "flat", "confidence_score": 0.8})
    res2 = calculate_model_strategy_alignment(str_mean, ml_flat, profile)
    assert res2["alignment_label"] == "model_aligned_with_candidate"
