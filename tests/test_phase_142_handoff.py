# -*- coding: utf-8 -*-
"""Unit tests for Phase 141 -> Phase 142 Handoff."""

from advanced_calibration_uncertainty.phase_142_handoff import (
    build_phase_142_model_drift_monitoring_handoff_report,
    summarize_phase_142_handoff,
)


def test_phase_142_handoff():
    df, summary = build_phase_142_model_drift_monitoring_handoff_report()
    assert summary["source_phase"] == 141
    assert summary["next_phase"] == 142
    assert summary["target_final_phase"] == 160
    assert summary["handoff_status"] == "READY_FOR_PHASE_142"
    assert summary["all_prerequisites_met"] is True
    assert summary["all_non_signal"] is True
