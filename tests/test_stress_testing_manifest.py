# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stress Testing Manifest."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_manifest import (
    build_stress_testing_manifest,
)


def test_manifest():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_manifest(prof)
    assert not df.empty
    assert summary["current_phase"] == 148
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 149
    assert bool(df.iloc[0]["stress_test_executed"]) is False
    assert bool(df.iloc[0]["scenario_simulation_executed"]) is False
    assert summary["phase_149_handoff_ready"] is True
    assert summary["non_signal"] is True
