# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Pipeline."""

from advanced_realistic_backtest.realistic_backtest_pipeline import (
    RealisticBacktestPipeline,
)


def test_pipeline_execution():
    pipeline = RealisticBacktestPipeline()
    status_df, summary = pipeline.build_realistic_backtest_status(save=False)
    assert not status_df.empty
    assert len(status_df) >= 10
    assert summary["phase"] == 146
    assert summary["next_phase"] == 147
    assert summary["readiness_score"] >= 0.50
    assert summary["live_trading"] is False
    assert summary["broker_execution"] is False
    assert summary["non_signal"] is True
