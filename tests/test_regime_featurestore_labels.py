"""Tests for Phase 134 Regime FeatureStore Labels."""

from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    list_regime_featurestore_domain_labels,
    list_regime_featurestore_status_labels,
    list_regime_featurestore_entity_labels,
    validate_regime_featurestore_domain_label,
    validate_regime_featurestore_status_label,
    validate_regime_featurestore_entity_label,
    REGIME_FEATURESTORE_PROFILE_DOMAIN,
    REGIME_STORE_READY,
    STORE_ENTITY_REGIME_TAXONOMY,
)


def test_domain_labels():
    domains = list_regime_featurestore_domain_labels()
    assert len(domains) >= 30
    assert REGIME_FEATURESTORE_PROFILE_DOMAIN in domains
    assert validate_regime_featurestore_domain_label(REGIME_FEATURESTORE_PROFILE_DOMAIN) is True
    assert validate_regime_featurestore_domain_label("invalid_domain") is False


def test_status_labels():
    statuses = list_regime_featurestore_status_labels()
    assert len(statuses) >= 5
    assert REGIME_STORE_READY in statuses
    assert validate_regime_featurestore_status_label(REGIME_STORE_READY) is True
    assert validate_regime_featurestore_status_label("invalid_status") is False


def test_entity_labels():
    entities = list_regime_featurestore_entity_labels()
    assert len(entities) >= 8
    assert STORE_ENTITY_REGIME_TAXONOMY in entities
    assert validate_regime_featurestore_entity_label(STORE_ENTITY_REGIME_TAXONOMY) is True
    assert validate_regime_featurestore_entity_label("invalid_entity") is False
