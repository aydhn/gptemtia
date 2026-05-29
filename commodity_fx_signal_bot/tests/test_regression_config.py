import pytest
from scenario_regression.regression_config import (
    ScenarioRegressionProfile,
    get_scenario_regression_profile,
    list_scenario_regression_profiles,
    validate_scenario_regression_profiles,
    get_default_scenario_regression_profile,
    ConfigError
)

def test_validate_scenario_regression_profiles():
    validate_scenario_regression_profiles() # Should not raise

def test_get_default_scenario_regression_profile():
    p = get_default_scenario_regression_profile()
    assert isinstance(p, ScenarioRegressionProfile)
    assert p.use_synthetic_only is True
    assert p.allow_real_market_download is False

def test_invalid_profile():
    with pytest.raises(ConfigError):
        get_scenario_regression_profile("non_existent_profile")
