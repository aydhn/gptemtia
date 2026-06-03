from backup_recovery.backup_report_builder import build_backup_disclaimer

def test_build_backup_disclaimer():
    res = build_backup_disclaimer()
    assert "WARNING" in res
