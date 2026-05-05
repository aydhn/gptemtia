from signals.signal_candidate import (
    SignalCandidate,
    build_candidate_id,
    signal_candidate_to_dict,
)


def test_build_candidate_id_deterministic():
    id1 = build_candidate_id("GC=F", "1d", "2023-01-01", "trend_following", "bullish")
    id2 = build_candidate_id("GC=F", "1d", "2023-01-01", "trend_following", "bullish")
    assert id1 == id2
    assert len(id1) == 16


def test_signal_candidate_to_dict():
    c = SignalCandidate(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023-01-01",
        candidate_id="xyz",
        candidate_type="test",
        directional_bias="bullish",
        primary_event_group="trend",
        active_events=[],
        event_count=0,
        event_strength_score=1.0,
        category_confluence_score=1.0,
        trend_context_score=1.0,
        regime_context_score=1.0,
        mtf_context_score=1.0,
        macro_context_score=1.0,
        asset_profile_context_score=1.0,
        data_quality_score=1.0,
        conflict_score=0.0,
        risk_precheck_score=1.0,
        candidate_score=1.0,
        confidence_score=1.0,
        quality_score=1.0,
        passed_pre_filters=True,
        warnings=[],
    )
    d = signal_candidate_to_dict(c)
    assert d["symbol"] == "GC=F"
    assert "candidate_score" in d
