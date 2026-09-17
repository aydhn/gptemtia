# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Domain Registry."""

import pytest
from advanced_model_drift_monitoring.model_drift_domain_registry import (
    build_model_drift_domain_registry,
    summarize_model_drift_domains,
)


def test_build_domain_registry():
    df, summary = build_model_drift_domain_registry()
    assert len(df) >= 50
    assert summary["total_domains"] >= 50
    assert summary["all_zero_execution"] is True
    assert summary["all_non_signal"] is True
