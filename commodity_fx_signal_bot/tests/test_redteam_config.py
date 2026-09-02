import pytest
from local_redteam.redteam_config import (
    validate_local_redteam_profiles,
    get_default_local_redteam_profile,
    get_local_redteam_profile,
    ConfigError
)

def test_validate_local_redteam_profiles():
    validate_local_redteam_profiles() # Should not raise

def test_get_default_local_redteam_profile():
    p = get_default_local_redteam_profile()
    assert p.language == "tr"
    assert p.max_items > 0
    assert p.max_scenarios > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert p.allow_real_attack is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_redteam_profile("unknown_profile")
