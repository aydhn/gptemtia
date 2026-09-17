"""Test suite for Phase 137 Advanced ML Dataset Data Models."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_models import (
    AdvancedMlDatasetProfileItem,
    MlDatasetContract,
    MlDatasetSourceCatalogItem,
    MlDatasetSchemaItem,
    MlDatasetSplitPolicy,
    MlDatasetGuardItem,
    MlFeatureSnapshotContract,
    MlExperimentRegistryItem,
    MlExperimentTemplate,
    MlExperimentPermission,
    MlDatasetFinding,
    MlDatasetReadinessScore,
    AdvancedMlDatasetManifest,
    MlDatasetManualReviewItem,
)


def test_models_default_safety_invariants():
    profile_item = AdvancedMlDatasetProfileItem(profile_name="test_p", description="test")
    assert profile_item.current_phase == 137
    assert profile_item.next_phase == 138
    assert profile_item.non_signal is True
    assert profile_item.dataset_materialized is False
    assert profile_item.model_training_executed is False

    contract = MlDatasetContract(contract_name="test_c", dataset_family="test_f")
    assert contract.target_label_generation_allowed is False
    assert contract.dataset_materialization_allowed is False
    assert contract.model_training_allowed is False
    assert contract.prediction_allowed is False

    snapshot = MlFeatureSnapshotContract(contract_name="test_s", dataset_family="test_f")
    assert snapshot.materialized is False
    assert snapshot.production_ready is False

    manifest = AdvancedMlDatasetManifest(manifest_name="test_m")
    assert manifest.current_phase == 137
    assert manifest.next_phase == 138
    assert manifest.dataset_materialized is False
    assert manifest.feature_snapshot_materialized is False
    assert manifest.model_training_executed is False
    assert manifest.model_predict_executed is False
    assert manifest.non_signal is True
