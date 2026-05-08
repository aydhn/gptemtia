from risk.volatility_risk import calculate_volatility_risk_score


def test_volatility_risk_high():
    ctx = {
        "atr_pct_14": 0.07,
        "percentile_atr_pct_14_120": 98,
        "event_range_shock_high": True,
    }
    res = calculate_volatility_risk_score(ctx)
    assert res.score > 0.8
    assert "ATR percentage > 6%" in res.reasons


def test_volatility_risk_low():
    ctx = {"atr_pct_14": 0.005, "percentile_atr_pct_14_120": 20}
    res = calculate_volatility_risk_score(ctx)
    assert res.score < 0.4
    assert res.report_builder = ReportBuilder()ed
