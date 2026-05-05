from decisions.decision_pool import DecisionCandidatePool
from decisions.decision_candidate import DecisionCandidate


def _mock_cand(score=0.5):
    return DecisionCandidate(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023",
        decision_id="1",
        decision_label="x",
        directional_bias="y",
        candidate_type="z",
        source_candidate_count=1,
        top_source_candidate_score=1.0,
        signal_score_component=1.0,
        directional_consensus_component=1.0,
        regime_confirmation_component=1.0,
        mtf_confirmation_component=1.0,
        macro_context_component=1.0,
        asset_profile_fit_component=1.0,
        quality_component=1.0,
        risk_precheck_component=1.0,
        conflict_score=0.0,
        decision_score=score,
        decision_confidence=1.0,
        decision_quality_score=1.0,
        strategy_readiness_score=1.0,
        passed_decision_filters=True,
        no_trade_reasons=[],
        conflict_reasons=[],
        warnings=[],
    )


def test_pool_operations():
    pool = DecisionCandidatePool()
    pool.add(_mock_cand(0.8))
    pool.add(_mock_cand(0.4))

    ranked = pool.rank()
    assert ranked[0].decision_score == 0.8

    df = pool.to_dataframe()
    assert len(df) == 2

    summ = pool.summarize()
    assert summ["total_decisions"] == 2
