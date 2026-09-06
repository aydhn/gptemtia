"""Tests for Phase 133 Regime Validation Acceptance Labels."""

from advanced_regime_validation_acceptance.regime_validation_acceptance_labels import (
    list_regime_validation_acceptance_domain_labels,
    list_regime_validation_acceptance_status_labels,
    list_regime_validation_acceptance_severity_labels,
    validate_regime_validation_acceptance_domain_label,
    validate_regime_validation_acceptance_status_label,
    validate_regime_validation_acceptance_severity_label,
)


def test_labels_lists_and_validation():
    domains = list_regime_validation_acceptance_domain_labels()
    assert len(domains) >= 28
    assert "no_lookahead_acceptance_domain" in domains
    assert "validation_gate_domain" in domains
    assert "phase_134_handoff_domain" in domains

    assert validate_regime_validation_acceptance_domain_label("no_lookahead_acceptance_domain") is True
    assert validate_regime_validation_acceptance_domain_label("invalid_random_domain") is False

    statuses = list_regime_validation_acceptance_status_labels()
    assert "acceptance_pass" in statuses
    assert "acceptance_fail" in statuses
    assert validate_regime_validation_acceptance_status_label("acceptance_pass") is True
    assert validate_regime_validation_acceptance_status_label("unknown_status") is False

    severities = list_regime_validation_acceptance_severity_labels()
    assert "acceptance_critical" in severities
    assert "acceptance_info" in severities
    assert validate_regime_validation_acceptance_severity_label("acceptance_critical") is True
    assert validate_regime_validation_acceptance_severity_label("extreme_danger") is False
