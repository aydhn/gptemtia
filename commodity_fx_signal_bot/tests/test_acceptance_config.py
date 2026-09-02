import pytest
from local_acceptance.acceptance_config import (
    validate_local_acceptance_profiles,
    get_default_local_acceptance_profile,
    get_local_acceptance_profile,
    ConfigError
)

def test_validate_local_acceptance_profiles():
    validate_local_acceptance_profiles()

def test_get_default_local_acceptance_profile():
    p = get_default_local_acceptance_profile()
    assert p.name == "balanced_local_acceptance"
    assert p.dry_run_default is True

def test_get_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_acceptance_profile("unknown_profile")
