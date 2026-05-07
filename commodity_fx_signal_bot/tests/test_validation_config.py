import pytest
from validation.validation_config import (
    validate_validation_profiles,
    get_default_validation_profile,
    get_validation_profile,
    ConfigError,
    ValidationProfile,
)

def test_validate_validation_profiles_no_error():
    validate_validation_profiles()

def test_get_default_validation_profile():
    profile = get_default_validation_profile()
    assert profile.name == "balanced_walk_forward_validation"
    assert profile.train_window_bars > 0

def test_window_values_positive():
    with pytest.raises(ValueError):
        ValidationProfile(
            name="invalid",
            description="test",
            train_window_bars=-1,
            test_window_bars=10,
            step_bars=5,
            min_train_bars=1,
            min_test_bars=1,
        )

def test_unknown_profile_raises_error():
    with pytest.raises(ConfigError):
        get_validation_profile("non_existent_profile_123")
