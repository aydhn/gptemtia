# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Readiness Scoring."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_readiness_scoring import (
    build_backtest_readiness_score_report,
    calculate_backtest_readiness_score,
)
import pandas as pd


def test_build_readiness_score_report():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_readiness_score_report(prof)
    assert not df.empty
    assert summary["readiness_score"] >= 0.50
    assert summary["meets_threshold"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["non_signal"] is True


def test_calculate_readiness_score_range():
    prof = get_default_realistic_backtest_profile()
    score = calculate_backtest_readiness_score(pd.DataFrame(), prof)
    assert 0.50 <= score.score <= 1.0
    assert score.production_ready is False
    assert score.broker_ready is False
