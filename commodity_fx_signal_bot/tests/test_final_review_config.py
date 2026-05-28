import pytest
from final_review.final_review_config import (
    validate_final_review_profiles, get_default_final_review_profile, get_final_review_profile, ConfigError
)

def test_validate_final_review_profiles():
    validate_final_review_profiles()

def test_get_default_final_review_profile():
    profile = get_default_final_review_profile()
    assert profile is not None
    assert profile.name == "balanced_final_review"
    assert profile.dry_run is True

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_final_review_profile("unknown_profile")
