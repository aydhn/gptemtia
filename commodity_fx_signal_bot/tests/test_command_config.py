import pytest
from command_center.command_config import (
    CommandCenterProfile,
    get_command_center_profile,
    validate_command_center_profiles,
    get_default_command_center_profile
)
from core.exceptions import ConfigError

def test_validate_command_center_profiles():
    # Should not raise any exceptions
    validate_command_center_profiles()

def test_get_default_command_center_profile():
    profile = get_default_command_center_profile()
    assert profile.name == "balanced_offline_command_center"
    assert profile.dry_run_default is True
    assert profile.allow_live_commands is False

def test_profile_constraints():
    profile = get_default_command_center_profile()
    assert profile.max_suggested_commands > 0
    assert 0.0 <= profile.min_quality_score <= 1.0
    assert profile.allow_broker_commands is False
    assert profile.allow_deploy_commands is False
    assert profile.allow_background_daemons is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_command_center_profile("unknown_profile")
