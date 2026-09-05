"""Tests for Regime Transition Labels and Categorizations."""

from advanced_regime_transition.regime_transition_labels import (
    REGIME_TRANSITION_DOMAIN_LABELS,
    REGIME_TRANSITION_STATUS_LABELS,
    REGIME_TRANSITION_SEVERITY_LABELS,
    list_regime_transition_domain_labels,
    list_regime_transition_status_labels,
    list_regime_transition_severity_labels,
    validate_regime_transition_domain_label,
    validate_regime_transition_status_label,
    validate_regime_transition_severity_label,
)
from advanced_regime_transition.regime_transition_validation import (
    FORBIDDEN_TRANSITION_TERMS,
)


def test_regime_transition_labels():
    domains = list_regime_transition_domain_labels()
    assert len(domains) >= 30
    assert "regime_transition_profile_domain" in domains
    assert "state_sequence_contract_domain" in domains
    assert "transition_metric_domain" in domains

    statuses = list_regime_transition_status_labels()
    assert "transition_ready" in statuses
    assert "transition_blocked_by_safety" in statuses

    severities = list_regime_transition_severity_labels()
    assert "transition_critical" in severities
    assert "transition_high" in severities


def test_label_validators():
    assert validate_regime_transition_domain_label("regime_transition_profile_domain") is True
    assert validate_regime_transition_status_label("transition_ready") is True
    assert validate_regime_transition_severity_label("transition_high") is True


def test_forbidden_transition_terms():
    assert "buy signal" in FORBIDDEN_TRANSITION_TERMS
    assert "sell signal" in FORBIDDEN_TRANSITION_TERMS
    assert "long position" in FORBIDDEN_TRANSITION_TERMS
    assert "short position" in FORBIDDEN_TRANSITION_TERMS
    assert "broker ready" in FORBIDDEN_TRANSITION_TERMS
    assert "production ready" in FORBIDDEN_TRANSITION_TERMS


