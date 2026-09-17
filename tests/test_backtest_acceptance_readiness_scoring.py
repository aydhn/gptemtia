import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_readiness_scoring import (
    classify_backtest_acceptance_readiness_score,
    calculate_backtest_acceptance_readiness_score,
    build_backtest_acceptance_readiness_score_report,
)

def test_classify_readiness_score():
    assert classify_backtest_acceptance_readiness_score(0.10) == "blocked"
    assert classify_backtest_acceptance_readiness_score(0.35) == "incomplete"
    assert classify_backtest_acceptance_readiness_score(0.60) == "contract_ready_with_manual_review"
    assert classify_backtest_acceptance_readiness_score(0.85) == "backtest_acceptance_contract_ready_non_production"
    assert classify_backtest_acceptance_readiness_score(1.00) == "backtest_acceptance_contract_ready_non_production"

    with pytest.raises(ValueError):
        classify_backtest_acceptance_readiness_score(-0.1)

    with pytest.raises(ValueError):
        classify_backtest_acceptance_readiness_score(1.1)

def test_calculate_readiness_score():
    score_clean = calculate_backtest_acceptance_readiness_score(findings_df=None)
    assert score_clean.score == 1.0
    assert score_clean.classification == "backtest_acceptance_contract_ready_non_production"
    assert score_clean.meets_threshold is True
    assert score_clean.production_ready is False
    assert score_clean.broker_ready is False
    assert score_clean.live_trading_ready is False
    assert score_clean.official_approval is False
    assert score_clean.strategy_approved is False
    assert score_clean.performance_guaranteed is False

    # Simulate findings impact
    findings_df = pd.DataFrame([
        {"severity_label": "CRITICAL"},
        {"severity_label": "WARNING"},
    ])
    score_impacted = calculate_backtest_acceptance_readiness_score(findings_df=findings_df)
    assert score_impacted.score < 1.0
    assert score_impacted.score >= 0.0

def test_build_readiness_score_report():
    df, summary = build_backtest_acceptance_readiness_score_report()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == 1
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["strategy_approved"] is False
    assert summary["non_signal"] is True
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
