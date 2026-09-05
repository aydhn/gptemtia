from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.ml_profiles import build_ml_profile_registry

def test_ml():
    p = get_default_advanced_config_system_profile()
    df, summary = build_ml_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "no_ml_baseline" in names
    assert "gpu_optional_ml_research" in names
