import pytest
from advanced_factor_metadata.factor_metadata_labels import (
    FACTOR_FAMILY_TREND,
    FACTOR_FAMILY_MOMENTUM,
    FACTOR_FAMILY_VOLATILITY,
    FACTOR_FAMILY_MEAN_REVERSION,
    FACTOR_READY,
    list_factor_family_labels,
    list_factor_metadata_domain_labels,
    list_factor_status_labels,
    validate_factor_family_label,
    validate_factor_metadata_domain_label,
    validate_factor_status_label,
)


def test_factor_metadata_domain_labels():
    labels = list_factor_metadata_domain_labels()
    assert len(labels) >= 32
    assert "factor_metadata_domain" in labels
    assert "factor_family_domain" in labels
    assert "factor_contract_domain" in labels
    assert validate_factor_metadata_domain_label("factor_contract_domain") is True
    assert validate_factor_metadata_domain_label("non_existent_label") is False


def test_factor_family_labels():
    families = list_factor_family_labels()
    assert len(families) >= 12
    assert FACTOR_FAMILY_TREND in families
    assert FACTOR_FAMILY_MOMENTUM in families
    assert FACTOR_FAMILY_VOLATILITY in families
    assert FACTOR_FAMILY_MEAN_REVERSION in families
    assert validate_factor_family_label(FACTOR_FAMILY_TREND) is True
    assert validate_factor_family_label("invalid_family") is False


def test_factor_status_labels():
    statuses = list_factor_status_labels()
    assert len(statuses) >= 6
    assert FACTOR_READY in statuses
    assert validate_factor_status_label(FACTOR_READY) is True
    assert validate_factor_status_label("random_status") is False
