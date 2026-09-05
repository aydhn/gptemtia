from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.research_mode_presets import build_research_mode_preset_registry

def test_research_mode_presets():
    p = get_default_advanced_config_system_profile()
    df, summary = build_research_mode_preset_registry(p)
    assert len(df) > 0
    # verify presets
    presets = df["mode_label"].tolist()
    assert "short_term_fx_research" in presets
