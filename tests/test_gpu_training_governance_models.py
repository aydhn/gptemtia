"""Test suite for Phase 139 GPU Training Governance Data Models."""

import pytest
from advanced_gpu_training_governance.gpu_training_governance_models import (
    GpuTrainingGovernanceProfileItem,
    GpuTrainingResourcePolicy,
    GpuDeviceSelectionPolicy,
    GpuMemoryBudgetPolicy,
    CpuFallbackPolicy,
    TrainingTimeoutPolicy,
    TrainingLoopStubContract,
    GpuTrainingHarnessStub,
    DryRunResourceCheckItem,
    GpuTrainingFinding,
    GpuTrainingReadinessScore,
    GpuTrainingManualReviewItem,
    GpuTrainingGovernanceManifest,
)


def test_gpu_training_resource_policy_defaults():
    policy = GpuTrainingResourcePolicy(
        policy_id="test_res_01",
        policy_name="Test Resource Policy",
        resource_type="gpu",
    )
    assert policy.allowed_mode == "contract_only"
    assert policy.dry_run_required is True
    assert policy.real_training_allowed is False
    assert policy.prediction_allowed is False
    assert policy.artifact_persistence_allowed is False
    assert policy.model_registry_write_allowed is False


def test_gpu_device_selection_policy():
    dev_policy = GpuDeviceSelectionPolicy(
        policy_id="dev_01",
        device_preference="cuda_if_available",
    )
    assert dev_policy.fallback_allowed is True
    assert dev_policy.allow_real_cuda_initialization is False
    assert dev_policy.dry_run_mode is True


def test_gpu_memory_budget_policy():
    mem_policy = GpuMemoryBudgetPolicy(
        policy_id="mem_01",
        max_memory_fraction=0.75,
        reserved_system_mb=2048,
    )
    assert mem_policy.enable_memory_guard is True
    assert mem_policy.dry_run_only is True


def test_cpu_fallback_policy():
    cpu_policy = CpuFallbackPolicy(
        policy_id="cpu_01",
        max_cpu_threads_placeholder=4,
    )
    assert cpu_policy.allow_cpu_fallback is True
    assert cpu_policy.dry_run_only is True


def test_training_timeout_policy():
    timeout_policy = TrainingTimeoutPolicy(
        policy_id="timeout_01",
        max_timeout_seconds=1800,
    )
    assert timeout_policy.terminate_on_timeout is True
    assert timeout_policy.dry_run_only is True


def test_training_loop_stub_contract():
    stub_contract = TrainingLoopStubContract(
        contract_id="loop_01",
        contract_name="Standard Stub Contract",
    )
    assert stub_contract.allowed_execution is False
    assert "fit" in stub_contract.blocked_keywords
    assert "backward" in stub_contract.blocked_keywords
    assert stub_contract.dry_run_only is True


def test_readiness_score_bounds():
    score = GpuTrainingReadinessScore(
        score=0.95,
        classification="PASS",
        meets_threshold=True,
    )
    assert score.score == 0.95
    assert score.current_phase == 139
    assert score.production_ready is False

    with pytest.raises(ValueError):
        GpuTrainingReadinessScore(
            score=1.5,
            classification="FAIL",
            meets_threshold=False,
        )


def test_gpu_training_manifest():
    manifest = GpuTrainingGovernanceManifest(
        manifest_name="phase_139_manifest",
    )
    assert manifest.current_phase == 139
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 140
    assert manifest.dry_run is True
    assert manifest.real_training_executed is False
    assert manifest.model_fit_executed is False
    assert manifest.model_predict_executed is False
    assert manifest.model_inference_executed is False
    assert manifest.artifact_persisted is False
    assert manifest.model_registry_written is False
