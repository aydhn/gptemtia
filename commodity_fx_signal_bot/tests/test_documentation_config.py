import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pytest
from documentation.documentation_config import (
    DocumentationProfile,
    get_documentation_profile,
    list_documentation_profiles,
    validate_documentation_profiles,
    get_default_documentation_profile,
    ConfigError
)

def test_validate_documentation_profiles_valid():
    try:
        validate_documentation_profiles()
    except ConfigError:
        pytest.fail("validate_documentation_profiles should not raise exception for default profiles")

def test_get_default_documentation_profile():
    profile = get_default_documentation_profile()
    assert profile.name == "balanced_documentation_pack"
    assert profile.language == "tr"

def test_get_documentation_profile_unknown():
    with pytest.raises(ConfigError):
        get_documentation_profile("unknown_profile")
