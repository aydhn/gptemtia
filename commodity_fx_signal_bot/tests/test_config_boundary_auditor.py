
import pytest
from pathlib import Path
from secrets_hygiene.config_boundary_auditor import (
    audit_settings_for_secret_defaults,
    audit_config_files_for_raw_credentials,
    audit_env_alignment_for_secret_hygiene
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_audit_settings_for_secret_defaults():
    df, s = audit_settings_for_secret_defaults(Path("."))
    assert not df.empty

def test_audit_config_files_for_raw_credentials():
    profile = get_default_secrets_hygiene_profile()
    df, s = audit_config_files_for_raw_credentials(Path("."), profile)
    assert df.empty

def test_audit_env_alignment():
    df, s = audit_env_alignment_for_secret_hygiene(Path("."))
    assert not df.empty
