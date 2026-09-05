import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_metadata_schema import (
    build_news_metadata_schema_contract,
    build_default_news_metadata_schema_fields,
    summarize_news_metadata_schema
)

def test_news_metadata_schema():
    profile = get_default_news_provider_profile()
    fields = build_default_news_metadata_schema_fields(profile)
    assert len(fields) >= 20
    df, summary = build_news_metadata_schema_contract(profile)
    assert len(df) >= 20
    assert "metadata_only" in df["field_name"].values
    assert "title_or_summary_ref" in df["field_name"].values
    assert summary["total_fields"] >= 20
