import pytest
from ml_integration.integration_config import (
    validate_ml_integration_profiles,
    get_default_ml_integration_profile,
    get_ml_integration_profile,
    ConfigError
)

def test_validate_ml_integration_profiles():
    # Should not raise any error
    validate_ml_integration_profiles()

def test_get_default_ml_integration_profile():
    profile = get_default_ml_integration_profile()
    assert profile.name == "balanced_ml_context_integration"
    assert 0.0 <= profile.min_confidence_score <= 1.0

def test_get_unknown_profile():
    with pytest.raises(ConfigError):
        get_ml_integration_profile("unknown_profile_123")
