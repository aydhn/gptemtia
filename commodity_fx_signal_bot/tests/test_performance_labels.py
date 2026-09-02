import pytest
from local_performance.performance_labels import list_performance_domain_labels, list_performance_estimate_labels, list_performance_status_labels, list_efficiency_candidate_labels, list_performance_risk_labels, validate_performance_domain_label, validate_performance_estimate_label, validate_performance_status, validate_efficiency_candidate_label, validate_performance_risk, ConfigError

def test_label_lists():
    assert len(list_performance_domain_labels()) > 0
    assert len(list_performance_estimate_labels()) > 0
    assert len(list_performance_status_labels()) > 0
    assert len(list_efficiency_candidate_labels()) > 0
    assert len(list_performance_risk_labels()) > 0

def test_validators():
    validate_performance_domain_label("performance_budget_domain")
    validate_performance_estimate_label("cpu_estimate_low")
    validate_performance_status("performance_ready_for_rehearsal")
    assert "production capacity approval" not in "performance_ready_for_rehearsal"
