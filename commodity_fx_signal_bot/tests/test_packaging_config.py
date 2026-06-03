import pytest
from portable_packaging.packaging_config import (
    validate_portable_packaging_profiles,
    get_default_portable_packaging_profile,
    get_portable_packaging_profile,
    ConfigError
)

def test_validate_portable_packaging_profiles():
    validate_portable_packaging_profiles()

def test_get_default_portable_packaging_profile():
    p = get_default_portable_packaging_profile()
    assert p is not None
    assert p.dry_run_default == True
    assert p.language != ""
    assert p.max_inventory_files > 0
    assert p.allow_archive_create == False
    assert p.allow_package_publish == False
    assert p.allow_docker == False
    assert p.allow_cloud_deploy == False
    assert p.allow_live_commands == False
    assert p.allow_broker_commands == False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_portable_packaging_profile("unknown")
