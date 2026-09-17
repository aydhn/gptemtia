# -*- coding: utf-8 -*-
"""Unit tests for Conformal Prediction Placeholders."""

from advanced_calibration_uncertainty.conformal_prediction_placeholders import (
    build_conformal_prediction_placeholder_registry,
    summarize_conformal_prediction_placeholders,
)


def test_conformal_prediction_placeholders():
    df, summary = build_conformal_prediction_placeholder_registry()
    assert summary["all_unexecuted"] is True
    assert summary["all_non_signal"] is True
