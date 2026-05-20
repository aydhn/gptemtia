import pytest
from research_reports.quality_summary import (
    summarize_data_quality,
    summarize_observability_health,
    summarize_security_readiness,
    summarize_orchestration_status,
    build_quality_research_summary
)
from research_reports.research_config import ResearchReportProfile

def test_quality_summaries():
    q1 = summarize_data_quality({}, {"missing_sources": ["a", "b"]})
    assert q1["missing_sources_count"] == 2

    q2 = summarize_observability_health({})
    assert q2["observability_status"] == "ok"

    q3 = summarize_security_readiness({})
    assert q3["security_readiness_label"] == "ready"

    q4 = summarize_orchestration_status({})
    assert q4["orchestration_latest_status"] == "ok"

def test_build_quality_research_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_quality_research_summary({}, {"warnings": ["w1"]}, prof)
    assert res["critical_warning_count"] == 0
    assert "w1" in res["warnings"]
