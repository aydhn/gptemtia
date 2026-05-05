import pytest
from signals.signal_config import (
    get_default_signal_scoring_profile,
    validate_signal_scoring_profiles,
    get_signal_scoring_profile,
    normalize_component_weights,
)


def test_validate_signal_scoring_profiles_works():
    validate_signal_scoring_profiles()


def test_get_default_signal_scoring_profile():
    profile = get_default_signal_scoring_profile()
    assert profile is not None
    assert profile.name == "balanced_candidate_scoring"


def test_normalize_component_weights():
    w = {"a": 1.0, "b": 1.0}
    norm = normalize_component_weights(w)
    assert norm["a"] == 0.5
    assert norm["b"] == 0.5


def test_unknown_profile_raises():
    with pytest.raises(ValueError):
        get_signal_scoring_profile("nonexistent_profile")
