"""Tests for Phase 121 Handoff Contract and Readiness."""

from advanced_feature_fusion.phase_121_handoff import (
    build_phase_121_handoff_manifest,
    validate_phase_121_handoff_readiness,
)


def test_phase_121_handoff_manifest():
    manifest = build_phase_121_handoff_manifest()
    assert manifest["current_phase"] == 120
    assert manifest["next_phase"] == 121
    assert manifest["target_final_phase"] == 160
    assert manifest["handoff_status"] == "READY"
    assert manifest["safety_invariants"]["zero_trade_signals"] is True
    assert manifest["safety_invariants"]["metadata_only_news"] is True
    assert manifest["safety_invariants"]["no_lookahead_backward_join"] is True
    assert manifest["safety_invariants"]["no_negative_shift"] is True
    assert len(manifest["checklist"]) >= 7


def test_phase_121_handoff_readiness():
    assert validate_phase_121_handoff_readiness() is True
