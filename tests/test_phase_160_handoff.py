# -*- coding: utf-8 -*-
"""Unit tests for Phase 160 Handoff."""

from advanced_final_hardening.phase_160_handoff import (
    build_phase_160_full_advanced_bot_final_delivery_handoff_report,
)


def test_build_phase_160_handoff():
    df, summary = build_phase_160_full_advanced_bot_final_delivery_handoff_report()
    assert not df.empty
    assert summary["current_phase"] == 159
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 160
    assert summary["phase_160_handoff_ready"] is True
    assert summary["all_satisfied"] is True
    assert (df["satisfied"] == True).all()
