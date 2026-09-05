from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.backtest_profiles import build_backtest_profile_registry

def test_backtest():
    p = get_default_advanced_config_system_profile()
    df, summary = build_backtest_profile_registry(p)
    assert len(df) > 0
