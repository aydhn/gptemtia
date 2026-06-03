from backup_recovery.disaster_recovery import build_disaster_recovery_manifest
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_build_disaster_recovery_manifest():
    prof = get_default_backup_recovery_profile()
    res = build_disaster_recovery_manifest(None, None, None, prof)
    assert res["status"] == "mocked"
