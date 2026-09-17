# -*- coding: utf-8 -*-
"""Unit tests for Calibration Metadata-Only News Guards."""

from advanced_calibration_uncertainty.calibration_metadata_only_news_guards import (
    build_calibration_metadata_only_news_guard_registry,
    summarize_calibration_metadata_only_news_guards,
)


def test_calibration_metadata_only_news_guards():
    df, summary = build_calibration_metadata_only_news_guard_registry()
    assert summary["all_active"] is True
    assert summary["all_blocking"] is True
