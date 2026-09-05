import pytest
from advanced_news_metadata.news_provider_labels import (
    NEWS_DOMAINS,
    NEWS_SOURCE_CATEGORIES,
    NEWS_DATA_TYPES,
    NEWS_PROVIDER_STATUS,
    NEWS_RISK_LABELS,
    validate_news_domain_label,
    validate_news_source_category_label,
    validate_news_data_type_label,
    validate_news_provider_status_label,
    validate_news_risk_label
)

def test_news_provider_labels():
    assert len(NEWS_DOMAINS) == 35
    assert len(NEWS_SOURCE_CATEGORIES) == 10
    assert len(NEWS_DATA_TYPES) == 8
    assert len(NEWS_PROVIDER_STATUS) == 8
    assert len(NEWS_RISK_LABELS) == 6

def test_label_validators():
    assert validate_news_domain_label("news_metadata_domain") is True
    assert validate_news_domain_label("invalid_domain") is False
    assert validate_news_source_category_label("news_source_central_bank") is True
    assert validate_news_data_type_label("news_data_metadata") is True
    assert validate_news_provider_status_label("news_provider_ready") is True
    assert validate_news_risk_label("news_provider_low_risk") is True
