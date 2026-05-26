import pytest
from maintenance.maintenance_config import get_maintenance_profile, list_maintenance_profiles, validate_maintenance_profiles, get_default_maintenance_profile, ConfigError

def test_validate_maintenance_profiles():
    validate_maintenance_profiles()

def test_get_default_maintenance_profile():
    profile = get_default_maintenance_profile()
    assert profile.name == "balanced_local_maintenance"
    assert profile.dry_run_default is True
    assert profile.allow_delete is False
    assert profile.allow_archive_move is False

def test_profile_constraints():
    profiles = list_maintenance_profiles()
    for profile in profiles:
        assert profile.max_inventory_files > 0
        assert profile.large_file_threshold_mb > 0
        assert profile.dry_run_default is True
        assert profile.allow_delete is False
        assert profile.allow_archive_move is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_maintenance_profile("unknown_profile_123")
