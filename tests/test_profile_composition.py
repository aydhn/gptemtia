from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_composition import build_composed_research_profile_registry

def test_composition():
    p = get_default_advanced_config_system_profile()
    df, summary = build_composed_research_profile_registry(p)
    names = df["composed_profile_name"].tolist()
    assert "full_advanced_research_dry_run" in names
    
    for _, row in df.iterrows():
        assert row["manual_review_required"] is True
