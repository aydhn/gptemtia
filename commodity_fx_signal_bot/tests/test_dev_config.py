import pytest
from devtools.dev_config import (
    DevExperienceProfile, get_dev_experience_profile,
    list_dev_experience_profiles, validate_dev_experience_profiles,
    get_default_dev_experience_profile
)

def test_validate_dev_experience_profiles():
    validate_dev_experience_profiles()

def test_get_default_dev_experience_profile():
    profile = get_default_dev_experience_profile()
    assert profile.name == "balanced_dev_experience"

def test_required_docs_not_empty():
    profile = get_default_dev_experience_profile()
    assert len(profile.required_docs) > 0

def test_max_cli_help_failures_not_negative():
    profile = get_default_dev_experience_profile()
    assert profile.max_cli_help_failures >= 0

def test_unknown_profile_raises():
    with pytest.raises(ValueError):
        get_dev_experience_profile("unknown_profile")
