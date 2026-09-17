# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_component_registry."""

from advanced_final_delivery.final_delivery_component_registry import build_final_delivery_component_registry


def test_build_final_delivery_component_registry():
    df, summary = build_final_delivery_component_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
