"""Test suite for Phase 137 to Phase 138 Handoff Report."""

import pytest
from advanced_ml_dataset_registry.phase_138_handoff import (
    build_phase_138_baseline_ml_model_contracts_handoff_report,
    summarize_phase_138_handoff,
)


def test_build_phase_138_handoff():
    df, summary = build_phase_138_baseline_ml_model_contracts_handoff_report()
    assert not df.empty
    assert summary["source_phase"] == 137
    assert summary["next_phase"] == 138
    assert summary["target_final_phase"] == 160
    assert summary["all_satisfied"] is True
    assert summary["handoff_status"] == "READY_FOR_PHASE_138"
    assert summary["live_trading_prohibited"] is True
    assert summary["broker_integration_blocked"] is True
    assert summary["non_signal"] is True
