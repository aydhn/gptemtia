from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.strategy_family_profiles import build_strategy_family_profile_registry

def test_strategy_family():
    p = get_default_advanced_config_system_profile()
    df, summary = build_strategy_family_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "trend_following_research" in names
    assert "mean_reversion_research" in names
