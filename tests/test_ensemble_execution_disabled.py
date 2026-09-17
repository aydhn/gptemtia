# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Execution Disabled Report."""

from advanced_ensemble_model_registry.ensemble_execution_disabled import (
    build_ensemble_execution_disabled_report,
    validate_ensemble_execution_disabled_report,
    summarize_ensemble_execution_disabled_report,
)


def test_ensemble_execution_disabled():
    report = build_ensemble_execution_disabled_report()
    assert report["ensemble_execution_allowed"] is False
    assert report["voting_executed"] is False
    assert report["blending_executed"] is False
    assert report["stacking_executed"] is False
    assert report["non_signal"] is True
    assert report["dry_run"] is True
    assert validate_ensemble_execution_disabled_report(report) is True

    summary = summarize_ensemble_execution_disabled_report(report)
    assert summary["all_executions_disabled"] is True
