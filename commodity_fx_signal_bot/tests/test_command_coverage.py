from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.command_coverage import build_safe_command_coverage_report
from config.paths import PROJECT_ROOT

def test_command_coverage():
    import pandas as pd
    profile = get_default_local_readiness_profile()
    df, s = build_safe_command_coverage_report(PROJECT_ROOT, pd.DataFrame(), profile)
    assert not df.empty
