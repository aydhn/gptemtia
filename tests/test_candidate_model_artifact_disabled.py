# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Artifact Persistence Disabled Report."""

from advanced_ensemble_model_registry.candidate_model_artifact_disabled import (
    build_candidate_model_artifact_disabled_report,
    validate_candidate_model_artifact_disabled_report,
    summarize_candidate_model_artifact_disabled_report,
)


def test_candidate_model_artifact_disabled():
    report = build_candidate_model_artifact_disabled_report()
    assert report["artifact_persistence_executed"] is False
    assert report["pickle_files_written"] == 0
    assert report["joblib_dumps_written"] == 0
    assert report["pytorch_weights_written"] == 0
    assert report["model_binary_bytes_persisted"] == 0
    assert report["non_signal"] is True
    assert validate_candidate_model_artifact_disabled_report(report) is True

    summary = summarize_candidate_model_artifact_disabled_report(report)
    assert summary["artifact_persistence_disabled"] is True
