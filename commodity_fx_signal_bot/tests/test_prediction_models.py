import pytest
from ml.prediction_models import (
    ModelPredictionOutput,
    PredictionAudit,
    model_prediction_output_to_dict,
    prediction_audit_to_dict,
    normalize_prediction_score,
    infer_predicted_direction_from_class,
    infer_prediction_context_label
)

def test_normalize_prediction_score():
    assert normalize_prediction_score(0.8, "classification_prediction") == 0.8
    assert normalize_prediction_score(1.5, "classification_prediction") == 1.0
    assert normalize_prediction_score(-0.5, "classification_prediction") == 0.0

def test_infer_predicted_direction_from_class():
    assert infer_predicted_direction_from_class("up") == "predicted_up"
    assert infer_predicted_direction_from_class("-1") == "predicted_down"
    assert infer_predicted_direction_from_class("flat") == "predicted_flat"
    assert infer_predicted_direction_from_class("random") == "predicted_unknown"
    assert infer_predicted_direction_from_class(None) == "predicted_unknown"

def test_infer_prediction_context_label():
    assert infer_prediction_context_label("predicted_up", 0.9, 0.1) == "ml_context_supportive"
    assert infer_prediction_context_label("predicted_down", 0.7, 0.8) == "ml_context_uncertain"
    assert infer_prediction_context_label("predicted_unknown", 0.9, 0.1) == "ml_context_unavailable"
