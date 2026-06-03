from backup_recovery.integrity_manifest import build_backup_integrity_manifest
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_build_backup_integrity_manifest():
    prof = get_default_backup_recovery_profile()
    df, sum = build_backup_integrity_manifest(None, prof)
    assert df.empty
