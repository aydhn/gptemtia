"""Tests for Regime Metadata-Only News Acceptance."""

import pandas as pd
from advanced_regime_validation_acceptance.regime_metadata_only_news_acceptance import (
    build_regime_metadata_only_news_acceptance_report,
    validate_metadata_only_news_acceptance,
    validate_no_forbidden_news_content,
    summarize_metadata_only_news_acceptance,
)


def test_metadata_only_news_acceptance():
    df, summary = build_regime_metadata_only_news_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["metadata_only_pure"] is True

    s_df = summarize_metadata_only_news_acceptance(df)
    assert s_df["metadata_only_pure"] is True

    # Validate allowed columns
    allowed_cols = ["news_id", "published_at", "topic_id", "asset_tag", "source_id"]
    assert validate_metadata_only_news_acceptance(allowed_cols)["passed"] is True

    # Validate forbidden columns
    forbidden_cols = ["news_id", "article_body", "scraped_html", "sentiment_score"]
    res_col = validate_metadata_only_news_acceptance(forbidden_cols)
    assert res_col["passed"] is False
    assert "article_body" in res_col["violating_columns"]

    # Validate text content
    clean_text = "News item published at 2026-01-01 with topic central_banks."
    assert validate_no_forbidden_news_content(text=clean_text)["passed"] is True

    dirty_text = "<html><body>Scraped news article body text</body></html>"
    assert validate_no_forbidden_news_content(text=dirty_text)["passed"] is False
