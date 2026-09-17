# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Dependency Freeze Contracts."""

from advanced_final_hardening.final_dependency_freeze_contracts import (
    build_final_dependency_freeze_contract_registry,
)


def test_build_final_dependency_freeze():
    df, summary = build_final_dependency_freeze_contract_registry()
    assert not df.empty
    assert summary["freeze_item_count"] >= 1
    assert summary["all_frozen"] is True
    assert (df["frozen"] == True).all()
