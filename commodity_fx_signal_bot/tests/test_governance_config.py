import pytest

from governance.governance_config import (
    ConfigError,
    get_default_governance_profile,
    get_governance_profile,
    validate_governance_profiles,
)


def test_validate_governance_profiles_passes():
    validate_governance_profiles()

def test_get_default_governance_profile():
    profile = get_default_governance_profile()
    assert profile.name == "balanced_research_governance"
    assert profile.max_file_hash_mb > 0
    assert profile.lineage_max_depth > 0
    assert profile.scan_data_lake or profile.scan_reports_output

def test_get_unknown_profile():
    with pytest.raises(ConfigError):
        get_governance_profile("unknown_profile")
