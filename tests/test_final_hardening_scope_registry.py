# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Scope Registry."""

from advanced_final_hardening.final_hardening_scope_registry import (
    build_final_hardening_scope_registry,
)


def test_build_scope_registry():
    df, summary = build_final_hardening_scope_registry()
    assert not df.empty
    assert summary["scope_item_count"] >= 1
    assert summary["status"] == "final_hardening_contract_ready"
    assert (df["local_only"] == True).all()
