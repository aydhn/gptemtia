from backup_recovery.recovery_gap_analysis import detect_recovery_gaps
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_detect_recovery_gaps():
    prof = get_default_backup_recovery_profile()
    df = detect_recovery_gaps(None, None, None, None, prof)
    assert df.empty
