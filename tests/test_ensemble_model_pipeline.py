# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Pipeline."""

from advanced_ensemble_model_registry.ensemble_model_pipeline import (
    run_ensemble_model_pipeline,
    validate_ensemble_model_pipeline_result,
    summarize_ensemble_model_pipeline_result,
)


def test_ensemble_model_pipeline():
    result = run_ensemble_model_pipeline()
    assert result["phase"] == 140
    assert result["next_phase"] == 141
    assert result["target_final_phase"] == 160
    assert result["candidate_contract_count"] == 10
    assert result["ensemble_strategy_count"] == 7
    assert result["health_status"] == "HEALTHY"
    assert result["validation_status"] == "VALID"
    assert result["readiness_score"] >= 0.85
    assert result["non_signal"] is True
    assert result["dry_run"] is True
    assert validate_ensemble_model_pipeline_result(result) is True

    summary = summarize_ensemble_model_pipeline_result(result)
    assert summary["is_valid"] is True
