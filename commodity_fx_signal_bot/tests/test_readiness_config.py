import pytest
from local_readiness.readiness_config import (
    validate_local_readiness_profiles,
    get_default_local_readiness_profile,
    get_local_readiness_profile,
    ConfigError
)

def test_validate_local_readiness_profiles():
    validate_local_readiness_profiles()

def test_get_default_local_readiness_profile():
    p = get_default_local_readiness_profile()
    assert p.language == "tr"
    assert p.max_checks > 0
    assert 0.0 <= p.min_readiness_score <= 1.0
    assert p.dry_run_default is True
    assert p.allow_production_release_claim is False
    assert p.allow_live_commands is False

def test_get_local_readiness_profile_unknown():
    with pytest.raises(ConfigError):
        get_local_readiness_profile("unknown_profile")
