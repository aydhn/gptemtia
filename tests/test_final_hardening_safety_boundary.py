# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Safety Boundary."""

from advanced_final_hardening.final_hardening_safety_boundary import (
    build_final_hardening_safety_boundary,
)


def test_build_final_hardening_safety_boundary():
    df, summary = build_final_hardening_safety_boundary()
    assert not df.empty
    assert summary["total_rules"] >= 1
    assert summary["safety_status"] == "SAFETY_BOUNDARY_ENFORCED"
    assert (df["enforced"] == True).all()
