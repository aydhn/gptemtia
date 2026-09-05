"""Tests for News Metadata Fusion Contracts."""

from advanced_feature_fusion.news_metadata_fusion_contracts import (
    build_news_metadata_fusion_contract_registry,
    get_news_metadata_contracts,
    summarize_news_metadata_fusion_contracts,
)


def test_news_metadata_contracts():
    df, summary = build_news_metadata_fusion_contract_registry()
    assert len(df) == 6
    assert summary["total_contracts"] == 6
    assert summary["metadata_only_verified"] is True
    assert summary["non_signal_guaranteed"] is True


def test_news_metadata_contracts_list():
    contracts = get_news_metadata_contracts()
    assert len(contracts) == 6
    assert any(c["contract_name"] == "news_topic_metadata_contract" for c in contracts)
