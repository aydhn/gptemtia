"""Tests for advanced_feature_quality_drift.feature_quality_drift_health."""

from pathlib import Path
import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_quality_drift_health import (
    HEALTH_CHECK_COMPONENTS,
    build_feature_quality_drift_health_check,
    summarize_feature_quality_drift_health,
)


def test_health_check_components_defined():
    assert len(HEALTH_CHECK_COMPONENTS) >= 7
    targets = [c["target"] for c in HEALTH_CHECK_COMPONENTS]
    assert "advanced_feature_quality_drift" in targets
    assert "advanced_factor_metadata" in targets
    assert "advanced_feature_validation" in targets


def test_build_feature_quality_drift_health_check():
    df, summary = build_feature_quality_drift_health_check(project_root=Path("."))
    assert not df.empty
    assert summary["total_components"] >= 8
    assert summary["healthy_components"] > 0
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False


def test_summarize_feature_quality_drift_health_empty():
    summary = summarize_feature_quality_drift_health(pd.DataFrame())
    assert summary["total_components"] == 0
    assert summary["healthy_components"] == 0
    assert summary["status"] == "diagnostic_pass"
    assert summary["manual_review_required"] is False
