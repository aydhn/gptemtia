# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_operator_handover."""

from advanced_final_delivery.final_delivery_operator_handover import build_final_delivery_operator_handover_registry


def test_build_final_delivery_operator_handover_registry():
    df, summary = build_final_delivery_operator_handover_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
