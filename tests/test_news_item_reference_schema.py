import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_item_reference_schema import (
    build_news_item_reference_schema_contract,
    build_default_news_item_reference_fields,
    summarize_news_item_reference_schema
)

def test_news_item_reference_schema():
    profile = get_default_news_provider_profile()
    fields = build_default_news_item_reference_fields(profile)
    assert len(fields) == 10
    df, summary = build_news_item_reference_schema_contract(profile)
    assert len(df) == 10
    assert "no_full_text_policy" in df["field_name"].values
    assert summary["total_fields"] == 10
