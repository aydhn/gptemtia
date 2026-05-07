import pytest
import numpy as np
from levels.level_models import (
    clamp_level_score,
    calculate_distance_pct,
    is_valid_level_for_direction,
    LevelInputSnapshot,
    level_input_snapshot_to_dict,
)


def test_clamp_score():
    assert clamp_level_score(1.5) == 1.0
    assert clamp_level_score(-0.5) == 0.0
    assert clamp_level_score(0.5) == 0.5
    assert clamp_level_score(np.nan) == 0.0


def test_calculate_distance_pct():
    assert calculate_distance_pct(100.0, 90.0) == 0.1
    assert calculate_distance_pct(100.0, 110.0) == 0.1
    assert calculate_distance_pct(np.nan, 100.0) is None


def test_is_valid_level():
    assert (
        is_valid_level_for_direction(100.0, 90.0, "long_bias_candidate", "stop") is True
    )
    assert (
        is_valid_level_for_direction(100.0, 110.0, "long_bias_candidate", "stop")
        is False
    )
    assert (
        is_valid_level_for_direction(100.0, 110.0, "short_bias_candidate", "stop")
        is True
    )


def test_snapshot_dict():
    snap = LevelInputSnapshot(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023-01-01",
        asset_class="metals",
        strategy_family="trend",
        condition_label="cond1",
        directional_bias="long_bias_candidate",
        sizing_label="approved",
        risk_label="approved",
        latest_close=100.0,
        atr_value=1.0,
        atr_pct=0.01,
        volatility_percentile=50.0,
        sizing_readiness_score=0.8,
        total_pretrade_risk_score=0.5,
        theoretical_units=1.0,
        adjusted_theoretical_units=1.0,
        context_available=True,
        warnings=[],
    )
    d = level_input_snapshot_to_dict(snap)
    assert d["symbol"] == "GC=F"
    assert "warnings" in d
