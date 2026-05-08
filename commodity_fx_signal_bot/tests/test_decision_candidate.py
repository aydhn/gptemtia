from decisions.decision_candidate import (
    DecisionCandidate,
    build_decision_id,
    decision_candidate_to_dict,
)


def test_build_decision_id():
    id1 = build_decision_id("GC=F", "1d", "2023-01-01", "long_bias", "trend")
    id2 = build_decision_id("GC=F", "1d", "2023-01-01", "long_bias", "trend")
    assert id1 == id2
    assert isinstance(id1, str)


def test_decision_candidate_to_dict():
    c = DecisionCandidate(
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
        decision_score=1.0,
        decision_confidence=1.0,
        decision_quality_score=1.0,
        strategy_readiness_score=1.0,
        report_builder = ReportBuilder()ed_decision_filters=True,
        no_trade_reasons=[],
        conflict_reasons=[],
        warnings=[],
    )
    d = decision_candidate_to_dict(c)
    assert d["symbol"] == "GC=F"
