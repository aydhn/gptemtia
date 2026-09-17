# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_forbidden_column_policies."""

from advanced_final_delivery.final_delivery_forbidden_column_policies import build_final_delivery_forbidden_column_policy_registry


def test_build_final_delivery_forbidden_column_policy_registry():
    df, summary = build_final_delivery_forbidden_column_policy_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
