import pytest
from research_reports.validation_summary import (
    summarize_walk_forward,
    summarize_parameter_sensitivity,
    summarize_overfitting_risk,
    summarize_robustness,
    build_validation_research_summary
)
from research_reports.research_config import ResearchReportProfile

def test_validation_summaries():
    v1 = summarize_walk_forward({})
    assert v1["split_count"] == 0

    v2 = summarize_parameter_sensitivity({})
    assert v2["stability_score"] == 0.0

    v3 = summarize_overfitting_risk({})
    assert "overfitting_risk_score" in v3

    v4 = summarize_robustness({})
    assert v4["validation_status"] == "unknown"

def test_build_validation_research_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_validation_research_summary({}, prof)
    assert "warnings" in res
