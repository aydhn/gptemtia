import pytest
from local_post_completion_preservation.preservation_config import get_default_local_post_completion_preservation_profile, get_local_post_completion_preservation_profile, validate_local_post_completion_preservation_profiles, ConfigError

def test_config():
    profile = get_default_local_post_completion_preservation_profile()
    assert profile.language != ""
    assert profile.max_items > 0
    assert profile.max_inventory_rows > 0
    assert 0 <= profile.min_readiness_score <= 1
    assert profile.dry_run_default == True
    assert not profile.allow_real_archive_seal
    
    validate_local_post_completion_preservation_profiles()
    
    with pytest.raises(ConfigError):
        get_local_post_completion_preservation_profile("unknown")
