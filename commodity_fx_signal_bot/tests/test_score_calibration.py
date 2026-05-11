import pytest
from ml.score_calibration import (
    normalize_classification_confidence,
    normalize_regression_score,
    calculate_calibrated_prediction_score
)

def test_normalize_classification_confidence():
    assert normalize_classification_confidence({"up": 0.8, "down": 0.2}) == 0.8
    assert normalize_classification_confidence({}) == 0.5

def test_normalize_regression_score():
    assert normalize_regression_score(0.0) == 0.5
    assert normalize_regression_score(0.05) == 1.0
    assert normalize_regression_score(-0.05) == 0.0
    assert normalize_regression_score(0.025) == 0.75

    # With reference volatility
    assert normalize_regression_score(0.0, 0.02) == 0.5
    assert normalize_regression_score(0.04, 0.02) > 0.8
