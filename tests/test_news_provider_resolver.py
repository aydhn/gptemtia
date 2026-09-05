import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_registry import build_default_news_provider_registry
from advanced_news_metadata.news_provider_request import create_news_provider_request
from advanced_news_metadata.news_provider_resolver import (
    resolve_news_provider_for_request,
    build_news_provider_resolver_map,
    summarize_news_provider_resolver_map
)

def test_news_provider_resolver():
    profile = get_default_news_provider_profile()
    reg = build_default_news_provider_registry(profile)
    req = create_news_provider_request("news_dry_run_fixture_provider", "news_data_metadata")
    prov = resolve_news_provider_for_request(req, reg, profile)
    assert prov is not None
    assert prov.provider_name == "news_dry_run_fixture_provider"

    df, summary = build_news_provider_resolver_map(profile)
    assert len(df) == 3
    assert summary["total_mappings"] == 3
