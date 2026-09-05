"""Tests for Phase 131 Cross-Asset Regime Labels."""

from advanced_cross_asset_regime_context.cross_asset_regime_labels import (
    CROSS_ASSET_REGIME_DOMAIN_LABELS,
    CROSS_ASSET_REGIME_STATUS_LABELS,
    CROSS_ASSET_RELATIONSHIP_LABELS,
    list_cross_asset_regime_domain_labels,
    list_cross_asset_regime_status_labels,
    list_cross_asset_relationship_labels,
    validate_cross_asset_regime_domain_label,
    validate_cross_asset_regime_status_label,
    validate_cross_asset_relationship_label,
)


def test_cross_asset_regime_labels_exist():
    assert len(CROSS_ASSET_REGIME_DOMAIN_LABELS) >= 30
    assert len(CROSS_ASSET_REGIME_STATUS_LABELS) >= 5
    assert len(CROSS_ASSET_RELATIONSHIP_LABELS) >= 10


def test_list_functions():
    assert len(list_cross_asset_regime_domain_labels()) == len(CROSS_ASSET_REGIME_DOMAIN_LABELS)
    assert len(list_cross_asset_regime_status_labels()) == len(CROSS_ASSET_REGIME_STATUS_LABELS)
    assert len(list_cross_asset_relationship_labels()) == len(CROSS_ASSET_RELATIONSHIP_LABELS)


def test_validation_functions():
    assert validate_cross_asset_regime_domain_label("cross_asset_regime_domain") is True
    assert validate_cross_asset_regime_domain_label("invalid_domain") is False

    assert validate_cross_asset_regime_status_label("cross_asset_context_ready") is True
    assert validate_cross_asset_regime_status_label("invalid_status") is False

    assert validate_cross_asset_relationship_label("relationship_comovement_context") is True
    assert validate_cross_asset_relationship_label("invalid_rel") is False
