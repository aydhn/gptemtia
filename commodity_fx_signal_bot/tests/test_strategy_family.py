from strategies.strategy_family import (
    get_compatible_families_for_decision,
    get_strategy_family_spec,
    validate_strategy_family_specs,
)


def test_validate_strategy_family_specs():
    validate_strategy_family_specs()


def test_get_strategy_family_spec():
    spec = get_strategy_family_spec("trend_following")
    assert spec.family == "trend_following"


def test_get_compatible_families_for_decision():
    families = get_compatible_families_for_decision(
        "long_bias_candidate", "trend_following"
    )
    assert "trend_following" in families


def test_no_trade_candidate_returns_no_trade_family():
    families = get_compatible_families_for_decision("no_trade_candidate", "unknown")
    assert families == ["no_trade"]
