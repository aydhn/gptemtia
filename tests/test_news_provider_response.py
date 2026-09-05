import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_response import (
    create_news_provider_response,
    validate_news_provider_response,
    news_provider_response_to_dict,
    build_news_provider_response_schema
)

def test_news_provider_response():
    profile = get_default_news_provider_profile()
    res = create_news_provider_response("req_1", "prov_1", "news_data_metadata", "news_provider_ready")
    assert res.response_id is not None
    assert res.manual_review_required is True

    val = validate_news_provider_response(res, profile)
    assert val["valid"] is True

    df, summary = build_news_provider_response_schema(profile)
    assert len(df) == 10
