"""Tests for Phase 132 Macro/Event/News Safety Boundary."""

from advanced_macro_event_news_regime.macro_event_news_regime_safety_boundary import (
    build_macro_event_news_regime_no_go_conditions,
    build_macro_event_news_regime_safe_go_conditions,
    build_macro_event_news_regime_safety_boundary,
    summarize_macro_event_news_regime_safety_boundary,
)


def test_build_safety_boundary():
    no_go, ng_sum = build_macro_event_news_regime_no_go_conditions()
    assert len(no_go) >= 20
    assert ng_sum["all_enforced"] is True

    safe_go, sg_sum = build_macro_event_news_regime_safe_go_conditions()
    assert len(safe_go) >= 9
    assert sg_sum["all_active"] is True

    boundary, b_sum = build_macro_event_news_regime_safety_boundary()
    assert len(boundary) >= 29
    assert b_sum["safety_status"] == "SECURE"
    assert b_sum["all_non_signal"] is True
    assert b_sum["all_source_preserved"] is True


def test_summarize_safety_boundary():
    boundary, _ = build_macro_event_news_regime_safety_boundary()
    summary = summarize_macro_event_news_regime_safety_boundary(boundary)
    assert summary["total_safety_rules"] >= 29
    assert summary["no_go_count"] >= 20
    assert summary["safe_go_count"] >= 9
    assert summary["all_non_signal"] is True
