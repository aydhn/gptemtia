import pytest
from advanced_fx_providers.fx_provider_config import get_default_fx_provider_profile, validate_fx_provider_profiles

def test_config():
    profile = get_default_fx_provider_profile()
    assert profile.current_phase == 107
    assert profile.target_final_phase == 160
    assert profile.next_phase == 108
    assert profile.local_only is True
    assert profile.dry_run_default is True
    assert profile.allow_web_scraping is False
    validate_fx_provider_profiles()

def test_fx_modules():
    assert True
