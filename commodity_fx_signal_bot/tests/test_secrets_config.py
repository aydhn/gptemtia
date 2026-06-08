
import pytest
from core.exceptions import ConfigError
from secrets_hygiene.secrets_config import (
    validate_secrets_hygiene_profiles,
    get_default_secrets_hygiene_profile,
    get_secrets_hygiene_profile,
    list_secrets_hygiene_profiles,
    SecretsHygieneProfile,
    _SECRETS_HYGIENE_PROFILES
)

def test_validate_secrets_hygiene_profiles():
    validate_secrets_hygiene_profiles()

def test_get_default_secrets_hygiene_profile():
    profile = get_default_secrets_hygiene_profile()
    assert profile.name == "balanced_local_secrets_hygiene"

def test_language_not_empty():
    profile = get_default_secrets_hygiene_profile()
    assert profile.language

def test_max_files_positive():
    profile = get_default_secrets_hygiene_profile()
    assert profile.max_files > 0

def test_entropy_threshold_positive():
    profile = get_default_secrets_hygiene_profile()
    assert profile.entropy_threshold > 0

def test_dry_run_default():
    profile = get_default_secrets_hygiene_profile()
    assert profile.dry_run_default is True

def test_allow_flags_false():
    profile = get_default_secrets_hygiene_profile()
    assert not profile.allow_secret_value_output
    assert not profile.allow_file_modification
    assert not profile.allow_secret_deletion
    assert not profile.allow_cloud_vault
    assert not profile.allow_external_scanner

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_secrets_hygiene_profile("unknown_profile")
