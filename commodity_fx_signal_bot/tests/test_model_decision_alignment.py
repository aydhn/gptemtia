import pytest
import pandas as pd
from ml_integration.integration_config import get_default_ml_integration_profile
from ml_integration.model_decision_alignment import calculate_model_decision_alignment

def test_decision_alignment():
    profile = get_default_ml_integration_profile()

    dec_long = pd.Series({"candidate_type": "long_bias_candidate"})
    ml_up = pd.Series({"predicted_direction": "up", "confidence_score": 0.8})
    res = calculate_model_decision_alignment(dec_long, ml_up, profile)
    assert res["alignment_label"] == "model_aligned_with_candidate"

    dec_short = pd.Series({"candidate_type": "short_bias_candidate"})
    res2 = calculate_model_decision_alignment(dec_short, ml_up, profile)
    assert res2["alignment_label"] == "model_conflicts_with_candidate"

    dec_neut = pd.Series({"candidate_type": "no_trade"})
    ml_flat = pd.Series({"predicted_direction": "flat", "confidence_score": 0.8})
    res3 = calculate_model_decision_alignment(dec_neut, ml_flat, profile)
    assert res3["alignment_label"] == "model_aligned_with_candidate"
