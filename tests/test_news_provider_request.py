import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_request import (
    create_news_provider_request,
    validate_news_provider_request,
    news_provider_request_to_dict,
    build_news_provider_request_schema
)

def test_news_provider_request():
    profile = get_default_news_provider_profile()
    req = create_news_provider_request("news_dry_run_fixture_provider", "news_data_metadata")
    assert req.dry_run is True
    assert req.local_only is True
    assert req.metadata_only is True

    val = validate_news_provider_request(req, profile)
    assert val["valid"] is True

    df, summary = build_news_provider_request_schema(profile)
    assert len(df) >= 10
