import pytest
from local_maintenance.maintenance_labels import (
    list_maintenance_domain_labels,
    list_maintenance_task_status_labels,
    list_refresh_cadence_labels,
    list_dependency_status_labels,
    list_sustainability_risk_labels,
    validate_maintenance_domain_label,
    validate_refresh_cadence_label
)

def test_label_lists_not_empty():
    assert len(list_maintenance_domain_labels()) > 0
    assert len(list_maintenance_task_status_labels()) > 0
    assert len(list_refresh_cadence_labels()) > 0
    assert len(list_dependency_status_labels()) > 0
    assert len(list_sustainability_risk_labels()) > 0

def test_validate_labels():
    validate_maintenance_domain_label("documentation_maintenance")
    validate_refresh_cadence_label("refresh_monthly_manual")

    with pytest.raises(ValueError):
        validate_maintenance_domain_label("invalid_label")

def test_refresh_monthly_manual_not_scheduler():
    labels = list_refresh_cadence_labels()
    # verify naming implies manual
    assert "refresh_monthly_manual" in labels
