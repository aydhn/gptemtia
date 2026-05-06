from risk.risk_candidate import (
    build_risk_id,
    risk_candidate_to_dict,
    RiskPrecheckCandidate,
)


def test_build_risk_id():
    id1 = build_risk_id("AAPL", "1d", "2023-01-01", "rule1")
    id2 = build_risk_id("AAPL", "1d", "2023-01-01", "rule1")
    assert id1 == id2


def test_risk_candidate_to_dict():
    cand = RiskPrecheckCandidate(
        "AAPL",
        "1d",
        "2023-01-01",
        "id1",
        "rule1",
        "strat1",
        "trend",
        "cond1",
        "long",
        "approval",
        "low",
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.9,
        True,
        [],
        [],
        [],
    )
    d = risk_candidate_to_dict(cand)
    assert d["symbol"] == "AAPL"
    assert "notes" in d
