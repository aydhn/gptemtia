import pytest
from research_reports.performance_summary import (
    summarize_advanced_performance,
    summarize_benchmark_comparison,
    summarize_inflation_adjusted_performance,
    summarize_relative_performance,
    build_performance_research_summary
)
from research_reports.research_config import ResearchReportProfile

def test_performance_summaries():
    p1 = summarize_advanced_performance({})
    assert "sharpe_ratio" in p1

    p2 = summarize_benchmark_comparison({})
    assert "benchmark_outperformance_summary" in p2

    p3 = summarize_inflation_adjusted_performance({})
    assert "tr_cpi_real_return" in p3

    p4 = summarize_relative_performance({})
    assert "usdtry_relative_result" in p4

def test_build_performance_research_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_performance_research_summary({}, prof)
    assert len(res["warnings"]) > 0
