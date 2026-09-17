# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Profile Registry."""

from advanced_final_hardening.final_hardening_profile_registry import (
    build_final_hardening_profile_registry,
)


def test_build_profile_registry():
    df, summary = build_final_hardening_profile_registry()
    assert not df.empty
    assert len(df) == 3
    assert summary["profile_count"] == 3
    assert summary["all_non_production"] is True
    assert summary["all_no_live_trading"] is True
    assert (df["allow_live_trading"] == False).all()
    assert (df["current_phase"] == 159).all()
    assert (df["target_final_phase"] == 160).all()
