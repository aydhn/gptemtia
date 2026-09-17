# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Manifest."""

from advanced_final_hardening.release_candidate_manifest import (
    build_release_candidate_manifest,
)


def test_build_release_candidate_manifest():
    df, summary = build_release_candidate_manifest()
    assert not df.empty
    assert summary["current_phase"] == 159
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 160
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["live_trading_ready"] is False
    assert summary["system_executed"] is False
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert (df["live_trading_ready"] == False).all()
