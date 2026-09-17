# -*- coding: utf-8 -*-
"""Unit tests for Calibration Transform Disabled Guarantees."""

from advanced_calibration_uncertainty.calibration_transform_disabled import (
    build_calibration_transform_disabled_report,
    summarize_calibration_transform_disabled,
)


def test_calibration_transform_disabled():
    df, summary = build_calibration_transform_disabled_report()
    assert summary["all_transform_disabled"] is True
    assert summary["all_non_signal"] is True
