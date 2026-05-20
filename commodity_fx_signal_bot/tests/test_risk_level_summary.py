import pytest
from research_reports.risk_level_summary import (
    summarize_risk_candidates,
    summarize_sizing_candidates,
    summarize_level_candidates,
    summarize_reward_risk_context,
    build_risk_level_summary
)
from research_reports.research_config import ResearchReportProfile

def test_risk_summaries():
    r1 = summarize_risk_candidates({"risk_candidates": [1, 2]})
    assert r1["risk_candidate_count"] == 2

    r2 = summarize_sizing_candidates({"sizing_candidates": [1]})
    assert r2["sizing_candidate_count"] == 1

    r3 = summarize_level_candidates({})
    assert r3["level_candidate_count"] == 0

def test_reward_risk():
    rr = summarize_reward_risk_context({})
    assert rr["avg_reward_risk"] > 0

def test_build_risk_level_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_risk_level_summary({}, prof)
    assert res["risk_candidate_count"] == 0
