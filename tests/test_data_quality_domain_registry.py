import pytest
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_domain_registry import (
    build_data_quality_domain_registry,
    build_default_data_quality_domains,
    summarize_data_quality_domains,
)


def test_data_quality_domain_registry():
    profile = get_default_data_quality_profile()
    domains = build_default_data_quality_domains(profile)
    assert len(domains) >= 25

    df, summary = build_data_quality_domain_registry(profile)
    assert len(df) >= 25
    assert summary["total_domains"] >= 25
    assert summary["current_phase"] == 112
    assert "schema_compliance_domain" in summary["domain_labels"]
