# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Warning Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_warnings import (
    build_advanced_ml_warning_registry,
    summarize_advanced_ml_warnings,
)


def test_warning_registry():
    df, summary = build_advanced_ml_warning_registry()
    assert not df.empty
    assert summary["total_warnings"] >= 5
    assert summary["status"] == "NOTICED"

    s = summarize_advanced_ml_warnings(df)
    assert s["warning_count"] >= 5
