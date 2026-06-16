from artifact_metadata.metadata_config import validate_artifact_metadata_profiles, get_default_artifact_metadata_profile, get_artifact_metadata_profile, ConfigError
import pytest

def test_validate_artifact_metadata_profiles():
    validate_artifact_metadata_profiles()

def test_get_default_artifact_metadata_profile():
    profile = get_default_artifact_metadata_profile()
    assert profile.name == "balanced_local_metadata"
    assert profile.language == "tr"
    assert profile.max_artifacts > 0
    assert profile.freshness_days_warning > 0
    assert profile.dry_run_default is True
    assert profile.allow_model_deployment_claims is False
    assert profile.allow_official_certification_claims is False
    assert profile.allow_investment_advice_claims is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_artifact_metadata_profile("unknown_profile")
