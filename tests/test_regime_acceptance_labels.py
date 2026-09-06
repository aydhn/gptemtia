"""Test suite for Phase 135 Regime Acceptance Labels."""

from advanced_regime_acceptance.regime_acceptance_labels import (
    list_regime_acceptance_domain_labels,
    list_regime_acceptance_status_labels,
    validate_regime_acceptance_domain_label,
    validate_regime_acceptance_status_label,
    REGIME_ACCEPTANCE_DOMAIN,
    REGIME_BLOCK_INVENTORY_DOMAIN,
    ACCEPTANCE_PASS,
    ACCEPTANCE_FAIL,
)


def test_domain_labels():
    domains = list_regime_acceptance_domain_labels()
    assert len(domains) >= 20
    assert REGIME_ACCEPTANCE_DOMAIN in domains
    assert REGIME_BLOCK_INVENTORY_DOMAIN in domains
    assert validate_regime_acceptance_domain_label(REGIME_ACCEPTANCE_DOMAIN) is True
    assert validate_regime_acceptance_domain_label("invalid_label") is False


def test_status_labels():
    statuses = list_regime_acceptance_status_labels()
    assert len(statuses) >= 7
    assert ACCEPTANCE_PASS in statuses
    assert ACCEPTANCE_FAIL in statuses
    assert validate_regime_acceptance_status_label(ACCEPTANCE_PASS) is True
    assert validate_regime_acceptance_status_label("non_status") is False
