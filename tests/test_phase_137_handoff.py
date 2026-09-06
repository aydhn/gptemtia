"""Test suite for Phase 136 to Phase 137 Handoff."""

import pytest
from advanced_gpu_ml_runtime.phase_137_handoff import (
    build_phase_137_advanced_ml_dataset_experiment_handoff_report,
)


def test_build_phase_137_handoff():
    df, summary = build_phase_137_advanced_ml_dataset_experiment_handoff_report()
    assert not df.empty
    assert summary["source_phase"] == 136
    assert summary["next_phase"] == 137
    assert summary["target_final_phase"] == 160
    assert summary["all_satisfied"] is True
    assert summary["status"] == "READY"
    assert summary["non_signal"] is True
