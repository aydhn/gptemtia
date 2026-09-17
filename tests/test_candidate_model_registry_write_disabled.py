# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Registry Write Disabled Report."""

from advanced_ensemble_model_registry.candidate_model_registry_write_disabled import (
    build_candidate_model_registry_write_disabled_report,
    validate_candidate_model_registry_write_disabled_report,
    summarize_candidate_model_registry_write_disabled_report,
)


def test_candidate_model_registry_write_disabled():
    report = build_candidate_model_registry_write_disabled_report()
    assert report["model_registry_write_executed"] is False
    assert report["external_registry_writes"] == 0
    assert report["mlflow_runs_logged"] == 0
    assert report["non_signal"] is True
    assert validate_candidate_model_registry_write_disabled_report(report) is True

    summary = summarize_candidate_model_registry_write_disabled_report(report)
    assert summary["registry_write_disabled"] is True
