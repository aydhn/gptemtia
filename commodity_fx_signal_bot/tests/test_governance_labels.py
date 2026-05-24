import pytest

from governance.governance_labels import (
    list_artifact_type_labels,
    list_audit_event_labels,
    list_governance_status_labels,
    list_lineage_relation_labels,
    validate_artifact_type,
    validate_governance_status,
)


def test_label_lists_not_empty():
    assert len(list_artifact_type_labels()) > 0
    assert len(list_lineage_relation_labels()) > 0
    assert len(list_governance_status_labels()) > 0
    assert len(list_audit_event_labels()) > 0

def test_valid_artifact_type():
    validate_artifact_type("feature_artifact")

def test_invalid_artifact_type():
    with pytest.raises(ValueError):
        validate_artifact_type("unknown_fake")

def test_governance_passed_not_compliance():
    # governance_passed is allowed
    validate_governance_status("governance_passed")
    # it is not named production_compliance_passed
    assert "production_compliance" not in list_governance_status_labels()
