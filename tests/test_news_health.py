import pytest
from pathlib import Path
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_health import (
    build_news_health_check,
    build_default_news_health_findings,
    summarize_news_health
)

def test_news_health():
    profile = get_default_news_provider_profile()
    findings = build_default_news_health_findings(profile)
    assert len(findings) >= 30
    df, summary = build_news_health_check(Path("."), profile)
    assert len(df) >= 30
    assert summary["healthy"] is True
