# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 -> Phase 141 Handoff."""

from advanced_ensemble_model_registry.phase_141_handoff import (
    build_phase_141_handoff_report,
    validate_phase_141_handoff_report,
    summarize_phase_141_handoff_report,
)


def test_phase_141_handoff():
    report = build_phase_141_handoff_report()
    assert report["current_phase"] == 140
    assert report["next_phase"] == 141
    assert report["target_final_phase"] == 160
    assert report["handoff_status"] == "READY_FOR_PHASE_141"
    assert report["phase_141_prerequisites_met"] is True
    assert report["non_signal"] is True
    assert validate_phase_141_handoff_report(report) is True

    summary = summarize_phase_141_handoff_report(report)
    assert summary["is_valid"] is True
