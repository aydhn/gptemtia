import pytest
from research_reports.paper_summary import (
    summarize_paper_orders,
    summarize_paper_positions,
    summarize_paper_portfolio,
    summarize_paper_quality,
    build_paper_research_summary
)
from research_reports.research_config import ResearchReportProfile

def test_paper_summaries():
    p1 = summarize_paper_orders({})
    assert p1["virtual_order_count"] == 0

    p2 = summarize_paper_positions({})
    assert p2["virtual_open_positions"] == 0

    p3 = summarize_paper_portfolio({})
    assert p3["virtual_equity"] == 0.0

    p4 = summarize_paper_quality({})
    assert p4["paper_quality_passed"] is True

def test_build_paper_research_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_paper_research_summary({}, prof)
    assert "warnings" in res
