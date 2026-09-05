"""Tests for advanced_feature_quality_drift.feature_quality_drift_manifest."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_quality_drift_manifest import (
    create_feature_quality_drift_manifest,
    build_feature_quality_drift_manifest,
    summarize_feature_quality_drift_manifest,
)


def test_create_feature_quality_drift_manifest():
    m = create_feature_quality_drift_manifest(
        manifest_id="test_manifest_1",
        matrix_or_factor_name="matrix_a",
        source_phase_refs=[116, 117],
        feature_count=10,
    )
    assert m["manifest_id"] == "test_manifest_1"
    assert m["matrix_or_factor_name"] == "matrix_a"
    assert m["source_phase_refs"] == "116,117"
    assert m["feature_count"] == 10
    assert m["factor_family_count"] == 10
    assert m["non_signal"] is True
    assert m["official_approval"] is False
    assert m["production_ready"] is False
    assert m["source_preserved"] is True
    assert m["auto_fix_allowed"] is False
    assert m["auto_drop_allowed"] is False


def test_build_feature_quality_drift_manifest_default():
    df, summary = build_feature_quality_drift_manifest()
    assert not df.empty
    assert len(df) == 3
    assert summary["total_matrices"] == 3
    assert summary["total_features"] == 24 + 32 + 56
    assert summary["all_source_preserved"] is True
    assert summary["all_non_signal"] is True
    assert summary["status"] == "diagnostic_pass"
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124


def test_summarize_feature_quality_drift_manifest_empty():
    summary = summarize_feature_quality_drift_manifest(pd.DataFrame())
    assert summary["total_matrices"] == 0
    assert summary["total_features"] == 0
    assert summary["total_manual_reviews"] == 0
    assert summary["all_source_preserved"] is True
    assert summary["all_non_signal"] is True
