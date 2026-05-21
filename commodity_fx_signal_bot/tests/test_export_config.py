import pytest
from report_exports.export_config import (
    validate_report_export_profiles,
    get_default_report_export_profile,
    get_report_export_profile,
    ConfigError
)

def test_validate_report_export_profiles():
    validate_report_export_profiles()

def test_get_default_report_export_profile():
    profile = get_default_report_export_profile()
    assert profile.name == "balanced_report_export"

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_report_export_profile("unknown_profile_123")
