# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Test Inventory."""

from advanced_final_hardening.final_test_inventory import (
    build_final_test_inventory_registry,
)


def test_build_final_test_inventory():
    df, summary = build_final_test_inventory_registry()
    assert not df.empty
    assert summary["test_count"] >= 1
    assert summary["all_metadata_only"] is True
    assert (df["non_signal"] == True).all()
