from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.tests_readiness import build_test_readiness_report
from config.paths import PROJECT_ROOT

def test_tests_readiness():
    profile = get_default_local_readiness_profile()
    df, s = build_test_readiness_report(PROJECT_ROOT, profile)
    assert s["total_test_files"] >= 0
