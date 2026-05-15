from strategies.strategy_candidate import StrategyCandidate
from strategies.strategy_pool import StrategyCandidatePool


def make_candidate(score):
    return StrategyCandidate(
        symbol="TEST",
        timeframe="1d",
        timestamp="2023",
        strategy_id=f"{score}",
        strategy_family="fam",
        strategy_status="stat",
        source_decision_id="2",
        source_decision_label="lbl",
        directional_bias="long",
        candidate_type="type",
        decision_score=1.0,
        decision_confidence=1.0,
        decision_quality_score=1.0,
        strategy_selection_score=score,
        strategy_fit_score=1.0,
        regime_fit_score=1.0,
        mtf_fit_score=1.0,
        macro_fit_score=1.0,
        asset_profile_fit_score=1.0,
        conflict_penalty=0.0,
        strategy_readiness_score=1.0,
        passed_strategy_filters=True,
        block_reasons=[],
        watchlist_reasons=[],
        warnings=[],
    )


def test_strategy_pool_add_and_to_dataframe():
    pool = StrategyCandidatePool()
    pool.add(make_candidate(0.8))
    pool.add(make_candidate(0.9))

    df = pool.to_dataframe()
    assert len(df) == 2
    assert "strategy_selection_score" in df.columns


def test_strategy_pool_rank():
    pool = StrategyCandidatePool()
    pool.add(make_candidate(0.8))
    pool.add(make_candidate(0.9))

    ranked = pool.rank()
    assert ranked[0].strategy_selection_score == 0.9


def test_strategy_pool_summarize():
    pool = StrategyCandidatePool()
    pool.add(make_candidate(0.8))
    summ = pool.summarize()
    assert summ["total_strategy_candidates"] == 1
    assert summ["average_selection_score"] == 0.8
