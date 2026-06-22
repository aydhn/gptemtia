import pytest
from local_maintenance.maintenance_config import (
    validate_local_maintenance_profiles,
    get_default_local_maintenance_profile,
    get_local_maintenance_profile,
    ConfigError
)

def test_validate_local_maintenance_profiles():
    # Should not raise exception
    validate_local_maintenance_profiles()

def test_get_default_local_maintenance_profile():
    profile = get_default_local_maintenance_profile()
    assert profile is not None
    assert profile.name == "balanced_local_maintenance"
    assert profile.language is not None
    assert 1 <= profile.default_monthly_review_day <= 28
    assert profile.stale_report_days_warning > 0
    assert 0.0 <= profile.min_sustainability_score <= 1.0
    assert profile.dry_run_default is True
    assert not profile.allow_production_scheduler
    assert not profile.allow_background_daemon
    assert not profile.allow_auto_upgrade
    assert not profile.allow_auto_fix
    assert not profile.allow_file_modification
    assert not profile.allow_file_deletion
    assert not profile.allow_overwrite
    assert not profile.allow_cloud_upload
    assert not profile.allow_external_service
    assert not profile.allow_live_commands
    assert not profile.allow_broker_commands
    assert not profile.allow_deploy_commands
    assert not profile.allow_real_market_download
    assert not profile.allow_external_llm

def test_get_local_maintenance_profile_unknown():
    with pytest.raises(ConfigError):
        get_local_maintenance_profile("unknown_profile_123")
