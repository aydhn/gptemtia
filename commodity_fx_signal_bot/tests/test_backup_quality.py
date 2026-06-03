from backup_recovery.backup_quality import check_project_state_inventory_quality
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_check_project_state_inventory_quality():
    prof = get_default_backup_recovery_profile()
    res = check_project_state_inventory_quality(None, prof)
    assert res["passed"] == True
