# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Report Inventory."""

from advanced_final_hardening.final_report_inventory import (
    build_final_report_inventory_registry,
)


def test_build_final_report_inventory():
    df, summary = build_final_report_inventory_registry()
    assert not df.empty
    assert summary["report_family_count"] >= 1
    assert summary["all_metadata_only"] is True
    assert (df["non_signal"] == True).all()
