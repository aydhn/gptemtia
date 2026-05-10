import pytest
from ml.prediction_config import (
    MLPredictionProfile,
    get_ml_prediction_profile,
    list_ml_prediction_profiles,
    get_default_ml_prediction_profile,
    validate_ml_prediction_profiles,
    ConfigError
)

def test_validate_ml_prediction_profiles_passes():
    validate_ml_prediction_profiles()

def test_get_default_ml_prediction_profile():
    profile = get_default_ml_prediction_profile()
    assert isinstance(profile, MLPredictionProfile)

def test_list_ml_prediction_profiles():
    profiles = list_ml_prediction_profiles()
    assert len(profiles) > 0
    assert all(p.enabled for p in profiles)

def test_get_ml_prediction_profile_not_found():
    with pytest.raises(ConfigError):
        get_ml_prediction_profile("non_existent_profile")
