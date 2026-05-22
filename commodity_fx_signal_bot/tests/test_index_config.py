import pytest
from synthetic_indices.index_config import (
    validate_synthetic_index_profiles,
    get_default_synthetic_index_profile,
    get_synthetic_index_profile,
    ConfigError
)

def test_validate_synthetic_index_profiles():
    # Should not raise any exceptions for the default profiles
    validate_synthetic_index_profiles()

def test_get_default_synthetic_index_profile():
    profile = get_default_synthetic_index_profile()
    assert profile.name == "balanced_synthetic_index_research"
    assert profile.base_value > 0
    assert 0 < profile.max_single_weight <= 1

def test_get_synthetic_index_profile():
    profile = get_synthetic_index_profile("short_term_rotation_research")
    assert profile.name == "short_term_rotation_research"

    with pytest.raises(ConfigError):
        get_synthetic_index_profile("non_existent_profile")
