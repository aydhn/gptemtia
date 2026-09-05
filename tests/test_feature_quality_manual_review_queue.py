import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_quality_manual_review_queue import (
    build_feature_quality_manual_review_queue,
    summarize_feature_quality_manual_review_queue,
)


def test_feature_quality_manual_review_queue():
    findings_df = pd.DataFrame([{
        "finding_id": "fqf_1",
        "source_table": "missingness",
        "feature_column": "feat_nan",
        "severity": "quality_critical",
        "issue_description": "Severe NaN ratio",
        "manual_review_required": True,
    }])
    df, summary = build_feature_quality_manual_review_queue(findings_df=findings_df)
    assert not df.empty
    assert summary["total_queued_items"] == 1
    assert summary["critical_items_count"] == 1
    assert summary["manual_review_pending"] is True

    row = df.iloc[0]
    assert row["auto_fix_forbidden"] == True
    assert row["auto_drop_forbidden"] == True
    assert row["production_approval_forbidden"] == True
