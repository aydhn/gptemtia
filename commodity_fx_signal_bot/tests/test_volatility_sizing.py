from sizing.volatility_sizing import (
    calculate_volatility_adjustment_factor,
    calculate_risk_readiness_adjustment,
    calculate_pretrade_risk_adjustment,
    apply_sizing_adjustment,
)


def test_calculate_volatility_adjustment_factor():
    # Low volatility, low atr pct -> increased size
    assert calculate_volatility_adjustment_factor(0.01, 0.1) > 1.0
    # High volatility -> decreased size
    assert calculate_volatility_adjustment_factor(0.02, 0.95) < 1.0
    # High atr pct -> decreased size
    assert calculate_volatility_adjustment_factor(0.06, 0.5) < 1.0
    # Values between 0.1 and 1.5
    assert 0.1 <= calculate_volatility_adjustment_factor(0.06, 0.95) <= 1.5


def test_calculate_risk_readiness_adjustment():
    assert calculate_risk_readiness_adjustment(0.4) < 1.0
    assert calculate_risk_readiness_adjustment(0.9) > 1.0


def test_calculate_pretrade_risk_adjustment():
    assert calculate_pretrade_risk_adjustment(0.9) < 1.0
    assert calculate_pretrade_risk_adjustment(0.1) > 1.0


def test_apply_sizing_adjustment():
    assert apply_sizing_adjustment(100.0, 0.5) == 50.0
    assert apply_sizing_adjustment(float("nan"), 0.5) == 0.0
