import pandas as pd
import pytest
from advanced_feature_quality_drift.macro_calendar_news_quality import (
    build_macro_calendar_news_quality_report,
    summarize_macro_calendar_news_quality,
)


def test_macro_calendar_news_quality_clean():
    df, summary = build_macro_calendar_news_quality_report()
    assert not df.empty
    assert summary["failed_checks"] == 0
    assert summary["metadata_only_boundary_compliant"] is True
    assert summary["status"] == "diagnostic_pass"


def test_macro_calendar_news_quality_forbidden_article_body():
    bad_df = pd.DataFrame({
        "timestamp": ["2026-01-01"],
        "article_body": ["Full text of news article..."],
    })
    df, summary = build_macro_calendar_news_quality_report(df=bad_df)
    assert summary["failed_checks"] > 0
    assert summary["metadata_only_boundary_compliant"] is False
    assert summary["status"] == "diagnostic_fail"
    assert summary["manual_review_required"] is True
