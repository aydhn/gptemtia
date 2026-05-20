import pytest
from research_reports.technical_summary import (
    summarize_trend_context,
    summarize_momentum_context,
    summarize_volatility_context,
    summarize_regime_context,
    summarize_signal_candidates,
    build_technical_summary
)
from research_reports.research_config import ResearchReportProfile

def test_trend_momentum_volatility_regime():
    assert "trend_label" in summarize_trend_context({})
    assert "momentum_label" in summarize_momentum_context({})
    assert "volatility_label" in summarize_volatility_context({})
    assert "regime_label" in summarize_regime_context({})

def test_summarize_signal_candidates():
    res = summarize_signal_candidates({"signal_candidates": [{"a": 1}]})
    assert res["signal_candidate_count"] == 1
    assert res["strongest_signal_context"] == "supportive_context"

def test_build_technical_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_technical_summary({"signal_candidates": []}, prof)
    assert res["signal_candidate_count"] == 0
    assert "warnings" in res
