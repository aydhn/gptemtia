import pytest
from levels.volatility_levels import (
    calculate_volatility_level_adjustment,
    build_volatility_adjusted_levels,
)


def test_calculate_volatility_adjustment():
    assert calculate_volatility_level_adjustment(0.01, 85.0) == 1.5
    assert calculate_volatility_level_adjustment(0.01, 15.0) == 0.8
    assert calculate_volatility_level_adjustment(None, None) == 1.0


def test_build_adjusted_levels():
    res = build_volatility_adjusted_levels(100.0, 1.0, 2.0, "long_bias_candidate", 1.5)
    assert res["volatility_adjusted_stop_candidate"] == 98.5
    assert res["volatility_adjusted_target_candidate"] == 103.0
