"""Tests for advanced_feature_quality_drift.feature_quality_drift_safety_boundary."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_quality_drift_safety_boundary import (
    NO_GO_CONDITIONS,
    SAFE_GO_CONDITIONS,
    build_feature_quality_drift_no_go_conditions,
    build_feature_quality_drift_safe_go_conditions,
    build_feature_quality_drift_safety_boundary,
    summarize_feature_quality_drift_safety_boundary,
)


def test_no_go_conditions_count():
    assert len(NO_GO_CONDITIONS) == 13
    rule_ids = [r["rule_id"] for r in NO_GO_CONDITIONS]
    assert "no_live_trading" in rule_ids
    assert "no_quality_drift_as_signal" in rule_ids
    assert "no_auto_imputation" in rule_ids
    assert "no_auto_feature_drop" in rule_ids
    assert "no_production_readiness_claims" in rule_ids


def test_safe_go_conditions_count():
    assert len(SAFE_GO_CONDITIONS) == 7
    principle_ids = [p["principle_id"] for p in SAFE_GO_CONDITIONS]
    assert "safe_local_offline_diagnostics" in principle_ids
    assert "safe_manual_review_queue" in principle_ids
    assert "safe_phase_124_handoff" in principle_ids


def test_build_feature_quality_drift_safety_boundary():
    df, summary = build_feature_quality_drift_safety_boundary()
    assert not df.empty
    assert len(df) == 13 + 7
    assert summary["total_rules"] == 20
    assert summary["no_go_count"] == 13
    assert summary["safe_go_count"] == 7
    assert summary["safety_status"] == "SECURE"
    assert summary["destructive_action_allowed"] is False
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124


def test_summarize_feature_quality_drift_safety_boundary_empty():
    summary = summarize_feature_quality_drift_safety_boundary(pd.DataFrame())
    assert summary["total_rules"] == 0
    assert summary["safety_status"] == "SECURE"
    assert summary["destructive_action_allowed"] is False
