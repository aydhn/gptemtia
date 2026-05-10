import pytest
import pandas as pd
from ml.prediction_quality import (
    check_prediction_score_ranges,
    check_for_forbidden_live_terms_in_predictions,
    build_prediction_quality_report
)
from ml.prediction_config import MLPredictionProfile

def test_check_prediction_score_ranges():
    df = pd.DataFrame({"confidence_score": [0.5, 1.2, -0.1]})
    res = check_prediction_score_ranges(df)
    assert res["passed"] is False
    assert res["invalid_score_count"] == 2

    df2 = pd.DataFrame({"confidence_score": [0.5, 0.9]})
    assert check_prediction_score_ranges(df2)["passed"] is True

def test_forbidden_live_terms():
    df = pd.DataFrame({"notes": ["this is a LIVE_SIGNAL", "ok"]})
    res = check_for_forbidden_live_terms_in_predictions(df)
    assert res["passed"] is False
    assert "LIVE_SIGNAL" in res["forbidden_live_terms_found"]

def test_build_prediction_quality_report():
    df = pd.DataFrame({
        "prediction_id": ["p1", "p2"],
        "confidence_score": [0.8, 0.9],
        "uncertainty_score": [0.1, 0.2]
    })
    audit = {"schema_compatible": True, "model_quality_score": 0.9}
    profile = MLPredictionProfile(
        name="test", description="", dataset_profile="", training_profile="",
        allowed_model_families=("test",), min_model_quality_score=0.5
    )

    rep = build_prediction_quality_report(df, audit, profile)
    assert rep["passed"] is True
    assert rep["invalid_score_count"] == 0
