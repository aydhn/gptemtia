# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Disabled Execution Inventory."""

from advanced_final_hardening.final_disabled_execution_inventory import (
    build_final_disabled_execution_inventory_registry,
)


def test_build_final_disabled_execution_inventory():
    df, summary = build_final_disabled_execution_inventory_registry()
    assert not df.empty
    assert summary["disabled_action_count"] >= 1
    assert summary["all_disabled"] is True
    assert (df["is_disabled"] == True).all()
