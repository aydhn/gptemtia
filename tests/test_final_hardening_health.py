# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Health."""

from pathlib import Path
from advanced_final_hardening.final_hardening_health import (
    build_final_hardening_health_check,
)


def test_build_final_hardening_health():
    project_root = Path(__file__).resolve().parent.parent
    df, summary = build_final_hardening_health_check(project_root)
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["passed_checks"] == summary["total_checks"]
    assert (df["available"] == True).all()
