import pytest
from local_project_completion.completion_config import get_default_local_project_completion_profile, validate_local_project_completion_profiles, get_local_project_completion_profile

def test_validate_local_project_completion_profiles():
    validate_local_project_completion_profiles()

def test_get_default_local_project_completion_profile():
    p = get_default_local_project_completion_profile()
    assert p.language != ""
    assert p.max_items > 0
    assert p.max_inventory_rows > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert p.allow_real_project_closure is False

def test_get_unknown_profile():
    with pytest.raises(ValueError):
        get_local_project_completion_profile("unknown_profile")
