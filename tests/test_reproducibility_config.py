"""Test config."""
import pytest
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import validate_local_reproducibility_governance_profiles, get_default_local_reproducibility_governance_profile, ConfigError, get_local_reproducibility_governance_profile

def test_config():
    validate_local_reproducibility_governance_profiles()
    p = get_default_local_reproducibility_governance_profile()
    assert p.language
    assert p.max_items > 0
    assert p.max_rows > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default
    assert not p.allow_real_build
    with pytest.raises(ConfigError):
        get_local_reproducibility_governance_profile("unknown")
