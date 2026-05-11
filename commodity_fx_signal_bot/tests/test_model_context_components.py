import pytest
import pandas as pd
from ml_integration.integration_config import get_default_ml_integration_profile
from ml_integration.model_context_components import (
    calculate_ml_context_quality_score,
    calculate_ml_support_score,
    calculate_ml_conflict_score,
    calculate_ml_uncertainty_penalty,
    calculate_ml_leakage_penalty,
)

def test_context_quality_score():
    profile = get_default_ml_integration_profile()
    row = pd.Series({"model_quality_score": 0.8, "dataset_quality_score": 0.8, "leakage_risk_score": 0.1})
    q = calculate_ml_context_quality_score(row, profile)
    assert 0.69 < q < 0.71  # (0.8+0.8)/2 - 0.1

def test_support_and_conflict():
    profile = get_default_ml_integration_profile()

    row_bull = pd.Series({"predicted_direction": "up", "confidence_score": 0.8})
    assert calculate_ml_support_score(row_bull, "bullish", profile) == 0.8
    assert calculate_ml_conflict_score(row_bull, "bearish", profile) == 0.8

    row_bear = pd.Series({"predicted_direction": "down", "confidence_score": 0.9})
    assert calculate_ml_support_score(row_bear, "bearish", profile) == 0.9
    assert calculate_ml_conflict_score(row_bear, "bullish", profile) == 0.9

def test_uncertainty_and_leakage():
    profile = get_default_ml_integration_profile()

    row = pd.Series({"uncertainty_score": 0.85, "leakage_risk_score": 0.5})
    # profile max_uncertainty is 0.7, so 0.85 is excess 0.15 over 0.3 -> penalty 0.5
    u_pen = calculate_ml_uncertainty_penalty(row, profile)
    assert u_pen > 0.0

    l_pen = calculate_ml_leakage_penalty(row, profile)
    assert l_pen > 0.0
