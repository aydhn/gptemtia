import pytest
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile, validate_advanced_config_system_profiles

def test_default_profile():
    p = get_default_advanced_config_system_profile()
    assert p.current_phase == 104
    assert p.target_final_phase == 160
    assert p.local_only is True
    assert p.non_production is True
    assert p.research_only is True
    assert p.allow_live_trading is False

def test_validation():
    validate_advanced_config_system_profiles()
