from risk.risk_pool import RiskCandidatePool
from risk.risk_candidate import RiskPrecheckCandidate


def test_risk_pool_add_and_df():
    pool = RiskCandidatePool()
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
        "risk_approval_candidate",
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
    pool.add(cand)
    df = pool.to_dataframe()
    assert not df.empty
    assert len(df) == 1

    summary = pool.summarize()
    assert summary["total_risk_candidates"] == 1
    assert summary["passed_risk_candidates"] == 1
