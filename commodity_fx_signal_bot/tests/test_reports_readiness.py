from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.reports_readiness import build_report_output_readiness_report
from config.paths import PROJECT_ROOT

def test_reports_readiness():
    profile = get_default_local_readiness_profile()
    df, s = build_report_output_readiness_report(PROJECT_ROOT, profile)
    assert not df.empty
