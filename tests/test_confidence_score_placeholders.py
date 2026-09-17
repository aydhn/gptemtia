# -*- coding: utf-8 -*-
"""Unit tests for Confidence Score Placeholders."""

from advanced_calibration_uncertainty.confidence_score_placeholders import (
    build_confidence_score_placeholder_registry,
    summarize_confidence_score_placeholders,
)


def test_confidence_score_placeholders():
    df, summary = build_confidence_score_placeholder_registry()
    assert summary["all_uncalculated"] is True
    assert summary["all_non_signal"] is True
