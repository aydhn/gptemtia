import pandas as pd
from backup_recovery.restore_dry_run import build_restore_dry_run_plan
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_build_restore_dry_run_plan():
    prof = get_default_backup_recovery_profile()
    plan, sum = build_restore_dry_run_plan({}, prof)
    assert plan.empty
