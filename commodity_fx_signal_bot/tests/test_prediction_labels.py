import pytest
from commodity_fx_signal_bot.ml.prediction_labels import (
    list_prediction_candidate_labels,
    list_prediction_direction_labels,
    list_prediction_task_labels,
    list_prediction_context_labels,
    validate_prediction_candidate_label,
    validate_prediction_direction_label,
    validate_prediction_task_label,
    validate_prediction_context_label,
    is_blocking_prediction_label
)

def test_prediction_labels_not_empty():
    assert len(list_prediction_candidate_labels()) > 0
    assert len(list_prediction_direction_labels()) > 0
    assert len(list_prediction_task_labels()) > 0
    assert len(list_prediction_context_labels()) > 0

def test_validate_prediction_candidate_label():
    validate_prediction_candidate_label("prediction_candidate_ready")
    with pytest.raises(ValueError):
        validate_prediction_candidate_label("invalid_label")

def test_validate_prediction_direction_label():
    validate_prediction_direction_label("predicted_up")
    with pytest.raises(ValueError):
        validate_prediction_direction_label("buy_now")

def test_is_blocking_prediction_label():
    assert is_blocking_prediction_label("prediction_candidate_rejected") is True
    assert is_blocking_prediction_label("prediction_candidate_ready") is False
