import pytest
from local_delivery.delivery_config import get_local_delivery_profile, list_local_delivery_profiles, validate_local_delivery_profiles, get_default_local_delivery_profile, ConfigError

def test_validate_local_delivery_profiles():
    validate_local_delivery_profiles()

def test_get_default_local_delivery_profile():
    p = get_default_local_delivery_profile()
    assert p.name == "balanced_local_delivery"
    assert p.dry_run_default is True

def test_list_profiles():
    assert len(list_local_delivery_profiles()) > 0

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_delivery_profile("unknown")
