# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Target Label Disabled Report."""

from advanced_ensemble_model_registry.candidate_model_target_label_disabled import (
    build_candidate_model_target_label_disabled_report,
    validate_candidate_model_target_label_disabled_report,
    summarize_candidate_model_target_label_disabled_report,
)


def test_candidate_model_target_label_disabled():
    report = build_candidate_model_target_label_disabled_report()
    assert report["target_label_generation_executed"] is False
    assert report["forward_return_targets_created"] == 0
    assert report["target_columns_added"] == 0
    assert report["non_signal"] is True
    assert validate_candidate_model_target_label_disabled_report(report) is True

    summary = summarize_candidate_model_target_label_disabled_report(report)
    assert summary["target_label_generation_disabled"] is True
