# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Safety Boundary Inventory."""

from advanced_final_hardening.final_safety_boundary_inventory import (
    build_final_safety_boundary_inventory_registry,
)


def test_build_final_safety_boundary_inventory():
    df, summary = build_final_safety_boundary_inventory_registry()
    assert not df.empty
    assert summary["boundary_count"] >= 1
    assert summary["all_enforced"] is True
    assert (df["enforced"] == True).all()
