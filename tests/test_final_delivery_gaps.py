# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_gaps."""

from advanced_final_delivery.final_delivery_gaps import build_final_delivery_gap_registry


def test_build_final_delivery_gap_registry():
    df, summary = build_final_delivery_gap_registry()
    assert len(df) == 0
    assert isinstance(summary, dict)
    assert 'status' in summary
