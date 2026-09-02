import pytest
from local_briefing.briefing_config import get_default_local_briefing_profile, validate_local_briefing_profiles

def test_validate_local_briefing_profiles():
    validate_local_briefing_profiles()

def test_get_default_local_briefing_profile():
    p = get_default_local_briefing_profile()
    assert p is not None
    assert p.dry_run_default is True
    assert p.allow_investment_advice is False
