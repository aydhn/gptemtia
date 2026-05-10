from ml_integration.integration_labels import (
    list_ml_context_labels,
    list_model_alignment_labels,
    list_ml_integration_status_labels,
    validate_ml_context_label,
    validate_model_alignment_label,
    validate_ml_integration_status_label,
    is_conflicting_alignment,
    is_supportive_alignment,
    is_blocking_ml_context_label,
    ML_CONTEXT_SUPPORTIVE,
    MODEL_ALIGNED_WITH_CANDIDATE,
    MODEL_CONFLICTS_WITH_CANDIDATE,
    ML_CONTEXT_LEAKAGE_RISK
)
import pytest

def test_label_lists_not_empty():
    assert len(list_ml_context_labels()) > 0
    assert len(list_model_alignment_labels()) > 0
    assert len(list_ml_integration_status_labels()) > 0

def test_validate_labels():
    validate_ml_context_label(ML_CONTEXT_SUPPORTIVE)
    with pytest.raises(ValueError):
        validate_ml_context_label("invalid_label")

    validate_model_alignment_label(MODEL_ALIGNED_WITH_CANDIDATE)
    with pytest.raises(ValueError):
        validate_model_alignment_label("invalid_label")

def test_alignment_helpers():
    assert is_supportive_alignment(MODEL_ALIGNED_WITH_CANDIDATE)
    assert not is_supportive_alignment(MODEL_CONFLICTS_WITH_CANDIDATE)

    assert is_conflicting_alignment(MODEL_CONFLICTS_WITH_CANDIDATE)
    assert not is_conflicting_alignment(MODEL_ALIGNED_WITH_CANDIDATE)

    assert is_blocking_ml_context_label(ML_CONTEXT_LEAKAGE_RISK)
