# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Validation Report."""

from advanced_ensemble_model_registry.ensemble_model_validation import (
    build_ensemble_model_validation_report,
    validate_ensemble_model_validation_report,
    summarize_ensemble_model_validation_report,
)


def test_ensemble_model_validation():
    report = build_ensemble_model_validation_report()
    assert report["validation_status"] == "VALID"
    assert report["phase"] == 140
    assert report["target_final_phase"] == 160
    assert report["invariants_satisfied"] is True
    assert report["zero_execution_verified"] is True
    assert report["non_signal"] is True
    assert validate_ensemble_model_validation_report(report) is True

    summary = summarize_ensemble_model_validation_report(report)
    assert summary["is_valid"] is True
