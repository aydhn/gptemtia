from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.config_profile_registry import build_advanced_config_profile_registry

def test_registry():
    p = get_default_advanced_config_system_profile()
    df, summary = build_advanced_config_profile_registry(p)
    assert len(df) > 0
