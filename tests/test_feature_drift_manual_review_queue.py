"""Tests for advanced_feature_quality_drift.feature_drift_manual_review_queue."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_drift_manual_review_queue import (
    build_feature_drift_manual_review_queue,
    summarize_feature_drift_manual_review_queue,
)
from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
)


def test_build_feature_drift_manual_review_queue_empty():
    df, summary = build_feature_drift_manual_review_queue()
    assert not df.empty
    assert df.iloc[0]["queue_id"] == "dmr_nominal_empty"
    assert df.iloc[0]["trade_signal_generation_forbidden"] == True
    assert df.iloc[0]["non_signal"] == True
    assert summary["total_queued_items"] == 0
    assert summary["status"] == "diagnostic_pass"
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124


def test_build_feature_drift_manual_review_queue_with_findings():
    findings_data = [
        {
            "finding_id": "find_1",
            "source_table": "features_daily",
            "feature_column": "feat_rsi",
            "severity": "drift_high",
            "drift_description": "PSI drift above threshold",
            "manual_review_required": True,
        },
        {
            "finding_id": "find_2",
            "source_table": "features_daily",
            "feature_column": "feat_vol",
            "severity": "drift_low",
            "drift_description": "Minor drift",
            "manual_review_required": False,
        },
        {
            "finding_id": "find_3",
            "source_table": "features_daily",
            "feature_column": "feat_spread",
            "severity": "drift_critical",
            "drift_description": "KS test statistic high",
            "manual_review_required": True,
        },
    ]
    findings_df = pd.DataFrame(findings_data)

    df, summary = build_feature_drift_manual_review_queue(drift_findings_df=findings_df)
    assert len(df) == 2
    assert summary["total_queued_items"] == 2
    assert summary["critical_drift_items"] == 1
    assert summary["high_drift_items"] == 1
    assert summary["status"] == "diagnostic_fail"
    assert summary["manual_review_pending"] is True
    assert all(df["trade_signal_generation_forbidden"])
    assert all(df["non_signal"])


def test_summarize_feature_drift_manual_review_queue_empty_df():
    summary = summarize_feature_drift_manual_review_queue(pd.DataFrame())
    assert summary["total_queued_items"] == 0
    assert summary["critical_drift_items"] == 0
    assert summary["status"] == "diagnostic_pass"
    assert summary["manual_review_pending"] is False
