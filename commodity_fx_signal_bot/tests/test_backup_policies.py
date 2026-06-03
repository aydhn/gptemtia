from backup_recovery.backup_policies import build_default_backup_policies, backup_policies_to_dataframe
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_build_default_backup_policies():
    prof = get_default_backup_recovery_profile()
    pols = build_default_backup_policies(prof)
    assert len(pols) > 0
    df = backup_policies_to_dataframe(pols)
    assert not df.empty
