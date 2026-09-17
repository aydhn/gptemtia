# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_safety_boundary."""

from advanced_final_delivery.final_delivery_safety_boundary import build_final_delivery_safety_boundary


def test_build_final_delivery_safety_boundary():
    df, summary = build_final_delivery_safety_boundary()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
