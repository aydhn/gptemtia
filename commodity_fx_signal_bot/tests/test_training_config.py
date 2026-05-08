import pytest
from ml.training_config import validate_ml_training_profiles, get_default_ml_training_profile, get_ml_training_profile, ConfigError

def test_validate_ml_training_profiles():
    # Should run without raising any exceptions
    validate_ml_training_profiles()

def test_get_default_ml_training_profile():
    profile = get_default_ml_training_profile()
    assert profile is not None
    assert profile.name == "balanced_baseline_training"
    assert profile.task_type == "classification"
    assert profile.default_model_family == "random_forest"

def test_get_ml_training_profile_unknown():
    with pytest.raises(ConfigError):
        get_ml_training_profile("unknown_profile_123")
