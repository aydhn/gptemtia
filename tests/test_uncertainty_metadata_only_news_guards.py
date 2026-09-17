# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Metadata-Only News Guards."""

from advanced_calibration_uncertainty.uncertainty_metadata_only_news_guards import (
    build_uncertainty_metadata_only_news_guard_registry,
    summarize_uncertainty_metadata_only_news_guards,
)


def test_uncertainty_metadata_only_news_guards():
    df, summary = build_uncertainty_metadata_only_news_guard_registry()
    assert summary["all_active"] is True
    assert summary["all_blocking"] is True
