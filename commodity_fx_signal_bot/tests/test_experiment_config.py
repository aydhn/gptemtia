from experiments.experiment_config import (
    get_experiment_profile,
    list_experiment_profiles,
    validate_experiment_profiles,
    get_default_experiment_profile,
    ConfigError
)
import pytest

def test_validate_experiment_profiles():
    validate_experiment_profiles()

def test_get_default_experiment_profile():
    profile = get_default_experiment_profile()
    assert profile is not None

def test_invalid_profile():
    with pytest.raises(ConfigError):
        get_experiment_profile("unknown_profile")
