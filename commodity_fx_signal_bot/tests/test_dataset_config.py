import pytest
from ml.dataset_config import get_ml_dataset_profile, list_ml_dataset_profiles, validate_ml_dataset_profiles, get_default_ml_dataset_profile, ConfigError

def test_validate_ml_dataset_profiles():
    # Should run without error
    validate_ml_dataset_profiles()

def test_get_default_ml_dataset_profile():
    prof = get_default_ml_dataset_profile()
    assert prof is not None
    assert prof.name == "balanced_supervised_dataset"

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_ml_dataset_profile("unknown_profile_123")
