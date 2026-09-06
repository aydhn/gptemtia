"""Tests for Phase 132 Macro/Event/News Report Builder."""

import pandas as pd
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_macro_event_news_regime_disclaimer,
    build_macro_event_news_regime_profile_markdown_report,
    build_macro_event_news_entity_markdown_report,
    build_macro_context_markdown_report,
    build_event_context_markdown_report,
    build_news_metadata_context_markdown_report,
    build_metadata_only_boundary_markdown_report,
    build_macro_event_news_cross_asset_markdown_report,
    build_macro_event_news_findings_markdown_report,
    build_macro_event_news_score_markdown_report,
    build_macro_event_news_manifest_markdown_report,
    build_macro_event_news_validation_markdown_report,
    build_macro_event_news_safety_markdown_report,
    build_phase_133_handoff_markdown_report,
)


def test_disclaimer_presence():
    disc = build_macro_event_news_regime_disclaimer()
    assert "Phase 132" in disc
    assert "YASAL UYARI" in disc
    assert "investment advice" not in disc or "yatırım tavsiyesi" in disc


def test_report_builders_output():
    summary = {"current_phase": 132, "next_phase": 133, "context_score": 1.0}
    df = pd.DataFrame([{"col1": "val1"}])

    rep1 = build_macro_event_news_regime_profile_markdown_report(summary, df)
    assert "# Phase 132" in rep1
    assert "val1" in rep1

    rep2 = build_macro_event_news_entity_markdown_report(summary, df)
    assert "Entities Report" in rep2

    rep3 = build_macro_context_markdown_report(summary, df)
    assert "Macro Indicator" in rep3

    rep4 = build_event_context_markdown_report(summary, df)
    assert "Economic Calendar" in rep4

    rep5 = build_news_metadata_context_markdown_report(summary, df)
    assert "News Metadata" in rep5

    rep6 = build_metadata_only_boundary_markdown_report(summary, df)
    assert "Metadata-Only News Boundary" in rep6

    rep7 = build_macro_event_news_cross_asset_markdown_report(summary, df)
    assert "Cross-Asset" in rep7

    rep8 = build_macro_event_news_findings_markdown_report(summary, df)
    assert "Findings Report" in rep8

    rep9 = build_macro_event_news_score_markdown_report(summary, df)
    assert "Score Report" in rep9

    rep10 = build_macro_event_news_manifest_markdown_report(summary, df)
    assert "Context Manifest" in rep10

    rep11 = build_macro_event_news_validation_markdown_report(summary, df)
    assert "Validation Report" in rep11

    rep12 = build_macro_event_news_safety_markdown_report(summary, df)
    assert "Safety Boundary Report" in rep12

    rep13 = build_phase_133_handoff_markdown_report(summary, df)
    assert "Phase 133" in rep13
