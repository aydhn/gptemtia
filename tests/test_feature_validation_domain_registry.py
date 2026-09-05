import pytest
from advanced_feature_validation.feature_validation_domain_registry import (
    get_feature_validation_domains_registry,
    get_feature_validation_domains_summary,
)


def test_feature_validation_domain_registry():
    domains = get_feature_validation_domains_registry()
    assert "fx" in domains
    assert "commodity" in domains
    assert "macro" in domains
    assert "calendar" in domains
    assert "news_metadata" in domains
    assert "cross_asset" in domains

    summary = get_feature_validation_domains_summary()
    assert summary["total_domains"] >= 6
    assert summary["current_phase"] == 121
