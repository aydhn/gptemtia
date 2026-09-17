# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Evaluation Placeholders."""

from advanced_ensemble_model_registry.ensemble_evaluation_placeholders import (
    build_ensemble_evaluation_placeholders,
    validate_ensemble_evaluation_placeholders,
    summarize_ensemble_evaluation_placeholders,
)


def test_ensemble_evaluation_placeholders():
    placeholders = build_ensemble_evaluation_placeholders()
    assert len(placeholders) == 4
    assert "ensemble_cv_split_contract" in placeholders
    assert "ensemble_oof_evaluation_contract" in placeholders
    assert validate_ensemble_evaluation_placeholders(placeholders) is True

    summary = summarize_ensemble_evaluation_placeholders(placeholders)
    assert summary["total_evaluation_placeholders"] == 4
    assert summary["all_zero_evaluation"] is True
    assert summary["all_non_signal"] is True
