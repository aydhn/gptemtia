"""Test suite for Phase 139 GPU Training Governance Manifest."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_manifest import (
    build_gpu_training_governance_manifest,
    create_gpu_training_governance_manifest,
    summarize_gpu_training_governance_manifest,
)


def test_build_gpu_training_governance_manifest():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_governance_manifest(profile)

    assert len(df) == 1
    assert summary["current_phase"] == 139
    assert summary["next_phase"] == 140
    assert summary["target_final_phase"] == 160
    assert summary["dry_run"] is True
    assert summary["real_training_executed"] is False
    assert summary["model_fit_executed"] is False
    assert summary["model_predict_executed"] is False
    assert summary["target_label_generated"] is False
    assert summary["artifact_persisted"] is False
    assert summary["model_registry_written"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["non_signal"] is True


def test_create_gpu_training_governance_manifest():
    m = create_gpu_training_governance_manifest()
    assert m.current_phase == 139
    assert m.next_phase == 140
    assert m.target_final_phase == 160
    assert m.real_training_executed is False
    assert m.non_signal is True
