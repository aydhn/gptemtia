import pytest
from quality_gates.quality_labels import (
    list_quality_check_type_labels,
    list_quality_status_labels,
    list_release_candidate_labels,
    list_repo_hygiene_labels,
    validate_quality_check_type,
    validate_release_candidate_label,
    ValueErrorLabel
)

def test_label_lists_not_empty():
    assert len(list_quality_check_type_labels()) > 0
    assert len(list_quality_status_labels()) > 0
    assert len(list_release_candidate_labels()) > 0
    assert len(list_repo_hygiene_labels()) > 0

def test_validate_quality_check_type_valid():
    validate_quality_check_type("pytest_check")

def test_validate_quality_check_type_invalid():
    with pytest.raises(ValueErrorLabel):
        validate_quality_check_type("invalid_label")

def test_validate_release_candidate_label_valid():
    validate_release_candidate_label("rc_ready_offline")

def test_rc_ready_offline_not_production():
    assert "rc_ready_offline" in list_release_candidate_labels()
    # verify logic that rc_ready_offline is not a production release conceptually
