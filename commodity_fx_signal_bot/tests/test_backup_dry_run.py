import pandas as pd
from backup_recovery.backup_dry_run import build_backup_dry_run_plan
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_build_backup_dry_run_plan():
    prof = get_default_backup_recovery_profile()
    df = pd.DataFrame([{"include_policy": "include", "backup_scope": "critical_source_scope"}])
    plan, sum = build_backup_dry_run_plan(df, {}, prof)
    assert not plan.empty
