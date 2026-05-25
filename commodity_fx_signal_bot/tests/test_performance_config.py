import pytest
from performance.performance_config import (
    validate_performance_profiles,
    get_default_performance_profile,
    get_performance_profile,
    list_performance_profiles,
    ConfigError
)

def test_validate_performance_profiles():
    # Should not raise any exception
    validate_performance_profiles()

def test_get_default_performance_profile():
    profile = get_default_performance_profile()
    assert profile.name == "balanced_local_performance"

def test_performance_profile_constraints():
    profile = get_default_performance_profile()
    assert profile.max_runtime_seconds_per_script > 0
    assert profile.max_memory_mb_per_script > 0
    assert profile.max_parallel_workers >= 1

    # Check default parallel workers is 1 for initial profiles
    for p in list_performance_profiles():
        assert p.max_parallel_workers == 1

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_performance_profile("non_existent_profile")
