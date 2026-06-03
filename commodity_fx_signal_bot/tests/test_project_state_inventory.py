from pathlib import Path
from backup_recovery.project_state_inventory import scan_project_state
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_scan_project_state(tmp_path):
    prof = get_default_backup_recovery_profile()
    df, sum = scan_project_state(tmp_path, prof)
    assert df is not None
