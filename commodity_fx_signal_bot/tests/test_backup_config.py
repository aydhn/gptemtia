import pytest
from backup_recovery.backup_config import (
    BackupRecoveryProfile,
    get_backup_recovery_profile,
    get_default_backup_recovery_profile,
    list_backup_recovery_profiles,
    validate_backup_recovery_profiles,
    ConfigError
)

def test_validate_backup_recovery_profiles():
    validate_backup_recovery_profiles()

def test_get_default_backup_recovery_profile():
    p = get_default_backup_recovery_profile()
    assert p.name == "balanced_local_backup_recovery"

def test_list_backup_recovery_profiles():
    profs = list_backup_recovery_profiles()
    assert len(profs) > 0

def test_get_backup_recovery_profile_unknown():
    with pytest.raises(ConfigError):
        get_backup_recovery_profile("unknown_profile")
