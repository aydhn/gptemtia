# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_backtest_block_summary."""

from advanced_final_delivery.final_delivery_backtest_block_summary import build_final_delivery_backtest_block_summary_registry


def test_build_final_delivery_backtest_block_summary_registry():
    df, summary = build_final_delivery_backtest_block_summary_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
