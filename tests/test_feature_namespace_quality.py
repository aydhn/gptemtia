import pytest
from advanced_feature_quality_drift.feature_namespace_quality import (
    build_feature_namespace_quality_report,
    summarize_feature_namespace_quality,
    validate_feature_namespace_quality,
)


def test_validate_feature_namespace_quality():
    cols = [
        "feat_rsi_14",
        "target_return_5d",  # forbidden token 'target'
        "forward_pe",        # forbidden token 'forward'
        "FEAT_RSI_14",       # case-insensitive collision
    ]
    res = validate_feature_namespace_quality(cols)
    assert len(res) == 4

    rsi_row = res[res["feature_column"] == "feat_rsi_14"].iloc[0]
    assert rsi_row["status"] == "diagnostic_pass"

    target_row = res[res["feature_column"] == "target_return_5d"].iloc[0]
    assert target_row["has_forbidden_token"] == True
    assert target_row["status"] == "diagnostic_fail"
    assert target_row["manual_review_required"] == True

    coll_row = res[res["feature_column"] == "FEAT_RSI_14"].iloc[0]
    assert coll_row["is_duplicate"] == True
    assert coll_row["status"] == "diagnostic_fail"

    summary = summarize_feature_namespace_quality(res)
    assert summary["forbidden_name_count"] == 2
    assert summary["namespace_collision_count"] == 1
    assert summary["manual_review_required"] == True
