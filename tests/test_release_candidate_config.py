import pytest
from local_release_candidate.release_candidate_config import validate_local_release_candidate_profiles, get_default_local_release_candidate_profile, ConfigError

def test_validate_local_release_candidate_profiles():
    validate_local_release_candidate_profiles()

def test_get_default_local_release_candidate_profile():
    p = get_default_local_release_candidate_profile()
    assert p is not None
    assert p.name == "balanced_local_release_candidate"

def test_language_not_empty():
    p = get_default_local_release_candidate_profile()
    assert len(p.language) > 0
