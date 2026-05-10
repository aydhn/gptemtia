import pytest
import pandas as pd
from ml_integration.integration_config import get_default_ml_integration_profile
from ml_integration.model_uncertainty_filter import (
    detect_high_ml_uncertainty,
    calculate_uncertainty_adjusted_support,
)

def test_uncertainty_filter():
    profile = get_default_ml_integration_profile()

    ml_high = pd.Series({"uncertainty_score": 0.9})
    res_high = detect_high_ml_uncertainty(ml_high, profile)
    assert res_high["ml_uncertainty_high"] is True

    ml_low = pd.Series({"uncertainty_score": 0.2})
    res_low = detect_high_ml_uncertainty(ml_low, profile)
    assert res_low["ml_uncertainty_high"] is False

    ml_miss = None
    res_miss = detect_high_ml_uncertainty(ml_miss, profile)
    assert "Missing" in res_miss["ml_uncertainty_warning"]

def test_uncertainty_adjusted_support():
    profile = get_default_ml_integration_profile()
    # default max is 0.70
    assert calculate_uncertainty_adjusted_support(0.8, 0.5, profile) == 0.8
    adj = calculate_uncertainty_adjusted_support(0.8, 0.85, profile)
    assert adj < 0.8
