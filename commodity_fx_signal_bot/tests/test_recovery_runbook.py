from backup_recovery.recovery_runbook import build_project_state_recovery_runbook
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_build_project_state_recovery_runbook():
    prof = get_default_backup_recovery_profile()
    text, sum = build_project_state_recovery_runbook({}, None, None, prof)
    assert "Runbook" in text
