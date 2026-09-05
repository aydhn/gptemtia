from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.portfolio_profiles import build_portfolio_profile_registry

def test_portfolio():
    p = get_default_advanced_config_system_profile()
    df, summary = build_portfolio_profile_registry(p)
    assert len(df) > 0
