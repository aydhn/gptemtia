import pytest
from advanced_gap_closure.gap_closure_config import get_default_functional_gap_closure_profile, validate_functional_gap_closure_profiles

def test_config_phases():
    profile = get_default_functional_gap_closure_profile()
    assert profile.current_phase == 105
    assert profile.target_final_phase == 160
    assert profile.next_phase == 106
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False

def test_validation():
    validate_functional_gap_closure_profiles()
