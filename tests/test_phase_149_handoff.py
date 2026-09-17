# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Phase 149 Handoff."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.phase_149_handoff import (
    build_phase_149_monte_carlo_robustness_handoff_report,
)


def test_phase_149_handoff():
    prof = get_default_stress_testing_profile()
    df, summary = build_phase_149_monte_carlo_robustness_handoff_report(prof)
    assert not df.empty
    assert summary["phase_149_handoff_ready"] is True
    assert summary["handoff_status"] == "READY_FOR_PHASE_149"
    assert summary["current_phase"] == 148
    assert summary["next_phase"] == 149
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
