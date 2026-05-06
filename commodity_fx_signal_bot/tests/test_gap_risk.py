from risk.gap_risk import calculate_gap_risk_score


def test_gap_risk_high():
    ctx = {"abs_gap_pct": 0.05, "event_large_gap": True}
    res = calculate_gap_risk_score(ctx)
    assert res.score > 0.7
    assert "Large gap event detected" in res.reasons


def test_gap_risk_missing_context():
    ctx = {}
    res = calculate_gap_risk_score(ctx)
    assert "Missing gap percent context" in res.warnings
