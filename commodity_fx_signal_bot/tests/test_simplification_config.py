import pytest
from local_simplification.simplification_config import (
    validate_local_simplification_profiles,
    get_default_local_simplification_profile,
    get_local_simplification_profile,
    ConfigError
)

def test_validate_local_simplification_profiles_passes():
    validate_local_simplification_profiles()

def test_get_default_local_simplification_profile():
    p = get_default_local_simplification_profile()
    assert p.name == "balanced_local_simplification"
    assert p.language == "tr"
    assert p.max_items > 0
    assert p.max_candidate_items > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert p.allow_auto_refactor is False

def test_get_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_local_simplification_profile("unknown_profile_name")
