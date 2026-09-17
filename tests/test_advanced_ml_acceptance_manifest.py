# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Acceptance Manifest."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_manifest import (
    build_advanced_ml_acceptance_manifest,
    create_advanced_ml_acceptance_manifest,
    summarize_advanced_ml_acceptance_manifest,
)


def test_manifest_creation():
    manifest = create_advanced_ml_acceptance_manifest()
    assert manifest.current_phase == 145
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 146
    assert manifest.advanced_ml_block_completed is True
    assert manifest.phase_146_handoff_ready is True
    assert manifest.non_signal is True
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.production_approved is False
    assert manifest.broker_ready_approved is False
    assert manifest.live_trading_approved is False
    assert manifest.release_approved is False
    assert manifest.real_audit_log is False
    assert manifest.dataset_materialized is False
    assert manifest.feature_snapshot_materialized is False
    assert manifest.contains_target_or_prediction is False
    assert manifest.contains_trading_recommendation is False
    assert manifest.backtest_executed is False
    assert manifest.model_training_executed is False
    assert manifest.model_predict_executed is False
    assert manifest.artifact_persisted is False
    assert manifest.model_registry_written is False


def test_build_manifest_dataframe():
    df, summary = build_advanced_ml_acceptance_manifest()
    assert not df.empty
    assert summary["current_phase"] == 145
    assert summary["advanced_ml_block_completed"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["non_signal"] is True

    s = summarize_advanced_ml_acceptance_manifest(df)
    assert s["advanced_ml_block_completed"] is True
    assert s["production_ready"] is False
    assert s["phase_146_handoff_ready"] is True
