import pytest
from local_timeline.timeline_config import (
    LocalTimelineProfile, get_local_timeline_profile, list_local_timeline_profiles,
    validate_local_timeline_profiles, get_default_local_timeline_profile, ConfigError
)

def test_validate_local_timeline_profiles():
    # Should not raise exception
    validate_local_timeline_profiles()

def test_get_default_local_timeline_profile():
    profile = get_default_local_timeline_profile()
    assert isinstance(profile, LocalTimelineProfile)
    assert profile.name == "balanced_local_timeline"

def test_language_empty_raises():
    with pytest.raises(ValueError):
        LocalTimelineProfile(name="test", description="desc", language="")

def test_max_events_files_positive():
    with pytest.raises(ValueError):
        LocalTimelineProfile(name="test", description="desc", max_events=0)
    with pytest.raises(ValueError):
        LocalTimelineProfile(name="test", description="desc", max_files=-1)

def test_stale_days_warning_less_than_freshness_raises():
    with pytest.raises(ValueError):
        LocalTimelineProfile(name="test", description="desc", freshness_days_warning=45, stale_days_warning=30)

def test_dry_run_default():
    profiles = list_local_timeline_profiles()
    for p in profiles:
        assert p.dry_run_default is True
        assert p.allow_external_event_service is False
        assert p.allow_cloud_upload is False
        assert p.allow_file_modification is False
        assert p.allow_file_deletion is False
        assert p.allow_live_commands is False
        assert p.allow_broker_commands is False
        assert p.allow_deploy_commands is False
        assert p.allow_background_daemons is False
        assert p.allow_real_market_download is False
        assert p.allow_external_llm is False

def test_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_local_timeline_profile("non_existent_profile")
