from risk.macro_risk import calculate_macro_risk_score


def test_macro_risk_fx_pressure():
    ctx = {
        "event_macro_try_depreciation_pressure": True,
        "usdtry_depreciation_pressure": 0.8,
    }
    res = calculate_macro_risk_score(ctx)
    assert res.score > 0.2


def test_macro_risk_missing():
    ctx = {}
    res = calculate_macro_risk_score(ctx)
    assert "Missing macro context" in res.warnings
