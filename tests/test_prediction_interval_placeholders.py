# -*- coding: utf-8 -*-
"""Unit tests for Prediction Interval Placeholders."""

from advanced_calibration_uncertainty.prediction_interval_placeholders import (
    build_prediction_interval_placeholder_registry,
    summarize_prediction_interval_placeholders,
)


def test_prediction_interval_placeholders():
    df, summary = build_prediction_interval_placeholder_registry()
    assert summary["all_uncalculated"] is True
    assert summary["all_non_signal"] is True
