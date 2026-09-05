from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.asset_class_profiles import build_asset_class_profile_registry

def test_asset_class():
    p = get_default_advanced_config_system_profile()
    df, summary = build_asset_class_profile_registry(p)
    assert len(df) > 0
