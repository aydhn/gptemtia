from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.backup_packaging_readiness import build_backup_packaging_readiness_report
from config.paths import PROJECT_ROOT

def test_backup_packaging_readiness():
    profile = get_default_local_readiness_profile()
    df, s = build_backup_packaging_readiness_report(PROJECT_ROOT, profile)
    assert not df.empty
