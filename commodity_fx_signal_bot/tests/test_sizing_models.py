from sizing.sizing_models import (
    clamp_sizing_score,
    safe_positive_float,
    calculate_notional_from_risk_unit,
    SizingInputSnapshot,
    sizing_input_snapshot_to_dict,
)
import math


def test_clamp_sizing_score():
    assert clamp_sizing_score(-1.0) == 0.0
    assert clamp_sizing_score(2.0) == 1.0
    assert clamp_sizing_score(0.5) == 0.5
    assert clamp_sizing_score(float("nan")) == 0.0


def test_safe_positive_float():
    assert safe_positive_float(5.0) == 5.0
    assert safe_positive_float(-5.0) is None
    assert safe_positive_float("invalid") is None
    assert safe_positive_float(float("inf")) is None


def test_calculate_notional_from_risk_unit():
    assert calculate_notional_from_risk_unit(100.0, 10.0) == 10.0
    assert calculate_notional_from_risk_unit(100.0, 0.0) == 0.0


def test_sizing_input_snapshot_to_dict():
    snapshot = SizingInputSnapshot(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023-01-01",
        asset_class="metals",
        strategy_family="trend",
        condition_label="test",
        directional_bias="long",
        risk_label="risk_approved",
        risk_severity="low",
        total_pretrade_risk_score=0.1,
        risk_readiness_score=0.9,
        latest_close=100.0,
        atr_value=2.0,
        atr_pct=0.02,
        volatility_percentile=0.5,
        context_available=True,
        warnings=[],
    )
    d = sizing_input_snapshot_to_dict(snapshot)
    assert d["symbol"] == "GC=F"
    assert "latest_close" in d
