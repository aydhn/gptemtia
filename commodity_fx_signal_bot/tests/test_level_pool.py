import pytest
from levels.level_pool import StopTargetLevelCandidatePool
from levels.level_candidate import StopTargetLevelCandidate


def test_pool_operations():
    pool = StopTargetLevelCandidatePool()
    cand = StopTargetLevelCandidate(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023",
        level_id="L1",
        source_sizing_id="",
        source_risk_id="",
        source_rule_condition_id="",
        strategy_family="",
        condition_label="",
        directional_bias="",
        asset_class="",
        level_label="level_approved_candidate",
        level_method="",
        level_severity="",
        latest_close=100.0,
        atr_value=1.0,
        atr_pct=0.01,
        theoretical_stop_level=98.0,
        theoretical_target_level=104.0,
        theoretical_invalidation_level=98.0,
        stop_distance=2.0,
        target_distance=4.0,
        stop_distance_pct=0.02,
        target_distance_pct=0.04,
        reward_risk=2.0,
        selected_rr_multiplier=2.0,
        volatility_adjustment_factor=1.0,
        sizing_readiness_score=0.8,
        total_pretrade_risk_score=0.5,
        stop_target_readiness_score=0.9,
        stop_target_quality_score=0.9,
        passed_level_filters=True,
        block_reasons=[],
        watchlist_reasons=[],
        warnings=[],
    )
    pool.add(cand)
    df = pool.to_dataframe()
    assert not df.empty
    assert len(df) == 1

    ranked = pool.rank()
    assert len(ranked) == 1

    summary = pool.summarize()
    assert summary["total_level_candidates"] == 1
