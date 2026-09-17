# -*- coding: utf-8 -*-
"""Unit tests for Calibration Execution Disabled Guarantees."""

from advanced_calibration_uncertainty.calibration_execution_disabled import (
    build_calibration_execution_disabled_report,
    summarize_calibration_execution_disabled,
)


def test_calibration_execution_disabled():
    df, summary = build_calibration_execution_disabled_report()
    assert summary["all_disabled"] is True
    assert summary["all_enforced"] is True
