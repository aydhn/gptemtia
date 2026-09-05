from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.timeframe_profiles import build_timeframe_profile_registry

def test_timeframe():
    p = get_default_advanced_config_system_profile()
    df, summary = build_timeframe_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "daily_research" in names
    assert "multi_timeframe_research" in names
