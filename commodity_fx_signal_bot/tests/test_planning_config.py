import pytest
from research_planning.planning_config import (
    get_research_planning_profile,
    list_research_planning_profiles,
    validate_research_planning_profiles,
    get_default_research_planning_profile,
    ConfigError
)

def test_validate_research_planning_profiles():
    validate_research_planning_profiles() # Should not raise

def test_get_default_research_planning_profile():
    profile = get_default_research_planning_profile()
    assert profile.name == "balanced_research_planning"
    assert profile.max_backlog_items > 0
    assert profile.high_priority_threshold >= profile.min_priority_score
    assert profile.dry_run is True

def test_get_unknown_profile():
    with pytest.raises(ConfigError):
        get_research_planning_profile("unknown_profile")
