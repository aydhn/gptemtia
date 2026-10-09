import pytest

from advanced_data_providers.provider_labels import (
    validate_provider_asset_coverage_label,
    validate_provider_data_type_label,
    validate_provider_domain_label,
    validate_provider_risk_label,
    validate_provider_status,
    validate_provider_type_label,
)


def test_placeholder():
    assert True


def test_validate_provider_domain_label():
    assert validate_provider_domain_label("provider_profile_domain") is True
    with pytest.raises(ValueError):
        validate_provider_domain_label("invalid_label")


def test_validate_provider_type_label():
    assert validate_provider_type_label("provider_dry_run_fixture") is True
    with pytest.raises(ValueError):
        validate_provider_type_label("invalid_label")


def test_validate_provider_asset_coverage_label():
    assert validate_provider_asset_coverage_label("coverage_fx") is True
    with pytest.raises(ValueError):
        validate_provider_asset_coverage_label("invalid_label")


def test_validate_provider_data_type_label():
    assert validate_provider_data_type_label("data_ohlcv") is True
    with pytest.raises(ValueError):
        validate_provider_data_type_label("invalid_label")


def test_validate_provider_status():
    assert validate_provider_status("provider_ready") is True
    with pytest.raises(ValueError):
        validate_provider_status("invalid_label")


def test_validate_provider_risk_label():
    assert validate_provider_risk_label("provider_critical_risk") is True
    with pytest.raises(ValueError):
        validate_provider_risk_label("invalid_label")
