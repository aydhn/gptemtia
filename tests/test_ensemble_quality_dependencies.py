# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Quality Dependencies."""

from advanced_ensemble_model_registry.ensemble_quality_dependencies import (
    build_ensemble_quality_dependencies,
    validate_ensemble_quality_dependencies,
    summarize_ensemble_quality_dependencies,
)


def test_ensemble_quality_dependencies():
    deps = build_ensemble_quality_dependencies()
    assert len(deps) == 4
    assert "missingness_quality_dependency" in deps
    assert "drift_quality_dependency" in deps
    assert validate_ensemble_quality_dependencies(deps) is True

    summary = summarize_ensemble_quality_dependencies(deps)
    assert summary["total_dependencies"] == 4
    assert summary["all_enforced"] is True
    assert summary["all_non_signal"] is True
