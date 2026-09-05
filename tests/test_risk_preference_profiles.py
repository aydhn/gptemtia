from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.risk_preference_profiles import build_risk_preference_profile_registry

def test_risk_preference():
    p = get_default_advanced_config_system_profile()
    df, summary = build_risk_preference_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "conservative_research" in names
    assert "balanced_research" in names
    assert "aggressive_research_only" in names
