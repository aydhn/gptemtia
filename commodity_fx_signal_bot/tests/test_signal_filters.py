import pytest
from signals.signal_candidate import SignalCandidate
from signals.signal_filters import (
    filter_candidates_by_score,
    filter_candidates_by_quality,
    filter_candidates_by_conflict,
    filter_candidates_by_direction,
    rank_candidates,
)


def test_signal_filters():
    c1 = SignalCandidate(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023-01-01",
        candidate_id="1",
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
        conflict_score=0.1,
        risk_precheck_score=1.0,
        candidate_score=0.8,
        confidence_score=1.0,
        quality_score=0.9,
        passed_pre_filters=True,
        warnings=[],
    )
    c2 = SignalCandidate(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023-01-01",
        candidate_id="2",
        candidate_type="test",
        directional_bias="bearish",
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
        conflict_score=0.8,
        risk_precheck_score=1.0,
        candidate_score=0.4,
        confidence_score=1.0,
        quality_score=0.4,
        passed_pre_filters=False,
        warnings=[],
    )

    cands = [c1, c2]

    assert len(filter_candidates_by_score(cands, 0.5)) == 1
    assert len(filter_candidates_by_quality(cands, 0.5)) == 1
    assert len(filter_candidates_by_conflict(cands, 0.5)) == 1
    assert len(filter_candidates_by_direction(cands, "bullish")) == 1

    ranked = rank_candidates(cands)
    assert ranked[0].candidate_score == 0.8
