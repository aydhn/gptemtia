from advanced_regime_foundation.regime_foundation_labels import (
    list_regime_foundation_domain_labels,
    list_regime_family_labels,
    list_regime_status_labels,
    validate_regime_foundation_domain_label,
    validate_regime_family_label,
    validate_regime_status_label,
)


def test_regime_foundation_labels():
    domain_labels = list_regime_foundation_domain_labels()
    assert len(domain_labels) >= 20
    assert "market_behavior_taxonomy_domain" in domain_labels
    assert "regime_state_taxonomy_domain" in domain_labels
    assert "phase_127_handoff_domain" in domain_labels

    family_labels = list_regime_family_labels()
    assert "regime_family_volatility" in family_labels
    assert "regime_family_trend" in family_labels
    assert "regime_family_range" in family_labels

    status_labels = list_regime_status_labels()
    assert "regime_ready" in status_labels
    assert "regime_placeholder_only" in status_labels

    assert validate_regime_foundation_domain_label("market_behavior_taxonomy_domain") is True
    assert validate_regime_foundation_domain_label("invalid_label") is False

    assert validate_regime_family_label("regime_family_volatility") is True
    assert validate_regime_family_label("invalid_family") is False

    assert validate_regime_status_label("regime_ready") is True
    assert validate_regime_status_label("invalid_status") is False
