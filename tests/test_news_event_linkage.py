import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_event_linkage import (
    build_news_event_linkage_registry,
    build_default_news_event_linkages,
    summarize_news_event_linkage
)

def test_news_event_linkage():
    profile = get_default_news_provider_profile()
    linkages = build_default_news_event_linkages(profile)
    assert len(linkages) >= 6
    df, summary = build_news_event_linkage_registry(profile)
    assert len(df) >= 6
    assert "FOMC_RATE_DECISION" in df["linked_calendar_event"].values
    assert summary["total_linkages"] >= 6
