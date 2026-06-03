import pandas as pd
from backup_recovery.backup_manifest import build_backup_manifest
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_build_backup_manifest():
    prof = get_default_backup_recovery_profile()
    df = pd.DataFrame()
    manifest = build_backup_manifest(prof, df)
    assert manifest.profile_name == prof.name
