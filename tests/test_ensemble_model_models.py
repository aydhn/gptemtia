# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Dataclasses."""

import pytest
from advanced_ensemble_model_registry.ensemble_model_models import (
    EnsembleModelProfileItem,
    CandidateModelFamilyItem,
    CandidateModelContract,
    CandidateModelInputContract,
    CandidateModelOutputContract,
    CandidateModelEligibilityGate,
    CandidateCompatibilityMatrixItem,
    EnsembleStrategyContract,
    EnsemblePlaceholderItem,
    EnsembleFinding,
    EnsembleReadinessScore,
    EnsembleModelManifest,
    EnsembleManualReviewItem,
)


def test_ensemble_model_profile_item():
    item = EnsembleModelProfileItem(
        profile_name="test_profile",
        description="test desc",
    )
    assert item.current_phase == 140
    assert item.non_signal is True
    assert item.production_ready is False


def test_candidate_model_contract_invariants():
    contract = CandidateModelContract(
        contract_name="test_contract",
        candidate_family="linear_candidate",
        baseline_contract_ref="base_ref",
        dataset_contract_ref="data_ref",
        feature_snapshot_contract_ref="snap_ref",
        experiment_registry_ref="exp_ref",
        gpu_resource_policy_ref="gpu_ref",
        required_no_lookahead_guard_ref="look_ref",
        required_metadata_only_news_guard_ref="news_ref",
        required_source_preservation_guard_ref="src_ref",
        required_validation_dependency_ref="val_ref",
        required_quality_dependency_ref="qual_ref",
    )
    assert contract.real_training_allowed is False
    assert contract.model_fit_allowed is False
    assert contract.model_predict_allowed is False
    assert contract.ensemble_execution_allowed is False
    assert contract.non_signal_required is True


def test_ensemble_readiness_score_bounds():
    score = EnsembleReadinessScore(
        score_name="test_score",
        readiness_score=0.95,
        classification="READY_FOR_PHASE_141_HANDOFF",
        meets_threshold=True,
    )
    assert 0.0 <= score.readiness_score <= 1.0
    assert score.non_signal is True

    with pytest.raises(ValueError):
        EnsembleReadinessScore(
            score_name="bad_score",
            readiness_score=1.5,
            classification="BAD",
            meets_threshold=False,
        )


def test_ensemble_model_manifest():
    manifest = EnsembleModelManifest()
    assert manifest.current_phase == 140
    assert manifest.next_phase == 141
    assert manifest.target_final_phase == 160
    assert manifest.real_training_executed is False
    assert manifest.ensemble_executed is False
    assert manifest.non_signal is True
