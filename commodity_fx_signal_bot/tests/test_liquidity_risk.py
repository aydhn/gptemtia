from risk.liquidity_risk import calculate_liquidity_risk_score


def test_liquidity_risk_unusable():
    ctx = {"volume_is_usable": False}
    res = calculate_liquidity_risk_score(ctx)
    assert res.score > 0.4
    assert "Volume data is unreliable/unusable" in res.warnings


def test_liquidity_risk_low_rel_volume():
    ctx = {"volume_is_usable": True, "relative_volume_20": 0.2}
    res = calculate_liquidity_risk_score(ctx)
    assert res.score > 0.3
