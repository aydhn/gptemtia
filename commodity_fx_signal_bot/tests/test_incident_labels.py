from local_incident_response.incident_labels import (
    list_incident_domain_labels, list_safety_event_category_labels,
    list_severity_labels, list_incident_status_labels, list_incident_risk_labels,
    validate_incident_domain_label, validate_safety_event_category
)
import pytest

def test_label_lists():
    assert len(list_incident_domain_labels()) > 0
    assert len(list_safety_event_category_labels()) > 0
    assert len(list_severity_labels()) > 0
    assert len(list_incident_status_labels()) > 0
    assert len(list_incident_risk_labels()) > 0

def test_validate_labels():
    validate_incident_domain_label("incident_rehearsal_domain")
    validate_safety_event_category("event_boundary_breach")
    with pytest.raises(ValueError):
        validate_incident_domain_label("invalid_label")
