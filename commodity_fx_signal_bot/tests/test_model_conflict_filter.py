import pytest
import pandas as pd
from ml_integration.integration_config import get_default_ml_integration_profile
from ml_integration.model_conflict_filter import detect_ml_candidate_conflict

def test_model_conflict_filter():
    profile = get_default_ml_integration_profile()

    dec_long = pd.Series({"candidate_type": "long_bias_candidate"})
    ml_down = pd.Series({"predicted_direction": "down", "confidence_score": 0.9})

    res = detect_ml_candidate_conflict(dec_long, ml_down, profile, "decision")
    assert res.conflict_score == 0.9
    assert res.conflict_label == "model_conflicts_with_candidate"

    ml_up = pd.Series({"predicted_direction": "up", "confidence_score": 0.9})
    res_no = detect_ml_candidate_conflict(dec_long, ml_up, profile, "decision")
    assert res_no.conflict_score == 0.0
    assert res_no.conflict_label == "no_conflict"

    ml_miss = None
    res_miss = detect_ml_candidate_conflict(dec_long, ml_miss, profile, "decision")
    assert res_miss.conflict_label == "model_unavailable_for_candidate"
