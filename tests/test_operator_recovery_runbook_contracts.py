# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Operator Recovery Runbook Contracts."""

from advanced_final_hardening.operator_recovery_runbook_contracts import (
    build_operator_recovery_runbook_contract_registry,
)


def test_build_operator_recovery_runbook():
    df, summary = build_operator_recovery_runbook_contract_registry()
    assert not df.empty
    assert summary["procedure_count"] >= 1
    assert summary["all_non_destructive"] is True
    assert (df["destructive"] == False).all()
