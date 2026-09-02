
import pytest
from local_closure.closure_config import get_local_closure_profile, get_default_local_closure_profile, validate_local_closure_profiles

def test_validate_local_closure_profiles():
    validate_local_closure_profiles()

def test_get_default_local_closure_profile():
    p = get_default_local_closure_profile()
    assert p.name == "balanced_local_closure"
    assert p.language == "tr"
    assert p.max_items > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert not p.allow_real_v1_release
    assert not p.allow_live_trading_claim

def test_unknown_profile():
    with pytest.raises(Exception):
        get_local_closure_profile("unknown_profile")
