# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Operator No-Go Protocols."""

from advanced_final_hardening.operator_no_go_protocols import (
    build_operator_no_go_protocol_registry,
)


def test_build_operator_no_go_protocols():
    df, summary = build_operator_no_go_protocol_registry()
    assert not df.empty
    assert summary["rule_count"] >= 1
    assert summary["all_enforced"] is True
    assert (df["enforced"] == True).all()
