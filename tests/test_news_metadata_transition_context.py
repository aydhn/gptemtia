"""Tests for News Metadata Transition Context."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.news_metadata_transition_context import (
    build_news_metadata_transition_context_report,
    summarize_news_metadata_transition_context,
    NEWS_METADATA_TRANSITION_DATA,
)


def test_build_news_metadata_transition_context_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_news_metadata_transition_context_report(profile)

    assert not df.empty
    assert len(df) == 3
    assert "metadata_topic_cluster" in df.columns
    assert (df["full_text_used"] == False).all()
    assert (df["scraping_executed"] == False).all()
    assert (df["non_signal"] == True).all()

    assert summary["total_contexts"] == 3
    assert summary["all_metadata_only"] is True
    assert summary["zero_scraping_guaranteed"] is True


def test_summarize_news_metadata_transition_context():
    profile = get_default_regime_transition_profile()
    df, _ = build_news_metadata_transition_context_report(profile)
    summary = summarize_news_metadata_transition_context(df)
    assert summary["total_contexts"] == 3
    assert summary["zero_scraping_guaranteed"] is True
