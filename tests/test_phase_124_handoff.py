"""Tests for advanced_feature_quality_drift.phase_124_handoff."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.phase_124_handoff import (
    HANDOFF_ITEMS,
    build_phase_124_feature_store_integration_handoff_report,
    summarize_phase_124_handoff,
)


def test_handoff_items_count():
    assert len(HANDOFF_ITEMS) == 11
    item_ids = [item["item_id"] for item in HANDOFF_ITEMS]
    assert "item_feature_quality_manifest" in item_ids
    assert "item_factor_quality_manifest" in item_ids
    assert "item_validation_aware_metadata" in item_ids
    assert "item_quality_score_storage" in item_ids
    assert "item_drift_score_storage" in item_ids
    assert "item_manual_review_blocker_storage" in item_ids
    assert "item_namespace_schema_storage" in item_ids
    assert "item_source_preservation" in item_ids
    assert "item_no_auto_overwrite" in item_ids
    assert "item_non_signal_metadata" in item_ids
    assert "item_phase_125_acceptance_prep" in item_ids


def test_build_phase_124_feature_store_integration_handoff_report():
    df, summary = build_phase_124_feature_store_integration_handoff_report()
    assert not df.empty
    assert len(df) == 11
    assert summary["total_items"] == 11
    assert summary["ready_items"] == 11
    assert summary["handoff_status"] == "READY"
    assert summary["source_phase"] == 123
    assert summary["next_phase"] == 124
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
    assert all(df["source_phase"] == 123)
    assert all(df["next_phase"] == 124)
    assert all(df["target_final_phase"] == 160)
    assert all(df["non_signal"])


def test_summarize_phase_124_handoff_empty():
    summary = summarize_phase_124_handoff(pd.DataFrame())
    assert summary["total_items"] == 0
    assert summary["ready_items"] == 0
    assert summary["handoff_status"] == "BLOCKED"
    assert summary["source_phase"] == 123
    assert summary["next_phase"] == 124
    assert summary["target_final_phase"] == 160
