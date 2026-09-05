import pytest
from advanced_feature_validation.feature_validation_profile_registry import (
    get_feature_validation_profiles_registry,
    get_feature_validation_profile,
    get_feature_validation_profiles_summary,
)


def test_feature_validation_profile_registry():
    profiles = get_feature_validation_profiles_registry()
    assert len(profiles) >= 3
    assert "default" in profiles
    assert "strict" in profiles
    assert "lenient" in profiles

    default_prof = get_feature_validation_profile("default")
    assert default_prof.profile_name == "default"
    assert default_prof.non_signal is True

    summary = get_feature_validation_profiles_summary()
    assert summary["total_profiles"] == len(profiles)
    assert summary["current_phase"] == 121
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 122
    assert summary["dry_run_mandate"] is True
