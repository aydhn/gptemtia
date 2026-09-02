import pytest
from local_incident_response.incident_config import validate_local_incident_response_profiles, get_default_local_incident_response_profile, ConfigError

def test_validate_local_incident_response_profiles():
    validate_local_incident_response_profiles()

def test_get_default_local_incident_response_profile():
    profile = get_default_local_incident_response_profile()
    assert profile.name == "balanced_local_incident_response"
    assert profile.language == "tr"
    assert profile.max_items > 0
    assert profile.max_events > 0
    assert 0 <= profile.min_readiness_score <= 1
    assert profile.dry_run_default is True
    assert not profile.allow_real_incident_response
