"""Test suite for Phase 138 Baseline ML Model Dataclasses."""

import pytest
from advanced_baseline_ml_models.baseline_ml_model_models import (
    BaselineMlModelProfileItem,
    BaselineModelFamilyItem,
    BaselineModelContract,
    BaselineModelInputContract,
    BaselineModelOutputContract,
    DryRunHarnessContract,
    DryRunTrainerStub,
    BaselineModelFinding,
    BaselineModelReadinessScore,
    BaselineModelManualReviewItem,
    BaselineMlModelManifest,
)


def test_baseline_model_contract():
    contract = BaselineModelContract(
        contract_name="contract_logistic_regression",
        model_family="logistic_regression",
        dataset_contract_ref="ds_1",
        feature_snapshot_contract_ref="fs_1",
        experiment_registry_ref="exp_1",
        runtime_profile_ref="rt_1",
        required_no_lookahead_guard_ref="nlg_1",
        required_metadata_only_news_guard_ref="mon_1",
        required_source_preservation_guard_ref="spg_1",
        required_validation_dependency_ref="vd_1",
        required_quality_dependency_ref="qd_1",
    )
    assert contract.contract_name == "contract_logistic_regression"
    assert contract.real_training_allowed is False
    assert contract.model_fit_allowed is False
    assert contract.model_predict_allowed is False
    assert contract.non_signal_required is True


def test_dry_run_harness_contract():
    harness = DryRunHarnessContract(
        harness_id="harness_linear",
        harness_name="Linear Harness",
        allowed_mode="contract_only",
        simulation_mode="no_op_dry_run",
    )
    assert harness.allowed_mode == "contract_only"
    assert harness.real_training_allowed is False
    assert harness.model_fit_allowed is False
    assert harness.model_predict_allowed is False


def test_dry_run_trainer_stub():
    stub = DryRunTrainerStub(
        stub_id="stub_rf",
        trainer_name="RF Trainer Stub",
        model_family_ref="random_forest",
        harness_contract_ref="harness_rf",
    )
    assert stub.execution_status == "execution_blocked_no_real_training"
    assert stub.is_active_stub is True


def test_readiness_score_validation():
    score = BaselineModelReadinessScore(
        score=1.0,
        score_tier="READY_FOR_LOCAL_DRY_RUN_HARNESS",
        critical_blockers=0,
        total_findings=0,
        classification="READY_FOR_LOCAL_DRY_RUN_HARNESS",
    )
    assert score.score == 1.0

    with pytest.raises(ValueError, match="Readiness score must be between 0.0 and 1.0"):
        BaselineModelReadinessScore(
            score=1.5,
            score_tier="INVALID",
            critical_blockers=0,
            total_findings=0,
            classification="INVALID",
        )


def test_baseline_ml_model_manifest_defaults():
    manifest = BaselineMlModelManifest()
    assert manifest.current_phase == 138
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 139
    assert manifest.real_training_executed is False
    assert manifest.model_fit_executed is False
    assert manifest.model_predict_executed is False
    assert manifest.non_signal is True
