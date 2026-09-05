from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.data_provider_preference_profiles import build_data_provider_preference_profile_registry

def test_data_provider_preference():
    p = get_default_advanced_config_system_profile()
    df, summary = build_data_provider_preference_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "no_scraping_public_api_preferred" in names
