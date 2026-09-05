import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_dry_run_fixture import (
    NewsDryRunFixtureProvider,
    build_news_dry_run_fixture_report,
    run_news_dry_run_examples,
    summarize_news_dry_run_fixture
)
from advanced_news_metadata.news_provider_request import create_news_provider_request

def test_news_dry_run_fixture():
    profile = get_default_news_provider_profile()
    prov = NewsDryRunFixtureProvider()
    req = create_news_provider_request(prov.provider_name, "news_data_metadata")
    res = prov.fetch_news_metadata(req)
    assert res.provider_name == prov.provider_name
    assert res.row_count > 0
    assert "dry_run://" in res.output_ref

    df, summary = run_news_dry_run_examples(profile)
    assert len(df) == 2
    assert summary["total_requests"] == 2
