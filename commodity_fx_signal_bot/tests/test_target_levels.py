import pytest
from levels.target_levels import (
    calculate_target_from_stop_distance,
    build_target_ladder,
)


def test_calculate_target():
    assert (
        calculate_target_from_stop_distance(100.0, 2.0, "long_bias_candidate", 2.0)
        == 104.0
    )
    assert (
        calculate_target_from_stop_distance(100.0, 2.0, "short_bias_candidate", 2.0)
        == 96.0
    )


def test_build_ladder():
    ladder = build_target_ladder(100.0, 98.0, "long_bias_candidate", (1.0, 2.0))
    assert len(ladder) == 2
    assert ladder[0] == 102.0
    assert ladder[1] == 104.0
