import pytest

from observability.observability_config import (
    ObservabilityProfile,
    get_observability_profile,
    list_observability_profiles,
    validate_observability_profiles,
    get_default_observability_profile,
    ConfigError
)

def test_validate_observability_profiles_passes():
    # Built-in profiles should validate without error
    validate_observability_profiles()

def test_get_default_observability_profile():
    profile = get_default_observability_profile()
    assert isinstance(profile, ObservabilityProfile)
    assert profile.name == "balanced_system_observability"

def test_invalid_log_level():
    with pytest.raises(ValueError, match="Invalid log level"):
        ObservabilityProfile(name="test", description="test", log_level="INVALID")

def test_negative_stale_hours():
    with pytest.raises(ValueError, match="cannot be negative"):
        ObservabilityProfile(name="test", description="test", max_stale_hours_daily=-1.0)

def test_negative_max_log_files():
    with pytest.raises(ValueError, match="must be positive"):
        ObservabilityProfile(name="test", description="test", max_log_files=0)

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_observability_profile("unknown_profile_xyz")

def test_list_profiles():
    profiles = list_observability_profiles()
    assert len(profiles) > 0
    assert all(isinstance(p, ObservabilityProfile) for p in profiles)
