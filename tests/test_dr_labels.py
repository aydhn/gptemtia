from local_dr.dr_labels import (
    list_dr_domain_labels, list_dr_scenario_status_labels, list_restore_drill_status_labels,
    list_failure_severity_labels, list_resilience_risk_labels,
    validate_dr_domain_label, validate_dr_scenario_status, validate_restore_drill_status,
    validate_failure_severity, validate_resilience_risk
)
import pytest

def test_dr_labels():
    assert "archive_restore_dr" in list_dr_domain_labels()
    assert "defined" in list_dr_scenario_status_labels()
    assert "passed" in list_restore_drill_status_labels()
    assert "high" in list_failure_severity_labels()
    assert "critical" in list_resilience_risk_labels()

    validate_dr_domain_label("archive_restore_dr")
    with pytest.raises(ValueError):
        validate_dr_domain_label("invalid")

    validate_dr_scenario_status("defined")
    with pytest.raises(ValueError):
        validate_dr_scenario_status("invalid")

    validate_restore_drill_status("passed")
    with pytest.raises(ValueError):
        validate_restore_drill_status("invalid")

    validate_failure_severity("high")
    with pytest.raises(ValueError):
        validate_failure_severity("invalid")

    validate_resilience_risk("critical")
    with pytest.raises(ValueError):
        validate_resilience_risk("invalid")
