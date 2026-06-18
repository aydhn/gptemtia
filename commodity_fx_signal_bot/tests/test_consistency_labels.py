import pytest
from local_consistency.consistency_labels import (
    list_consistency_check_type_labels,
    list_consistency_status_labels,
    list_contradiction_severity_labels,
    list_reference_status_labels,
    list_reconciliation_status_labels,
    validate_consistency_check_type,
    validate_consistency_status,
    validate_contradiction_severity,
    validate_reference_status,
    validate_reconciliation_status
)

def test_labels_not_empty():
    assert len(list_consistency_check_type_labels()) > 0
    assert len(list_consistency_status_labels()) > 0
    assert len(list_contradiction_severity_labels()) > 0
    assert len(list_reference_status_labels()) > 0
    assert len(list_reconciliation_status_labels()) > 0

def test_validate_consistency_check_type():
    validate_consistency_check_type("config_env_check")
    with pytest.raises(ValueError):
        validate_consistency_check_type("invalid_check")

def test_validate_consistency_status():
    validate_consistency_status("consistency_passed")
    with pytest.raises(ValueError):
        validate_consistency_status("invalid_status")
