import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_quality_findings import (
    build_feature_quality_findings_registry,
    summarize_feature_quality_findings,
)


def test_feature_quality_findings_nominal():
    df, summary = build_feature_quality_findings_registry()
    assert not df.empty
    assert summary["critical_findings"] == 0
    assert summary["status"] == "diagnostic_pass"

    for _, row in df.iterrows():
        assert row["non_signal"] is True
        assert row["destructive_action_allowed"] is False


def test_feature_quality_findings_with_violations():
    diag_tables = {
        "missingness": pd.DataFrame([{
            "column": "feat_bad",
            "severity": "quality_critical",
            "notes": "100% missing",
            "manual_review_required": True,
        }])
    }
    df, summary = build_feature_quality_findings_registry(diagnostic_tables=diag_tables)
    assert summary["critical_findings"] == 1
    assert summary["status"] == "diagnostic_fail"
    assert summary["manual_review_required"] is True
