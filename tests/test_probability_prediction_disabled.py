# -*- coding: utf-8 -*-
"""Unit tests for Probability Prediction Disabled Guarantees."""

from advanced_calibration_uncertainty.probability_prediction_disabled import (
    build_probability_prediction_disabled_report,
    summarize_probability_prediction_disabled,
)


def test_probability_prediction_disabled():
    df, summary = build_probability_prediction_disabled_report()
    assert summary["all_prediction_disabled"] is True
    assert summary["all_non_signal"] is True
