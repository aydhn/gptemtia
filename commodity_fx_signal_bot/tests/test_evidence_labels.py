import pytest
from evidence_governance.evidence_labels import (
    list_evidence_artifact_labels,
    list_control_domain_labels,
    list_control_status_labels,
    list_evidence_freshness_labels,
    list_evidence_export_labels,
    validate_evidence_artifact_label,
    validate_control_domain,
    validate_control_status,
    validate_evidence_freshness,
    validate_evidence_export_label
)

def test_label_lists_not_empty():
    assert len(list_evidence_artifact_labels()) > 0
    assert len(list_control_domain_labels()) > 0
    assert len(list_control_status_labels()) > 0
    assert len(list_evidence_freshness_labels()) > 0
    assert len(list_evidence_export_labels()) > 0

def test_validate_evidence_artifact_label():
    validate_evidence_artifact_label("report_evidence")
    with pytest.raises(ValueError):
        validate_evidence_artifact_label("invalid_label")

def test_validate_control_domain():
    validate_control_domain("safety_controls")
    with pytest.raises(ValueError):
        validate_control_domain("invalid_domain")

def test_control_status_not_official():
    validate_control_status("control_evidenced")
    # control_evidenced is just a label, not an official compliance claim
