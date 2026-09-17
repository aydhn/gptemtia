# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_health."""

from advanced_final_delivery.final_delivery_health import build_final_delivery_health_check


def test_build_final_delivery_health_check():
    df, summary = build_final_delivery_health_check()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
