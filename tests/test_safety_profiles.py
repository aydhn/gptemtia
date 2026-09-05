from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.safety_profiles import build_safety_profile_registry

def test_safety():
    p = get_default_advanced_config_system_profile()
    df, summary = build_safety_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "strict_no_advice_safety" in names
    assert "strict_no_live_broker_safety" in names
