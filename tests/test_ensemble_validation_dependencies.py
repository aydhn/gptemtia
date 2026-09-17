# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Validation Dependencies."""

from advanced_ensemble_model_registry.ensemble_validation_dependencies import (
    build_ensemble_validation_dependencies,
    validate_ensemble_validation_dependencies,
    summarize_ensemble_validation_dependencies,
)


def test_ensemble_validation_dependencies():
    deps = build_ensemble_validation_dependencies()
    assert len(deps) == 4
    assert "dataset_validation_dependency" in deps
    assert "feature_validation_dependency" in deps
    assert validate_ensemble_validation_dependencies(deps) is True

    summary = summarize_ensemble_validation_dependencies(deps)
    assert summary["total_dependencies"] == 4
    assert summary["all_enforced"] is True
    assert summary["all_non_signal"] is True
