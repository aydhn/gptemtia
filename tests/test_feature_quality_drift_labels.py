import pytest
from advanced_feature_quality_drift.feature_quality_drift_labels import (
    list_quality_drift_domain_labels,
    list_quality_drift_severity_labels,
    list_quality_drift_status_labels,
    validate_quality_drift_domain_label,
    validate_quality_drift_severity_label,
    validate_quality_drift_status_label,
)


def test_feature_quality_drift_labels():
    domains = list_quality_drift_domain_labels()
    assert "missingness_domain" in domains
    assert "distribution_drift_domain" in domains
    assert "rolling_stability_domain" in domains
    assert "factor_quality_domain" in domains
    assert "phase_124_handoff_domain" in domains

    severities = list_quality_drift_severity_labels()
    assert "quality_critical" in severities
    assert "drift_critical" in severities
    assert "quality_info" in severities

    statuses = list_quality_drift_status_labels()
    assert "diagnostic_pass" in statuses
    assert "diagnostic_fail" in statuses
    assert "diagnostic_manual_review_required" in statuses

    assert validate_quality_drift_domain_label("missingness_domain") is True
    assert validate_quality_drift_severity_label("quality_critical") is True
    assert validate_quality_drift_status_label("diagnostic_pass") is True

    with pytest.raises(ValueError):
        validate_quality_drift_domain_label("unregistered_domain")
    with pytest.raises(ValueError):
        validate_quality_drift_severity_label("unregistered_severity")
    with pytest.raises(ValueError):
        validate_quality_drift_status_label("unregistered_status")
