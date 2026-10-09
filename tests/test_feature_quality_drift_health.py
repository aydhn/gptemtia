"""Tests for advanced_feature_quality_drift.feature_quality_drift_health."""

from pathlib import Path

import pandas as pd

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

import importlib


def test_build_feature_quality_drift_health_check_import_error(monkeypatch):
    """Test behavior when modules fail to import."""

    def mock_import_module(name):
        raise ImportError(f"Mocked error for {name}")

    monkeypatch.setattr(importlib, "import_module", mock_import_module)

    df, summary = build_feature_quality_drift_health_check(project_root=Path("."))

    # Check DataFrame
    assert not df.empty

    # Find upstream_package components which should fail
    upstream_components = df[df["category"] == "upstream_package"]
    assert len(upstream_components) > 0

    for _, row in upstream_components.iterrows():
        assert row["healthy"] is False
        assert row["status"] == "diagnostic_fail"
        assert "Import error: Mocked error for" in row["details"]

    # Check Summary
    assert summary["healthy_components"] < summary["total_components"]
    assert summary["unhealthy_components"] >= len(upstream_components)
    assert summary["status"] == "diagnostic_fail"
    assert summary["manual_review_required"] is True
