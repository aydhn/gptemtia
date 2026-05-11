import pytest
import pandas as pd
from ml.prediction_context import (
    build_model_context_features,
    build_ensemble_context_features
)

def test_build_model_context_features():
    df = pd.DataFrame({
        "timestamp": ["2020", "2021"],
        "predicted_direction": ["predicted_up", "predicted_down"],
        "prediction_score": [0.8, 0.2],
        "calibrated_score": [0.8, 0.2],
        "confidence_score": [0.8, 0.8],
        "uncertainty_score": [0.1, 0.1],
        "model_quality_score": [0.9, 0.9],
        "dataset_quality_score": [0.9, 0.9],
        "leakage_risk_score": [0.0, 0.0],
        "prediction_context_label": ["ml_context_supportive", "ml_context_supportive"]
    })

    ctx, status = build_model_context_features(df)

    assert "ml_predicted_direction_code" in ctx.columns
    assert ctx.loc["2020", "ml_predicted_direction_code"] == 1
    assert ctx.loc["2021", "ml_predicted_direction_code"] == -1
    assert ctx["ml_context_supportive"].sum() == 2

def test_build_ensemble_context_features():
    df = pd.DataFrame(index=["2020"], data={
        "ensemble_predicted_direction": ["predicted_up"],
        "ensemble_prediction_score": [0.8],
        "ensemble_confidence_score": [0.8],
        "ensemble_uncertainty_score": [0.1],
        "ensemble_disagreement_score": [0.0],
        "ensemble_context_label": ["ml_context_supportive"]
    })

    ctx, status = build_ensemble_context_features(df)

    assert "ml_ensemble_direction_code" in ctx.columns
    assert ctx.loc["2020", "ml_ensemble_direction_code"] == 1
