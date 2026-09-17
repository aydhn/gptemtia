"""Test suite for Phase 140 Handoff."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.phase_140_handoff import (
    PHASE_140_PREREQUISITES,
    build_phase_140_ensemble_candidate_model_registry_handoff_report,
    summarize_phase_140_handoff,
)


def test_build_phase_140_ensemble_candidate_model_registry_handoff_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_phase_140_ensemble_candidate_model_registry_handoff_report(profile)

    assert len(df) == len(PHASE_140_PREREQUISITES)
    assert summary["source_phase"] == 139
    assert summary["next_phase"] == 140
    assert summary["target_final_phase"] == 160
    assert summary["total_prerequisites"] == len(df)
    assert summary["all_satisfied"] is True
    assert summary["handoff_status"] == "READY_FOR_PHASE_140"
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["non_signal"] is True


def test_summarize_phase_140_handoff():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_phase_140_ensemble_candidate_model_registry_handoff_report(profile)
    summary = summarize_phase_140_handoff(df)

    assert summary["total_prerequisites"] == len(df)
    assert summary["all_satisfied"] is True
    assert summary["handoff_status"] == "READY_FOR_PHASE_140"
    assert summary["non_signal"] is True
