from backup_recovery.backup_safety import scan_backup_inventory_for_secret_risk
from pathlib import Path

def test_scan_backup_inventory_for_secret_risk():
    df, sum = scan_backup_inventory_for_secret_risk(None, Path("."))
    assert df.empty
