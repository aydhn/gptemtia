import pytest
from advanced_feature_validation.feature_validation_report_builder import (
    build_feature_validation_report,
    build_feature_validation_markdown_report,
    build_feature_validation_text_summary,
)


def test_feature_validation_report_builder():
    dummy_pipeline_result = {
        "status": "PASS",
        "scores": {
            "overall_score": 0.96,
            "lookahead_score": 1.0,
            "forbidden_column_score": 1.0,
            "integrity_score": 0.95,
            "numeric_sanity_score": 0.98,
            "completeness_score": 0.90,
            "is_passing": True,
        },
        "findings": [],
        "manifest": {"matrix_name": "test_mat", "total_columns": 5, "total_rows": 20},
    }

    report = build_feature_validation_report(dummy_pipeline_result, profile_name="test_profile")
    assert report["profile_name"] == "test_profile"
    assert report["current_phase"] == 121
    assert "disclaimer" in report

    md = build_feature_validation_markdown_report(report)
    assert "# Phase 121: Feature Validation and No-Lookahead Guard Report" in md
    assert "Overall Quality Score" in md

    txt = build_feature_validation_text_summary(report)
    assert "Phase 121" in txt
