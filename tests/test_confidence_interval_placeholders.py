# -*- coding: utf-8 -*-
"""Unit tests for Confidence Interval Placeholders."""

from advanced_calibration_uncertainty.confidence_interval_placeholders import (
    build_confidence_interval_placeholder_registry,
    summarize_confidence_interval_placeholders,
)


def test_confidence_interval_placeholders():
    df, summary = build_confidence_interval_placeholder_registry()
    assert summary["all_uncalculated"] is True
    assert summary["all_non_signal"] is True
