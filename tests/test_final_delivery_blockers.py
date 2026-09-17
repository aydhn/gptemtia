# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_blockers."""

from advanced_final_delivery.final_delivery_blockers import build_final_delivery_blocker_registry


def test_build_final_delivery_blocker_registry():
    df, summary = build_final_delivery_blocker_registry()
    assert len(df) == 0
    assert isinstance(summary, dict)
    assert 'status' in summary
