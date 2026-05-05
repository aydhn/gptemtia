import pytest
import pandas as pd
from signals.signal_candidate import SignalCandidate
from signals.signal_pool import SignalCandidatePool


def test_signal_candidate_pool():
    pool = SignalCandidatePool()

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
        candidate_score=0.8,
        confidence_score=1.0,
        quality_score=1.0,
        passed_pre_filters=True,
        warnings=[],
    )

    pool.add(c)
    assert len(pool.candidates) == 1

    df = pool.to_dataframe()
    assert not df.empty

    pool2 = SignalCandidatePool.from_dataframe(df)
    assert len(pool2.candidates) == 1

    summary = pool2.summarize()
    assert summary["total_candidates"] == 1

    ranked = pool2.rank()
    assert len(ranked) == 1
