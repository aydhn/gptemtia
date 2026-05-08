from sizing.sizing_pool import SizingCandidatePool
from sizing.sizing_candidate import SizingCandidate
import pandas as pd


def test_sizing_candidate_pool():
    pool = SizingCandidatePool()
    c1 = SizingCandidate(
        symbol="GC=F",
        timeframe="1d",
        timestamp="2023-01-01",
        sizing_id="s1",
        source_risk_id="r1",
        source_rule_condition_id="",
        strategy_family="trend",
        condition_label="",
        directional_bias="long",
        asset_class="metals",
        sizing_label="sizing_approved_candidate",
        sizing_method="atr_based_theoretical",
        sizing_severity="low",
        theoretical_account_equity=10000.0,
        theoretical_risk_amount=100.0,
        capped_theoretical_risk_amount=100.0,
        latest_close=100.0,
        atr_value=2.0,
        atr_pct=0.02,
        volatility_adjustment_factor=1.0,
        risk_adjustment_factor=1.0,
        combined_adjustment_factor=1.0,
        theoretical_units=50.0,
        adjusted_theoretical_units=50.0,
        theoretical_notional=5000.0,
        adjusted_theoretical_notional=5000.0,
        total_pretrade_risk_score=0.1,
        risk_readiness_score=0.9,
        sizing_readiness_score=0.9,
        sizing_quality_score=1.0,
        report_builder = ReportBuilder()ed_sizing_filters=True,
        block_reasons=[],
        watchlist_reasons=[],
        warnings=[],
    )
    pool.add(c1)

    df = pool.to_dataframe()
    assert not df.empty
    assert len(df) == 1

    # from dataframe
    pool2 = SizingCandidatePool.from_dataframe(df)
    assert len(pool2.candidates) == 1
    assert pool2.candidates[0].sizing_id == "s1"

    summary = pool.summarize()
    assert summary["total_sizing_candidates"] == 1
    assert summary["report_builder = ReportBuilder()ed_sizing_candidates"] == 1
