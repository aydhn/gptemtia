import pytest
from factor_research.factor_config import validate_factor_research_profiles, get_default_factor_research_profile

def test_validate_profiles():
    # Should run without raising exceptions
    validate_factor_research_profiles()

def test_get_default():
    profile = get_default_factor_research_profile()
    assert profile is not None
    assert profile.name == "balanced_factor_research"
