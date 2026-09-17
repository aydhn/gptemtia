# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Profile Registry."""

import pytest
from advanced_model_drift_monitoring.model_drift_profile_registry import (
    build_model_drift_profile_registry,
    summarize_model_drift_profiles,
)


def test_build_profile_registry():
    df, summary = build_model_drift_profile_registry()
    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["all_non_executing"] is True
    assert summary["all_zero_calculation"] is True
    assert "balanced_local_model_drift_contracts" in summary["profiles"]
