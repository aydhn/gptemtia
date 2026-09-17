# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_warnings."""

from advanced_final_delivery.final_delivery_warnings import build_final_delivery_warning_registry


def test_build_final_delivery_warning_registry():
    df, summary = build_final_delivery_warning_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
