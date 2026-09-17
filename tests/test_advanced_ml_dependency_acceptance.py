# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Dependency Acceptance."""

import pytest
from advanced_ml_acceptance.advanced_ml_dependency_acceptance import (
    build_advanced_ml_dependency_acceptance_registry,
    summarize_advanced_ml_dependency_acceptance,
)


def test_dependency_acceptance():
    df, summary = build_advanced_ml_dependency_acceptance_registry()
    assert not df.empty
    assert len(df) >= 10
    assert summary["all_satisfied"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"

    s = summarize_advanced_ml_dependency_acceptance(df)
    assert s["dependency_count"] >= 10
    assert s["all_satisfied"] is True
