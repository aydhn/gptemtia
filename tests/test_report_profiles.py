from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.report_profiles import build_report_profile_registry

def test_report():
    p = get_default_advanced_config_system_profile()
    df, summary = build_report_profile_registry(p)
    assert len(df) > 0
