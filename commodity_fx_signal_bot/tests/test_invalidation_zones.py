import pytest
from levels.invalidation_zones import (
    calculate_atr_invalidation_zone,
    calculate_structure_invalidation_zone,
)


def test_atr_invalidation():
    res = calculate_atr_invalidation_zone(100.0, 1.0, "long_bias_candidate")
    assert res["invalidation_level_candidate"] == 98.5
    assert res["invalidation_zone_low_candidate"] == 98.0


def test_structure_invalidation():
    res = calculate_structure_invalidation_zone(98.0, 1.0, "long_bias_candidate")
    assert res["invalidation_level_candidate"] == 98.0
    assert res["invalidation_zone_low_candidate"] == 97.0
