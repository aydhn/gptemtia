from strategies.strategy_candidate import (
    StrategyCandidate,
    build_strategy_id,
    strategy_candidate_to_dict,
)


def test_build_strategy_id():
    id1 = build_strategy_id("TEST", "1d", "2023", "family", "src")
    id2 = build_strategy_id("TEST", "1d", "2023", "family", "src")
    assert id1 == id2
    assert isinstance(id1, str)


def test_strategy_candidate_to_dict():
    c = StrategyCandidate(
        symbol="TEST",
        timeframe="1d",
        timestamp="2023",
        strategy_id="1",
        strategy_family="fam",
        strategy_status="stat",
        source_decision_id="2",
        source_decision_label="lbl",
        directional_bias="long",
        candidate_type="type",
        decision_score=1.0,
        decision_confidence=1.0,
        decision_quality_score=1.0,
        strategy_selection_score=1.0,
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
    d = strategy_candidate_to_dict(c)
    assert d["symbol"] == "TEST"
    assert d["strategy_selection_score"] == 1.0
