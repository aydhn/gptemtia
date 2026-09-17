# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Non-Production Boundaries."""

import pytest
from advanced_ml_acceptance.advanced_ml_non_production_boundaries import (
    build_advanced_ml_non_production_boundary_registry,
    summarize_advanced_ml_non_production_boundaries,
)


def test_non_production_boundaries():
    df, summary = build_advanced_ml_non_production_boundary_registry()
    assert not df.empty
    assert len(df) >= 6
    assert summary["all_active"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "ENFORCED"

    s = summarize_advanced_ml_non_production_boundaries(df)
    assert s["boundary_count"] >= 6
    assert s["all_active"] is True
