import pytest
from research_reports.backtest_summary import (
    summarize_backtest_trades,
    summarize_backtest_equity,
    summarize_backtest_quality,
    build_backtest_research_summary
)
from research_reports.research_config import ResearchReportProfile

def test_backtest_trades():
    t = summarize_backtest_trades({})
    assert t["trade_count"] == 0
    assert "win_rate" in t

def test_backtest_equity():
    e = summarize_backtest_equity({})
    assert "total_return_pct" in e

def test_backtest_quality():
    q = summarize_backtest_quality({})
    assert q["lookahead_audit_passed"] is True

def test_build_backtest_research_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_backtest_research_summary({}, prof)
    assert len(res["warnings"]) > 0  # No trades warning
