"""Tests for Fusion Feature Domain Registry."""

from advanced_feature_fusion.fusion_feature_domain_registry import (
    build_fusion_feature_domain_registry,
    get_fusion_feature_domains_registry,
    get_fusion_feature_domains_summary,
)


def test_domain_registry():
    df, summary = build_fusion_feature_domain_registry()
    assert len(df) == 35
    assert summary["total_domains"] == 35
    assert summary["status"] == "READY"


def test_domain_helpers():
    df = get_fusion_feature_domains_registry()
    assert len(df) == 35
    summary = get_fusion_feature_domains_summary()
    assert summary["total_domains"] == 35
