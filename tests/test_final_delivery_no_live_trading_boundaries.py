# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_no_live_trading_boundaries."""

from advanced_final_delivery.final_delivery_no_live_trading_boundaries import build_final_delivery_no_live_trading_boundary_registry


def test_build_final_delivery_no_live_trading_boundary_registry():
    df, summary = build_final_delivery_no_live_trading_boundary_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
