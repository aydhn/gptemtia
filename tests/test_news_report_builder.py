import pytest
from advanced_news_metadata.news_report_builder import (
    build_news_provider_disclaimer,
    build_news_provider_profile_registry_markdown_report,
    build_news_source_registry_markdown_report,
    build_news_metadata_schema_markdown_report,
    build_news_safety_markdown_report,
    build_news_quality_markdown_report,
    build_phase_112_handoff_markdown_report
)

def test_news_report_builder():
    disc = build_news_provider_disclaimer()
    assert "Phase 111" in disc
    assert "No Scraping" in disc
    assert "yatırım tavsiyesi" in disc

    rep = build_news_provider_profile_registry_markdown_report({})
    assert "# News Provider Profile Registry" in rep

    handoff = build_phase_112_handoff_markdown_report({})
    assert "Phase 112" in handoff
