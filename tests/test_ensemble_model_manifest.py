# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Manifest."""

from advanced_ensemble_model_registry.ensemble_model_manifest import (
    build_ensemble_model_manifest,
    validate_ensemble_model_manifest,
    summarize_ensemble_model_manifest,
)


def test_ensemble_model_manifest():
    manifest = build_ensemble_model_manifest()
    assert manifest.current_phase == 140
    assert manifest.next_phase == 141
    assert manifest.target_final_phase == 160
    assert manifest.real_training_executed is False
    assert manifest.model_fit_executed is False
    assert manifest.model_predict_executed is False
    assert manifest.ensemble_executed is False
    assert manifest.voting_executed is False
    assert manifest.blending_executed is False
    assert manifest.stacking_executed is False
    assert manifest.calibration_executed is False
    assert manifest.artifact_persisted is False
    assert manifest.model_registry_written is False
    assert manifest.non_signal is True
    assert validate_ensemble_model_manifest(manifest) is True

    summary = summarize_ensemble_model_manifest(manifest)
    assert summary["is_valid"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
