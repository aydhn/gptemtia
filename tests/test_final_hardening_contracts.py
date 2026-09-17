# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Contracts."""

from advanced_final_hardening.final_hardening_contracts import (
    build_final_hardening_contract_registry,
)


def test_build_final_hardening_contracts():
    df, summary = build_final_hardening_contract_registry()
    assert not df.empty
    assert summary["contract_count"] >= 1
    assert summary["all_execution_blocked"] is True
    assert (df["live_trading_allowed"] == False).all()
    assert (df["system_execution_allowed"] == False).all()
