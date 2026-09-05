from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_domain_registry import (
    build_data_lineage_domain_registry,
    build_default_data_lineage_domains,
)


def test_domain_registry():
    profile = get_default_data_lineage_profile()
    domains = build_default_data_lineage_domains(profile)
    assert len(domains) >= 25

    df, summary = build_data_lineage_domain_registry(profile)
    assert len(df) >= 25
    assert "fx_lineage_domain" in summary["domain_labels"]
    assert "commodity_lineage_domain" in summary["domain_labels"]
    assert "news_metadata_lineage_domain" in summary["domain_labels"]
