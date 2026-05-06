from risk.regime_risk import calculate_regime_risk_score


def test_regime_risk_mismatch():
    ctx = {"strategy_family": "trend_following", "regime_primary_label": "range"}
    res = calculate_regime_risk_score(ctx)
    assert res.score > 0.5


def test_regime_risk_match():
    ctx = {
        "strategy_family": "trend_following",
        "regime_primary_label": "strong_trend",
        "regime_confidence": 0.9,
    }
    res = calculate_regime_risk_score(ctx)
    assert res.score < 0.3
