import pytest
import pandas as pd
from ml_integration.integration_config import get_default_ml_integration_profile
from ml_integration.model_signal_alignment import calculate_model_signal_alignment

def test_signal_alignment():
    profile = get_default_ml_integration_profile()

    sig = pd.Series({"directional_bias": "bullish"})
    ml_up = pd.Series({"predicted_direction": "up", "confidence_score": 0.8})

    res = calculate_model_signal_alignment(sig, ml_up, profile)
    assert res["alignment_label"] == "model_aligned_with_candidate"

    ml_down = pd.Series({"predicted_direction": "down", "confidence_score": 0.8})
    res_conflict = calculate_model_signal_alignment(sig, ml_down, profile)
    assert res_conflict["alignment_label"] == "model_conflicts_with_candidate"

    res_miss = calculate_model_signal_alignment(sig, None, profile)
    assert res_miss["alignment_label"] == "model_unavailable_for_candidate"
