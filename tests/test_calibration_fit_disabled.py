# -*- coding: utf-8 -*-
"""Unit tests for Calibration Fit Disabled Guarantees."""

from advanced_calibration_uncertainty.calibration_fit_disabled import (
    build_calibration_fit_disabled_report,
    summarize_calibration_fit_disabled,
)


def test_calibration_fit_disabled():
    df, summary = build_calibration_fit_disabled_report()
    assert summary["all_fit_disabled"] is True
    assert summary["all_non_signal"] is True
