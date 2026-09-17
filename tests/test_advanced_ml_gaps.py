# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Gap Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_gaps import (
    build_advanced_ml_gap_registry,
    summarize_advanced_ml_gaps,
)


def test_gap_registry():
    df, summary = build_advanced_ml_gap_registry()
    assert not df.empty
    assert summary["total_gaps"] >= 1
    assert summary["status"] == "TRACKED"

    s = summarize_advanced_ml_gaps(df)
    assert s["gap_count"] >= 1
