# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Operator Safe Usage Protocols."""

from advanced_final_hardening.operator_safe_usage_protocols import (
    build_operator_safe_usage_protocol_registry,
)


def test_build_operator_safe_usage_protocols():
    df, summary = build_operator_safe_usage_protocol_registry()
    assert not df.empty
    assert summary["rule_count"] >= 1
    assert summary["all_enforced"] is True
    assert (df["enforced"] == True).all()
