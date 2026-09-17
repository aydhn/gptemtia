# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Operator Startup Runbook Contracts."""

from advanced_final_hardening.operator_startup_runbook_contracts import (
    build_operator_startup_runbook_contract_registry,
)


def test_build_operator_startup_runbook():
    df, summary = build_operator_startup_runbook_contract_registry()
    assert not df.empty
    assert summary["step_count"] >= 1
    assert summary["no_bot_execution"] is True
    assert (df["requires_manual_inspection"] == True).all()
