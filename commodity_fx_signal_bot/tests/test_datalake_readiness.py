from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.datalake_readiness import build_datalake_readiness_report
from config.paths import PROJECT_ROOT

def test_datalake_readiness():
    profile = get_default_local_readiness_profile()
    df, s = build_datalake_readiness_report(PROJECT_ROOT, profile)
    assert not df.empty
