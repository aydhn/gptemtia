import pytest
import pandas as pd
from ml.prediction_candidate import (
    build_prediction_id,
    build_prediction_candidate_from_row
)
from ml.prediction_config import MLPredictionProfile

def test_build_prediction_id():
    pid1 = build_prediction_id("A", "1d", "2020-01-01", "m1", "t1")
    pid2 = build_prediction_id("A", "1d", "2020-01-01", "m1", "t1")
    pid3 = build_prediction_id("B", "1d", "2020-01-01", "m1", "t1")

    assert pid1 == pid2
    assert pid1 != pid3

def test_build_prediction_candidate_from_row():
    profile = MLPredictionProfile(
        name="test", description="", dataset_profile="", training_profile="",
        allowed_model_families=("test",), uncertainty_warning_threshold=0.6,
        min_confidence_score=0.4
    )

    row = pd.Series({
        "symbol": "BTC",
        "timeframe": "1d",
        "timestamp": "2021-01-01",
        "model_id": "m1",
        "confidence_score": 0.8,
        "uncertainty_score": 0.1
    })

    audit = {"passed": True}

    cand = build_prediction_candidate_from_row(row, audit, profile)

    assert cand.symbol == "BTC"
    assert cand.passed_prediction_filters is True
    assert cand.prediction_label == "prediction_candidate_ready"

    row["confidence_score"] = 0.2
    cand2 = build_prediction_candidate_from_row(row, audit, profile)
    assert cand2.passed_prediction_filters is False
    assert cand2.prediction_label == "prediction_candidate_low_confidence"
