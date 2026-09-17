# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_scope_registry."""

from advanced_final_delivery.final_delivery_scope_registry import build_final_delivery_scope_registry


def test_build_final_delivery_scope_registry():
    df, summary = build_final_delivery_scope_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
