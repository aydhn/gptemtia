from risk.asset_risk import calculate_asset_profile_risk_score


def test_asset_risk_gap_warning():
    ctx = {"event_asset_high_gap_risk_warning": True}
    res = calculate_asset_profile_risk_score(ctx)
    assert res.score > 0.4
    assert "Asset high gap risk warning" in res.reasons


def test_asset_risk_rs_mismatch():
    ctx = {"asset_relative_strength_regime_label": "weak", "directional_bias": "long"}
    res = calculate_asset_profile_risk_score(ctx)
    assert res.score > 0.3
