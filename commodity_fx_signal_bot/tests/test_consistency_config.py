import pytest
from local_consistency.consistency_config import (
    ConfigError,
    get_local_consistency_profile,
    list_local_consistency_profiles,
    validate_local_consistency_profiles,
    get_default_local_consistency_profile
)

def test_validate_local_consistency_profiles():
    validate_local_consistency_profiles()

def test_get_default_local_consistency_profile():
    profile = get_default_local_consistency_profile()
    assert profile.name == "balanced_local_consistency"

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_consistency_profile("unknown")
