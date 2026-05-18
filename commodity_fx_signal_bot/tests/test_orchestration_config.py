import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from orchestration.orchestration_config import (
    validate_orchestration_profiles,
    get_default_orchestration_profile,
    get_orchestration_profile,
    ConfigError
)

def test_validate_orchestration_profiles():
    validate_orchestration_profiles()

def test_get_default_orchestration_profile():
    profile = get_default_orchestration_profile()
    assert profile is not None
    assert profile.max_symbols_per_run > 0

def test_get_unknown_profile():
    with pytest.raises(ConfigError):
        get_orchestration_profile("unknown_nonexistent_profile")
