import pytest
from quality_gates.quality_config import (
    validate_quality_gate_profiles,
    get_default_quality_gate_profile,
    get_quality_gate_profile,
    ConfigError
)

def test_validate_quality_gate_profiles_passes():
    validate_quality_gate_profiles()

def test_get_default_quality_gate_profile():
    # Will use settings default "balanced_local_quality_gate"
    profile = get_default_quality_gate_profile()
    assert profile.name == "balanced_local_quality_gate"
    assert profile.max_test_runtime_seconds > 0
    assert 0.0 <= profile.min_pass_rate <= 1.0
    assert profile.allow_network_calls is False
    assert profile.allow_live_commands is False
    assert profile.allow_broker_commands is False
    assert profile.allow_deploy_commands is False
    assert profile.allow_background_daemons is False
    assert profile.release_candidate_dry_run is True

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_quality_gate_profile("unknown_profile")
