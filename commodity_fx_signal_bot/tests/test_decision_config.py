import pytest
from decisions.decision_config import (
    get_decision_profile,
    list_decision_profiles,
    validate_decision_profiles,
    get_default_decision_profile,
    normalize_decision_weights,
    ConfigError,
)


def test_validate_decision_profiles():
    validate_decision_profiles()  # Should not raise


def test_get_default_decision_profile():
    prof = get_default_decision_profile()
    assert prof is not None
    assert prof.name == "balanced_directional_decision"


def test_normalize_decision_weights():
    w = {"a": 1.0, "b": 1.0}
    norm = normalize_decision_weights(w)
    assert norm["a"] == 0.5
    assert norm["b"] == 0.5


def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_decision_profile("unknown_profile_123")
