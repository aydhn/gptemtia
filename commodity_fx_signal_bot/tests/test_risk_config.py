import pytest
from risk.risk_config import (
    get_default_risk_precheck_profile,
    validate_risk_precheck_profiles,
    normalize_risk_component_weights,
    get_risk_precheck_profile,
    ConfigError,
)


def test_validate_risk_precheck_profiles():
    validate_risk_precheck_profiles()  # Should not raise exception


def test_get_default_risk_precheck_profile():
    prof = get_default_risk_precheck_profile()
    assert prof.name == "balanced_pretrade_risk"
    assert "volatility" in prof.enabled_risk_components


def test_normalize_risk_component_weights():
    weights = {"a": 1, "b": 1}
    norm = normalize_risk_component_weights(weights)
    assert norm["a"] == 0.5
    assert norm["b"] == 0.5


def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_risk_precheck_profile("does_not_exist")
