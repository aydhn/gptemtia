# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Handoff Report."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.phase_155_handoff import (
    build_phase_155_handoff_report,
    summarize_phase_155_handoff,
)


def test_phase_155_handoff():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_phase_155_handoff_report(profile)
    assert not df.empty
    assert len(df) == 10
    assert summary["all_satisfied"] is True
    assert summary["source_phase"] == 154
    assert summary["target_phase"] == 155
    assert summary["target_final_phase"] == 160
    assert summary["status"] == "HANDOFF_READY"
    assert (df["satisfied"] == True).all()


def test_summarize_phase_155_handoff():
    profile = get_default_portfolio_optimization_profile()
    df, _ = build_phase_155_handoff_report(profile)
    summary = summarize_phase_155_handoff(df)
    assert summary["total_items"] == 10
    assert summary["satisfied_count"] == 10
    assert summary["all_satisfied"] is True
