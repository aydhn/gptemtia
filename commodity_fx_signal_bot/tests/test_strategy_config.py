import pytest

from strategies.strategy_config import (
    ConfigError,
    get_default_strategy_selection_profile,
    get_strategy_selection_profile,
    normalize_strategy_weights,
    validate_strategy_selection_profiles,
)


def test_validate_strategy_selection_profiles():
    validate_strategy_selection_profiles()


def test_get_default_strategy_selection_profile():
    profile = get_default_strategy_selection_profile()
    assert profile is not None
    assert profile.name == "balanced_strategy_selection"


def test_normalize_strategy_weights():
    weights = {"a": 2.0, "b": 2.0}
    norm = normalize_strategy_weights(weights)
    assert norm["a"] == 0.5
    assert norm["b"] == 0.5


def test_unknown_profile_raises_error():
    with pytest.raises(ConfigError):
        get_strategy_selection_profile("unknown_profile_123")
