from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.feature_profiles import build_feature_profile_registry

def test_feature():
    p = get_default_advanced_config_system_profile()
    df, summary = build_feature_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "standard_technical_features" in names
    assert "macro_factor_features" in names
    assert "cross_asset_features" in names
