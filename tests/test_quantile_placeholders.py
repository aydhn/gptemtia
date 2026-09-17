# -*- coding: utf-8 -*-
"""Unit tests for Quantile Placeholders."""

from advanced_calibration_uncertainty.quantile_placeholders import (
    build_quantile_placeholder_registry,
    summarize_quantile_placeholders,
)


def test_quantile_placeholders():
    df, summary = build_quantile_placeholder_registry()
    assert summary["all_uncalculated"] is True
    assert summary["all_non_signal"] is True
