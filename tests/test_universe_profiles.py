from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.universe_profiles import build_universe_profile_registry

def test_universe():
    p = get_default_advanced_config_system_profile()
    df, summary = build_universe_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "major_fx_pairs" in names
    assert "precious_metals" in names
