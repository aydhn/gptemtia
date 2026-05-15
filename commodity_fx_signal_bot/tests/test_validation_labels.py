import pytest
from validation.validation_labels import (
    list_validation_status_labels,
    validate_validation_status,
    validate_split_label,
    validate_optimizer_candidate_label,
    is_blocking_validation_status,
)

def test_list_validation_status_labels():
    labels = list_validation_status_labels()
    assert len(labels) > 0
    assert "validation_passed" in labels

def test_validate_validation_status():
    validate_validation_status("validation_passed")
    with pytest.raises(ValueError):
        validate_validation_status("invalid_status_xyz")

def test_validate_split_label():
    validate_split_label("train")
    with pytest.raises(ValueError):
        validate_split_label("invalid_split_xyz")

def test_validate_optimizer_candidate_label():
    validate_optimizer_candidate_label("optimizer_candidate_passed")
    with pytest.raises(ValueError):
        validate_optimizer_candidate_label("invalid_candidate_xyz")

def test_blocking_status():
    assert is_blocking_validation_status("validation_failed") is True
    assert is_blocking_validation_status("validation_passed") is False
